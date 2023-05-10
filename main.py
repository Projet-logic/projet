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
     #   nb_clauses += 1
     #   variables |= set(map(abs, clause))

    # Ecrire la formule au format DIMACS dans le fichier
    with open(filename, "w") as file:
        # Ecrire l'en-tête
        file.write("c Fichier DIMACS\n")
        file.write(f"p cnf {len(variables)} {nb_clauses}\n")

        # Ecrire chaque clause
        for clause in formule._table:
            file.write(" ".join(str(v) for v in clause._table) + " 0\n")

#---------------------------------------------------------------------------------#

def read_dimacs_file(filename):
    """Reads a DIMACS format file and returns a list of clauses."""
    clauses = []

    with open(filename, "r") as file:
        for line in file:
            if line.startswith("c") or line.startswith("p"):
                continue  # Skip comments and problem line
            clause = [x for x in line.split()[:-1]]  # Exclude the trailing 0
            clauses.append(clause)

    return clauses

def convert_variables_to_numbers(formula, variable_map):
    """Converts variable names in the formula to numeric values based on the variable map."""
    converted_formula = []

    for clause in formula:
        converted_clause=[]
        for var in clause:
            if(var[0]=='-'):
                converted_clause.append(-variable_map[var[1:]])
            else:
                converted_clause.append(variable_map[var])
        converted_formula.append(converted_clause)

    return converted_formula

def convert_numbers_to_variables(result, variable_map):
    """Converts variable names in the formula to numeric values based on the variable map."""
    converted_result = []
    # Create a reverse mapping of the variable map
    variable_map_reverse = {value: key for key, value in variable_map.items()}
    for var in result:
        if(var<0):
            converted_result.append('-'+variable_map_reverse[abs(var)])
        else:
            converted_result.append(variable_map_reverse[var])

    return converted_result


def create_num(g:Game):
    res=dict();
    j=1
    for i in g.get_possib_var_horiz():
        res[i.name]=j
        j+=1
    for i in g.get_possib_var_vert():
        res[i.name]=j
        j+=1
    return res
    


#---------------------------USE PYCOSAT------------------------------------------------# 
 # Trouver une solution
def satSolution(final_list,variable_map):
    
    solution = sat.solve(final_list)
    # Si une solution a été trouvée, l'afficher et mettre à jour le texte
    if not (solution == "UNSAT" or solution == "UNKNOWN" or solution == []):
        solution=convert_numbers_to_variables(solution, variable_map)
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
        if(not f):
            print("Aucune solution trouvée!")
            return 0
        f.env_val()
        print(f"formula = {f}")
        variable_map=create_num(g)
        #print(variable_map)
        dimacs(f, "sat.cnf")
        final_list = read_dimacs_file("sat.cnf")
        #print(final_list), this line is for testing
        final_list=convert_variables_to_numbers(final_list, variable_map)
        #print(final_list), this line is for testing
        satSolution(final_list,variable_map)    
        return 0
        
    except:
        print("you have some problem or that's end, lets restart")


            
            
    
if __name__=='__main__':
    main()


