# -*- coding: utf-8 -*-
"""
Created on Mon May  1 10:36:00 2023

@author: moham
"""
from formula_d import formula,AND,OR
from Game import Game
from itertools import combinations
from copy import deepcopy


def ens_possible_connexion(g:Game,alpha:int,beta:int,n1:int):
    tmp=g.get_variable_possible()[str(alpha)]
    for var in list(tmp):
        if((var.name[0]==str(beta) and var.name[1]==str(alpha) )or( var.name[1]==str(beta) and var.name[0]==str(alpha))):
            tmp.remove(var)
    return combinations(tmp, n1)

def next_circle(l_variables,alpha):
    res=list()
    for var in l_variables:
        if(var.name[0]==str(alpha) and not int(var.name[1]) in res ):
            res.append(int(var.name[1]))
        elif(var.name[1]==str(alpha) and not int(var.name[1]) in res):
            res.append(int(var.name[0]))
    return res

def create_formula_rec(F:formula ,game:Game, list_of_seen_island : list,alpha:int,beta:int, c:tuple,tb:dict): 
    #input(f"args  entrance = \n{F}\n{game._islands}\n{game.get_variable_interdi()}\n{list_of_seen_island}\n{alpha} \n {beta} \n {c} \n {tb}\n")
    list_of_seen_island[alpha-1]=1
    n1=c[2]- tb[str(alpha)]
    if(not n1):
        return F,all(list_of_seen_island)
    li=ens_possible_connexion(game, alpha, beta, n1)
    f1=formula(connector=OR)
    is_one_bloc=False
    for S in li:
        f2=formula(connector=AND)
        next_circles=next_circle(S,alpha)
        tb_copy=deepcopy(tb)
        list_of_seen_island_copy=deepcopy(list_of_seen_island)
        list_name_in_S=list(map(lambda x:x.name,S))
        for var in S:
            IN=game.get_variable_interdi()[var.name[:-1]]
            #for i in IN:
                #print(i,end=" ")
            #print()
            #print (f"possible variable for {alpha}:")
            for v in game.get_variable_possible()[str(alpha)]:
                #print(v)
                if (v.name not in list_name_in_S and v.name[0]!=str(beta) and v.name[1]!=str(beta) ):
                    IN.append(v)
            f2*=var
            tb_copy[str(alpha)]+=1
            if(var.name[0]==str(alpha)):
                tb_copy[var.name[1]]+=1
            else:
                tb_copy[var.name[0]]+=1
            #print(f"forbidden varibles for {var} are\n")
            for var_i in IN:
                f2*=(-var_i)
                #print(var_i)
                
        for n in next_circles:
            c_next=game.get_circle(n-1)
            tmp=formula()
            tmp,condi=create_formula_rec(tmp, game,list_of_seen_island_copy , n, alpha, c_next, tb_copy)
            if(not condi):
                break
            f2*=tmp
        if(condi):
            f1+=f2
        is_one_bloc= is_one_bloc or condi
        
    F*=f1
    #input(f"args  exit = {F}\n{game._islands}\n{list_of_seen_island}\n{alpha} \n {beta} \n {c} \n {tb}\n")
    return F, is_one_bloc
            
        
def create_formula(game:Game):
    res=formula()
    list_of_seen_island=[0 for i in range(len(game._list_islands))]
    tb=dict([(str(i+1),0) for i in range(len(game._list_islands)) ] )
    c=game.get_circle(0)
    res,is_one_bloc=create_formula_rec(res, game, list_of_seen_island, 1, 0, c, tb)
    return res,is_one_bloc
    