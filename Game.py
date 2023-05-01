# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 06:02:56 2023

@author: moham
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 01:09:20 2023

@author: Tang Khac Vinh

FILE DESCRIPTION:
       game module for Hashiwokakero
"""

from formula_d import *
from connector_d import *
from UI import *
from copy import deepcopy
class Game:
   
    
    def __init__(self):
        l,m,n=init_game()
        #l=[(1,1,4),(1,3,5),(1,6,2),(4,1,4),(4,3,8),(4,6,5),(6,6,2),(7,1,2),\
           #(7,3,4)]
        #m=8
        #n=8
        self._list_islands=l
        self._islands=[[0 for j in range(m)] for i in range(n)]
        for c in l:
            self._islands[c[0]][c[1]]=c[2]
        self._m=m
        self._n=n
        c=self.__possible_connexion()
        self._possible_connexion_vert=c[0]
        self._possible_connexion_horiz=c[1]
        self._possible_variable_horiz=self.__possible_v(self._possible_connexion_horiz)
        self._possible_variable_vert=self.__possible_v(self._possible_connexion_vert)
        self._dict_variables_interdit=self.__variables_interdit()
        self._dict_variables_possible=self.__variable_possible()
        
        
 
    def __possible_connexion(self):
        i=0
        c_vert=list()
        c_horiz=list()
        while (i<self._n):
            j=0
            c=list()
            while(j<self._m):
                if(self._islands[i][j] ):
                    c.append((i,j,self._islands[i][j]))
                    if(len(c)==2):
                        c_horiz.append(tuple(c))
                        c=list()
                        c.append((i,j,self._islands[i][j]))
                j+=1
            i+=1
        i=0
        while (i<self._m):
            j=0
            c=list()
            while(j<self._n):
                if( self._islands[j][i] ):
                    c.append((j,i,self._islands[j][i]))
                    if(len(c)==2):
                        c_vert.append(tuple(c))
                        c=list()
                        c.append((j,i,self._islands[j][i]))
                j+=1
            i+=1
        return c_vert,c_horiz
                
    def get_circle(self,index):
        return deepcopy(self._list_islands[index])
    def get_posiib_horiz(self):
        return deepcopy(self._possible_connexion_horiz)
    def get_posiib_vert(self):
        return deepcopy(self._possible_connexion_vert)
    
    def get_possib_var_horiz(self):
        return deepcopy(self._possible_variable_horiz)
    def get_possib_var_vert(self):
        return deepcopy(self._possible_variable_vert)
    def get_variable_interdi(self):
        return deepcopy(self._dict_variables_interdit)
    
    def get_variable_possible(self):
        return deepcopy(self._dict_variables_possible)
    
    
    def __possible_v(self,list_c):
        res=list()
        for couple in list_c:
            nbc1=self._list_islands.index(couple[0])+1
            nbc2=self._list_islands.index(couple[1])+1
            var=formula(str(nbc1)+str(nbc2)+'1')
            res.append(var)
            var=formula(str(nbc1)+str(nbc2)+'2')
            res.append(var)
        return res
    
    def __variables_interdit(self):
        res=dict()
        for c in self._possible_variable_horiz:
            key=c.name[:-1]
            res[key]=list()
            
        for c in self._possible_variable_vert:
            key=c.name[:-1]
            res[key]=list()
            
        for horiz in self._possible_connexion_horiz:
            key1=self._list_islands.index(horiz[0])+1
            key2=self._list_islands.index(horiz[1])+1
            key=str(key1)+str(key2)
            l=list()
            for vert in self._possible_connexion_vert:
                if(horiz[0][1]<vert[0][1]<horiz[1][1]  and \
                ((vert[0][0]>horiz[0][0] and vert[1][0]<horiz[0][0]) or \
                (vert[1][0]>horiz[0][0] and vert[0][0]<horiz[0][0]) )):
                    key_v=str(self._list_islands.index(vert[0])+1)+str(self._list_islands.index(vert[1])+1)
                    l.append(formula(key_v+'1'))
                    print(f"add {key_v}1 for {key}")
                    l.append(formula(key_v+'2'))
                    print(f"add {key_v}2 for {key}")
                    res[key_v].append(formula(key+'1'))
                    res[key_v].append(formula(key+'2'))
                    
            res[key]=l
        return res
    
    def __variable_possible(self):
        res=dict()
        for i in range(len(self._list_islands)):
            l=list()
            for var in self._possible_variable_horiz:
                if(var.name[0]==str(i+1) or var.name[1] == str(i+1)):
                    l.append(var)
            for var in self._possible_variable_vert:
                if(var.name[0]==str(i+1) or var.name[1] == str(i+1)):
                    l.append(var)
            res[str(i+1)]=l
        return res
        
