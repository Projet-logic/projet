# -*- coding: utf-8 -*-
"""
Created on Mon May  1 16:12:46 2023

@author: moham & Vinh & Yuchen
"""
from algo import *
from Game import Game
from formula_d import formula,AND,OR

def save_dimacs(formule, filename):
    """
    Saves the clauses provided in the first argument to the file provided in the
    second argument in DIMACS format.
    Expected format of clauses: list of integers (DIMACS format compatible with a DPLL solveur, 
    i think pycosat or python-sat but i dont try to test yet)
    """
    
    # Initialiser le nombre sur clauses et un ensemble pour stocker les variables dans la formule.
    nb_clauses = 0
    variables = set()

    # Compter le nombre de clauses et ajouter chaque variable à l'ensemble.
    for clause in formule:
        nb_clauses += 1
        variables |= set(map(abs, clause))

    # Écrire la formule au format DIMACS dans le fichier.
    with open(filename, "w") as file:
        # Write the header
        file.write("c Fichier DIMACS\n")
        file.write(f"p cnf {len(variables)} {nb_clauses}\n")

        # Write each clause
        for clause in formule:
            file.write(" ".join(str(v) for v in clause) + " 0\n")
    
def main():
    while True:
        try:
            g=Game()
            f=create_formula_iterative(g)
            print(f"formula = {f}")
            f.dev()
            print(f"development = {f}")
            save_dimacs(f, "dimacs.txt")
            input()
            return 1
        except:
            print("you have some problem lets restart")
    
if __name__=='__main__':
    main()
