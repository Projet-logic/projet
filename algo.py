# -*- coding: utf-8 -*-
"""
Created on Mon May  1 10:36:00 2023

@author: moham
"""
from formula_d import formula,AND,OR
from Game import Game
from itertools import combinations
from copy import deepcopy


def ens_possible_connexion(g:Game,alpha:int,connexions:dict,n1:int):
    #print(n1)
    c_already_seen=list()
    
    tmp=g.get_variable_possible()[str(alpha)]
    
    for var in list(tmp):
        if(connexions[var.name[:-1]]):
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

def create_formula_rec(F:formula ,game:Game,alpha:int,beta:int,connexions:dict, c:tuple,tb:dict): 
    #print(f"args  entrance = \n{F}\n{game.get_variable_interdi()}\n{alpha}\n{connexions}  \n {c} \n {tb}\n")
    n1=c[2]- tb[str(alpha)]
    if(n1==0):
        #print("1")
        l=[0 for i in range(len(game._list_islands))]
        l[alpha-1]=1
        return F,l,True
    elif(n1<0):
        #print("2,False")
        l=[0 for i in range(len(game._list_islands))]
        return F,l,False
    li=list(ens_possible_connexion(game, alpha, connexions, n1))
    if(not len(li)):
        #print("3,False")
        l=[0 for i in range(len(game._list_islands))]
        return F,l,False
    f1=formula(connector=OR)
    is_one_bloc=False
    
    for S in li:
        #input("hello")
        #input(f"S={S}")
        f2=formula(connector=AND)
        next_circles=next_circle(S,alpha)
        tb_copy=deepcopy(tb)
        #list_of_seen_island_copy=deepcopy(list_of_seen_island)
        #for n in next_circles:
         #   list_of_seen_island_copy[n-1]=1
        list_name_in_S=list(map(lambda x:x.name,S))
        #input(list_name_in_S)
        IN=list()
        IN_names=list()
        condi_g=False
        for var in S:
            #input(f"var={var}")
            connexions[var.name[:-1]]=1
            IN.extend(game.get_variable_interdi()[var.name[:-1]])
            IN_names.extend(list(map(lambda x:x.name,IN)))
            for i in IN:
               print(i,end=" ")
            #input()
            #input (f"possible variable for {alpha}:")
            for v in game.get_variable_possible()[str(alpha)]:
                #input(v)
                if (v.name not in list_name_in_S and v.name[0]!=str(beta) and v.name[1]!=str(beta) and v.name not in IN_names ):
                    IN.append(v)
                    IN_names.append(v.name)
            f2*=var
            tb_copy[str(alpha)]+=1
            if(var.name[0]==str(alpha)):
                tb_copy[var.name[1]]+=1
            else:
                tb_copy[var.name[0]]+=1
            #input(f"forbidden varibles for {var} are\n")
            for var_i in list(IN):
                f2*=(-var_i)
                IN.remove(var_i)
                #input(var_i)
        list_of_seen_island=[0 for i in range(len(game._list_islands))]        
        for n in next_circles:
            list_of_seen_island[n-1]=1
            c_next=game.get_circle(n-1)
            tmp=formula()
            tmp,l,condi=create_formula_rec(tmp, game , n, alpha, deepcopy(connexions) ,c_next, tb_copy)
            if(not condi):
                break
            list_of_seen_island= list_of_seen_island or l
            f2*=tmp
        condi_g=condi_g or condi
        if(condi) :
            f1+=f2
        else:
            list_of_seen_island=[0 for i in range(len(game._list_islands))]
            continue
    F*=f1
    #input(f"args  exit = {F}\n{list_of_seen_island}\n{game.get_variable_interdi()}\n{alpha} \n {beta} \n {c} \n {tb}\n")
    return F, list_of_seen_island,condi_g
            
def create_formula(game:Game):
    res=formula()
    tb=dict([(str(i+1),0) for i in range(len(game._list_islands)) ] )
    connexions=dict([(i.name[:-1],0) for i in game.get_possib_var_horiz()]+[(i.name[:-1],0) for i in game.get_possib_var_vert()])
    c=game.get_circle(0)
    res,is_one_bloc,r=create_formula_rec(res, game, 1, 0, connexions,c, tb)
    return res,is_one_bloc,r
    
