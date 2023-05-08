# -*- coding: utf-8 -*-
"""
Created on Mon May  1 16:12:46 2023

@author: Tang Khac Vinh
"""
from tkinter import *
from algo import *
from Game import Game
from formula_d import formula,AND,OR
import pycosat as sat
import re

#------------------------------SAVE DIMACS--------------------------------------
def dimacs(formule, filename):
    """
    Enregistre les clauses fournies dans le premier argument dans le fichier fourni dans le
     deuxième argument au format DIMACS.
    Format attendu des clauses : liste d'entiers (format DIMACS compatible avec pycosat)
    """
    
    # Initialiser le nombre de clauses et un ensemble pour stocker les variables dans la formule
    nb_clauses = 0
    variables = set()

    # Compter le nombre de clauses et ajouter chaque variable à l'ensemble
    for clause in formule:
        nb_clauses += 1
        variables |= set(map(abs, clause))

    # Ecrire la formule au format DIMACS dans le fichier
    with open(filename, "w") as file:
        # Ecrire l'en-tête
        file.write("c Fichier DIMACS\n")
        file.write(f"p cnf {len(variables)} {nb_clauses}\n")

        # Ecrire chaque clause
        for clause in formule:
            file.write(" ".join(str(v) for v in clause) + " 0\n")

#---------------------------------------------------------------------------------#
"""
convertir la formule en une forme utilisable et solvable par pycosat
"""
def extract_variables(s):
    # Diviser les chaînes en variables et calculs
    s= s[1:len(s)-1]

    # Rechercher et diviser des sous-chaînes
    variables = re.findall(r'\((?:[^(]+|\((?:[^(]+|\([^()]+\))*\))*\)|\d+', s)

            
    #créer des sous-listes dans une grande liste       
    big_list = []
    for val in variables:
        if val[0] == "(":
            val = val[1:len(val)-1]
            
        if "-" in val and "+" in val:
            t = val.split('+')
            big_list.append(t)
        elif "+" in val and "-" not in val:
            t = val.split("+")
            big_list.append(t) 
        else :
            big_list.append([val])
    #print(big_list)
            
    #donner des noms numériques aux variables
    variable_names = []
    int_variable_names = []

    var_dict = {}
    var_num = 1

    for sublist in big_list:
        new_sublist = []
        for item in sublist:
            if item[0] == '-':
                # check if the positive variable has already been assigned a name
                pos_var = item[1:]
                if pos_var in var_dict:
                    new_sublist.append('-' + var_dict[pos_var])
                else:
                    var_dict[pos_var] = str(var_num)
                    new_sublist.append('-' + str(var_num))
                    var_num += 1
            else:
                if item in var_dict:
                    new_sublist.append(var_dict[item])
                else:
                    var_dict[item] = str(var_num)
                    new_sublist.append(str(var_num))
                    var_num += 1
        variable_names.append(new_sublist)
    #print(variable_names)
            
    for sublist in variable_names:
        new_sublist = []
        for element in sublist:
            try:
                new_sublist.append(int(element))
            except ValueError:
                new_sublist.append(element)
        int_variable_names.append(new_sublist)
    return int_variable_names

#---------------------------USE PYCOSAT------------------------------------------------# 
 # Trouver une solution
def satSolution(final_list):
    
    solution = sat.solve(final_list)
    # Si une solution a été trouvée, l'afficher et mettre à jour le texte
    if not (solution == "UNSAT" or solution == "UNKNOWN"):
        print(solution)
        print("Solution trouvée!")
    # Sinon, juste mettre a jour le texte
    else:
        print("Aucune solution trouvée!")
        
        
 #-----------------------------------------MAIN FUNCTION--------------------------------#                                   
def main():
    try:
        g=Game()
        f=create_formula_iterative(g)
        print(f"formula = {f}")
        #f.dev()
        #print(f"development = {f}")
        
        final_list=extract_variables(str(f))
        #print(final_list)
        dimacs(final_list, "sat.cnf")
        satSolution(final_list)       
        
    except:
        print("you have some problem or that's end, lets restart")


            
            
    
if __name__=='__main__':
    main()


