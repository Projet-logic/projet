# -*- coding: utf-8 -*-
"""
Created on Mon May  1 16:12:46 2023

@author: moham & Vinh & Yuchen
"""
from algo import *
from Game import Game
from formula_d import formula,AND,OR
import minisat as sat

class CNF:
    
    def __init__(self):
        self.clauses = []
        self.num_vars = 0

    def add_clause(self, literals):
        self.clauses.append(literals)

        for literal in literals:
            if abs(literal) > self.num_vars:
                self.num_vars = abs(literal)

    def to_dimacs(self):
        lines = []
        lines.append(f"p cnf {self.num_vars} {len(self.clauses)}")

        for clause in self.clauses:
            line = " ".join(str(literal) for literal in clause)
            line += " 0"
            lines.append(line)

        return "\n".join(lines)
                    
def main():
    while True:
        try:
            g=Game()
            f=create_formula_iterative(g)
            print(f"formula = {f}")
            f.dev()
            print(f"development = {f}")
            
            cnf = CNF()
            
            # transformer au fichier CNF
            for clause in f.clauses:
                cnf.add_clause(clause)
            
            # Sauvegarder CNF au fichier DIMACS
            with open("formula.dimacs", "w") as file:
                file.write(cnf.to_dimacs())
                
            # Resoudre SAT par SAT Solveur
            with open("formula.dimacs", "r") as file:
                cnf = sat.CNF(from_file=file)
                solver = sat.Solver()
                solver.append_formula(cnf.clauses)
                is_sat, model = solver.solve()
                
                if is_sat:
                    print("the formula is correct")
                    print(f"A valid alternative: {model}")
                else:
                    print("the formula is not correct")
            return 1
        except:
            print("you have some problem or that's end, lets restart")
            
            
    
if __name__=='__main__':
    main()
