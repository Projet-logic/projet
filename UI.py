# -*- coding: utf-8 -*-
"""
Created on Sat Mai 3 06:02:56 2023

@author: Tang Khac Vinh 

FILE DESCRIPTION:
       game module for Hashiwokakero
"""

"""
Ouvrir le fichier txt information et convertir les valeur de la taille de la grille et des iles
"""
with open('information.txt', 'r') as f:
    lines = f.readlines()
    num1 = lines[0]
    num1 = eval(num1[19:])
    
    num2 = lines[1]
    num2 = int(num2[-3:])

"""
La fonction est utilisée pour vérifier si un point donné se trouve à l'intérieur de l'un des cercles de la liste "l".
"""

def exist_in_list(l,i,j):
    for circle in l:
        if(circle[0]==i and circle[1]==j):
            return circle[2]
    else:
        return None


"""       
Imprimer l'instance de l'objet cercle sur la grille.
"""

def print_instance(list_of_c,n,m):
    print(" ",end="")
    for i in range(m):
        print("---",end="")
    print(" ",end="")
    print()
    for j in range(n):
        print('|',end="")
        index=-1
        j2=0
        while j2<(m*3)+1:
            index+=(j2%3 == 0)
            n=exist_in_list(list_of_c, j, index)
            if(n):
                print(f'({n})',end="")
                j2+=3
            else:
                print(' ',end="")
                j2+=1
        print('|')
    print(" ",end="")
    for i in range(m):
        print("---",end="")
    print(" ",end="")
    print()


grille_du_jeux=print_instance(num1,num2,num2)
   
    
    



    
  
   


            
