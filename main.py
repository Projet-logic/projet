# -*- coding: utf-8 -*-
"""
Created on Mon May 3 10:12:24 2023

@author: Vinh
"""
from algo import *
from Game import Game
from formula_d import formula,AND,OR
import pycosat as sat


from algo import *
from Game import Game
from formula_d import formula,AND,OR
import pycosat as sat


def save_dimacs(formule, filename):
    """Saves the clauses provided in the first argument to the file provided in the
    second argument in DIMACS format.
    Expected format of clauses: list of integers (DIMACS format compatible with pycosat)"""
    
    # Initialize the number of clauses and a set to store the variables in the formula
    nb_clauses = 0
    variables = set()

    # Count the number of clauses and add each variable to the set
    for clause in formule:
        nb_clauses += 1
        variables |= set(map(abs, clause))

    # Write the formula in DIMACS format to the file
    with open(filename, "w") as file:
        # Write the header
        file.write("c Fichier DIMACS\n")
        file.write(f"p cnf {len(variables)} {nb_clauses}\n")

        # Write each clause
        for clause in formule:
            file.write(" ".join(str(v) for v in clause) + " 0\n")

#---------------------------------------------------------------------------------
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
 
#---------------------------use pycosat------------------------------------------------ 
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
        
        
 #-----------------------------------------main function--------------------------------                                   
def main():
    try:
        g=Game()
        f=create_formula_iterative(g)
        print(f"formula = {f}")
        #f.dev()
        #print(f"development = {f}")
        
        final_list=extract_variables(str(f))
        print(final_list)
        save_dimacs(final_list, "sat.cnf")
        satSolution(final_list)       
        
    except:
        print("you have some problem or that's end, lets restart")


            
            
    
if __name__=='__main__':
    main()
