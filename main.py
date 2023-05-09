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
    #for clause in formule:
    #    nb_clauses += 1
    #    variables |= set(map(abs, clause))

    # Ecrire la formule au format DIMACS dans le fichier
    with open(filename, "w") as file:
        # Ecrire l'en-tête
        file.write("c\n")
        file.write("c start with comments\n")
        file.write("c\n")
        file.write("c\n")
        file.write(f"p cnf {len(variables)} {nb_clauses}\n")

        # Ecrire chaque clause
        for clause in formule._table:
            file.write(" ".join(str(v) for v in clause._table) + " 0\n")

#---------------------------------------------------------------------------------#

def read_dimacs_file(filename):
    """Reads a DIMACS format file and returns a list of clauses."""
    clauses = []

    with open(filename, "r") as file:
        for i, line in enumerate(file):
            if i >= 5:
                clause = [x for x in line.split()[:-1]]  # Exclude the trailing 0
                clauses.append(clause)


    return clauses

def convert_variables_to_numbers(formula):
    """Converts variable names in the formula to numeric values."""
    converted_formula = []

    for clause in formula:
        converted_clause=[]           
        for var in clause :
            value = int(var)
            converted_clause.append(value)                 
        converted_formula.append(converted_clause)

    return converted_formula

def convert_numbers_to_solved_by_pycosat(lists):
    """Converts variable names in the formula to numeric values that can be solved by pycosat"""
    dictionary = {}
    result = []
    n = 1
    for small_list in lists:
        for value in small_list:
            if value not in dictionary:
                if value > 0:
                    dictionary[value] = n
                    dictionary[value*(-1)] = n*(-1)
                    n+=1
                else:
                    dictionary[value] = n*(-1)
                    dictionary[value*(-1)] = n
                    n+=1
            
            
    for small_list in lists:
        new_small_list = [dictionary[value] for value in small_list]
        result.append(new_small_list)

    return result


#---------------------------USE PYCOSAT------------------------------------------------# 
 # Trouver une solution
def satSolution(final_list):
    
    solution = sat.solve(final_list)
    # Si une solution a été trouvée, l'afficher et mettre à jour le texte
    if not (solution == "UNSAT" or solution == "UNKNOWN" or solution == []):
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
        """
        if(not f):
            print("Aucune solution trouvée!")
            return 1
        """
        print(f"formula = {f}")
        f.dev()
        print(f"development = {f}")
        dimacs(f, "sat.cnf")
        dimacs_file = read_dimacs_file("sat.cnf")
        print(dimacs_file)
        list_converted=convert_variables_to_numbers(dimacs_file)
        print(list_converted)
        final_list = convert_numbers_to_solved_by_pycosat(list_converted)
        print(final_list)
        satSolution(final_list)       
        
    except:
        print("you have some problem or that's end, lets restart")


            
            
    
if __name__=='__main__':
    main()


