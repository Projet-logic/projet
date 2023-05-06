# -*- coding: utf-8 -*-
"""
Created on Mon May  1 16:12:46 2023

@author: Vinh 
"""
from algo import *
from Game import Game
from formula_d import formula,AND,OR
import pycosat as sat


def save_dimacs(formule, filename):
    """
        Enregistre les clauses fournies en 1e argument dans le fichier fourni en
            2e argument au format DIMACS.
         Format de clauses attendu: liste d'entiers (format dimacs compatible avec
        pycosat)
    """    
    #Initialisation du nombre de clause
    nb_clauses = 0
    #Initialisation d'une liste pour chercher le nombre de variables de la formule
    listeVar=[]

    for clause in formule:
        # incrémenter le nombre de clauses
        nb_clauses+=1
        # Pour chaque variable, si elle n'est pas dans listeVar, incrementer
        # le compteur du nombre de variable et l'ajouter dans listeVar
        for variable in clause:
            if not(variable in listeVar) and not(-variable in listeVar):
                listeVar.append(variable)
    #Ecriture du le fichier au format DIMACS
    with open(filename, "w") as fichier:
        # En-tête
        fichier.write("c Fichier DIMACS\n")
        fichier.write("p cnf ")
        fichier.write(str(len(listeVar)))
        fichier.write(" ")
        fichier.write(str(nb_clauses))
        fichier.write("\n")
        # Clauses
        for clause in formule:
            i = 1
            for variable in clause:
                fichier.write(str(variable))
                fichier.write(" ")
                if i == len(clause):
                    fichier.write("0")
                i += 1
            fichier.write("\n")

def extract_variables(s):
    # Diviser les chaînes en variables et calculs
    values = s.split('*')
    variables = []
    for val in values:
        if val[0] == "(":
            variables.append(val[1:len(val)-1])
        else:
            variables.append(val)
            
    #créer des sous-listes dans une grande liste       
    big_list = []
    for val in variables:
        if "-" in val and "+" in val:
            t = val.split('+')
            big_list.append(t)
        elif "+" in val and "-" not in val:
            t = val.split("+")
            big_list.append(t) 
        else :
            big_list.append([val])
            
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
            
    for sublist in variable_names:
        new_sublist = []
        for element in sublist:
            try:
                new_sublist.append(int(element))
            except ValueError:
                new_sublist.append(element)
        int_variable_names.append(new_sublist)
    return int_variable_names
 
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
                                    
def main():
    try:
        g=Game()
        f=create_formula_iterative(g)
        print(f"formula = {f}")
        #f.dev()
        #print(f"development = {f}")
        
        final_list=extract_variables(f)
        print(final_list)
        satSolution(final_list)       
        save_dimacs(sat, sat.cnf)
    except:
        print("you have some problem or that's end, lets restart")


            
            
    
if __name__=='__main__':
    main()
