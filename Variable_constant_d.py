# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:59:31 2023

@author: Kian Feizabadi

FILE DESCRIPTION:
       variables and Constant type definition
"""

from enum import Enum

class constant(Enum):
    T=True
    F=False
    
    
class Infix:
    def __init__(self,function):
        self.function=function
    def __ror__(self,other):
        return Infix(lambda x , self=self, other=other:self.function(other,x))
    def __or__(self,other):
        return self.function(other)
    
    
class variable:
    def __init__(self,name):
        if(name.__class__!=str):
            raise ValueError("the name of variable should be string");
        self.name=name
    def __affect(self,Value):
        self.Value=Value
    affect=Infix(lambda x,y : x.__affect(y))
    def __str__(self):
        if(hasattr(self,'Value')):
            return self.Value.name
        else:
            return self.name
    
    
