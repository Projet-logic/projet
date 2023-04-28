# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:16:23 2023

@author: Kian Feizabadi

FILE DESCRIPTION:
       formula type definition
"""
from connector_d import connector
from enum import Enum
AND=connector.AND
OR = connector.OR
NOT= connector.NOT
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
    
        
class formula :
        affect=Infix(lambda x,y : x.__affect(y))
        def __init__(self,f,connector=None):
            self._table=[f]
            if isinstance(f,str):
                self.name=f 
                self.is_variable=True
            elif isinstance(f,formula):
                self.is_variable=0
                self._connector=connector
                
        def add_subf(self,elem,index,connector=AND):
            if(self.is_variable):
                self._table.append(elem)
                self._connector=connector
                self.is_variable=False
                
            else:
                self._table.insert(index,elem)
                
        def remove_subf(self,elem):
            if(self.__class__==variable):
                raise ValueError(f"{self} is a variable and has no attribute table\n")
            res=self._table.pop(self._table.index(elem))
            return res

        def set_connector(self,connector=AND):
            if(self.is_variable):
                raise ValueError(f"{self} is a variable and has no attribute connector\n")
            self._connector=connector
            
        def get_subf(self,i):
            if(self.is_variable):
                raise ValueError(f"{self} is a variable and has no attribute table\n")
            return self._table[i]
        
        def get_len(self):
            return self._len
        
        def get_connector(self):
            if(self.is_variable):
                raise ValueError(f"{self} is a variable and has no attribute connector\n")
            return self._connector
        
        def __affect(self,Value):
            if not self.is_variable:
                raise ValueError(f"{self} is not a variable")
            self.Value=Value
        
       
        def refr(self):
            if(not self.is_variable):
                for f in list(self._table):
                    i=self._table.index(f)
                    if(not f.is_variable):
                        f.refr()
                        if f.get_connector()==self.get_connector():
                            self.remove_subf(f)
                            for sf in list(f._table):
                                self.add_subf(sf, i)
                        else:
                            pass
                    else:
                        pass
            else:
                pass
                    
                                
                            
                        
        def __add__(self,f):
          res=formula(self,connector= OR)
          res.add_subf(f,1,connector=OR)
          res.refr()
          return res
        
        
        def __mul__(self,f):
            res=formula(self,connector= AND)
            res.add_subf(f,1,connector= AND)
            res.refr()
            return res
        
        
        def dev(self):
            if(self.is_variable):
                pass
            elif()
        
        
        def __str__(self):
            if(self.is_variable):
                if(hasattr(self, 'value')):
                    return f"{self.value}"
                else :
                    return f"{self.name}"
            else:
                if(len(self._table)>1):
                    res='('
                    for i in self._table:
                        res+=i.__str__()
                        res+=self._connector.value
                    res=res[:-1]
                    res+=')'
                    return res
                elif(self._connector==NOT):
                    return f"(-{self._table[0].__str()})"



            
