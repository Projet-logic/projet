# -*- coding: utf-8 -*-
"""
Created on Mon May  1 10:36:00 2023

@author: moham
"""
from formula_d import formula,AND,OR
from Game import Game
from itertools import combinations
from copy import deepcopy




def ens_possible_connexion(g:Game,c:tuple):
    
    tmp=g.get_variable_possible()[str(c[2])]
    return combinations(tmp, c[2])

def create_formula_iterative(game:Game):
    F=formula()
    alpha=1
    for c in game.get_list():
        
        li=list(ens_possible_connexion(game, c))
        f1=formula()
        for S in li:
            list_name_in_S=list(map(lambda x:x.name,S))
            f2=formula()
            IN=list()
            IN_names=list()
            for var in S:
                IN.extend(game.get_variable_interdi()[var.name[:-1]])
                IN_names.extend(list(map(lambda x:x.name,IN)))
                for v in game.get_variable_possible()[str(alpha)]:
                    if (v.name not in list_name_in_S and v.name not in IN_names ):
                        IN.append(v)
                        IN_names.append(v.name)
                f2*=var
                for var_i in list(IN):
                    f2*=(-var_i)
                    IN.remove(var_i)
            f1+=f2
        F*=f1
        f3=formula()
        for var in game.get_variable_possible()[str(alpha)]:
            f3+=var
        F*=f3
        alpha+=1
    return F
        
