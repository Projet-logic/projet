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
    


"""
this is an auxiliary class to define a specific operator
"""
class Infix:
    def __init__(self,function):
        self.function=function
    def __ror__(self,other):
        return Infix(lambda x , self=self, other=other:self.function(other,x))
    def __or__(self,other):
        return self.function(other)
    
    
"""
formula is a type using the optional parameters to make different instance(variable or formula)
if you make an instance using a string as parameter, the instance will be a variable using the parameter for its name
while if you make the instance using anouther 
"""
        
class formula :
        affect=Infix(lambda x,y : x.__affect(y))
        def __init__(self,f=None,connector=None):
            self._table=[]
            if isinstance(f,str):
                self._table.append(f)
                self.name=f
                self.is_variable=True
                self.is_neg=False
                self.not_initiated=False
            elif isinstance(f,formula):
                self._table.append(f)
                self.is_variable=False
                self._connector=connector
                self.not_initiated=False
            else:
                self.is_variable=False
                self.not_initiated=True
                self._connector=connector

        def add_subf(self,elem,index,connector=AND):
            if(self.is_variable and not self.not_initiated):
                self._table.append(elem)
                self._connector=connector
                self.is_variable=False
                
            elif (not self.not_initiated):
                self._table.insert(index,elem)
            else :
                self._table.append(elem)
                
                
        def remove_subf(self,elem):
            if(self.is_variable or self.not_initiated):
                raise ValueError(f"{self} is a variable and has no attribute table\n")
            res=self._table.pop(self._table.index(elem))
            return res

        def set_connector(self,connector=AND):
            if(self.is_variable):
                raise ValueError(f"{self} is a variable and has no attribute connector\n")
            self._connector=connector
            
        def get_subf(self,i):
            if(self.is_variable and self.not_initiated):
                raise ValueError(f"{self} is a variable and has no attribute table\n")
            return self._table[i]
        
        
        def get_connector(self):
            if(self.is_variable):
                raise ValueError(f"{self} is a variable and has no attribute connector\n")
            return self._connector
        
        def __affect(self,Value):
            if not self.is_variable:
                raise ValueError(f"{self} is not a variable")
            self.Value=Value
        
       
        def refr(self):
            if(not self.is_variable and not self.not_initiated):
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
            if(self.not_initiated):
                return f
            elif(f.not_initiated):
                return self
            res=formula(self,connector= OR)
            res.add_subf(f,1,connector=OR)
            res.refr()
            return res
        
        
        def __mul__(self,f):
            if(self.not_initiated):
                return f
            elif(f.not_initiated):
                return self
            res=formula(self,connector= AND)
            res.add_subf(f,1,connector= AND)
            res.refr()
            return res
        
        def __neg__(self):
            res=formula()
            res._table=self._table
            res.is_variable=self.is_variable
            res.not_initiated=self.not_initiated
            if(self.is_variable):
                res.name=self.name
                res.is_neg=not self.is_neg
            elif(not self.not_initiated):
                res._connector=self._connector
                for i in range(len(res._table)):
                    
                    res._table[i]=-res._table[i]
                    
                if(res._connector==AND):
                    res._connector=OR
                else:
                    res._connector=AND
            return res
        def dev(self):
            if(self.is_variable or self.not_initiated):
                pass
            elif(self.get_connector()==OR):
                #input(f"start or{self}")
                for f in self._table:
                    f.dev()
                for f in list(self._table):
                    if(not f.is_variable and f.get_connector()==AND):
                        self.remove_subf(f)
                        res=formula(formula(f.get_subf(0),connector=OR) + formula(self,connector=OR),connector=AND)
                        for fs in list(f._table)[1:]:
                            res=res*(fs+self)
                        self._table=list(res._table)
                        self._connector=res._connector
                        self.is_variable=res.is_variable
                        self.dev()
                        self.refr()
                        #input(f"end or{self}")
                        break
            elif(self.get_connector()==AND):
                #input(f"start and{self}")
                for f in self._table:
                    f.dev()
                    #print(f)
                self.refr()
                #input(f"end and{self}")
        
        def __str__(self):
            if(self.is_variable):
                if(hasattr(self, 'value')):
                    return f"{self.value}"
                elif(self.is_neg):
                    return f"-{self.name}"
                else :
                    return f"{self.name}"
            else:
                if(len(self._table)>=1):
                    res='('
                    for i in self._table:
                        if(i!=None):
                            res+=i.__str__()
                            res+=self._connector.value
                    res=res[:-1]
                    res+=')'
                    return res
                else:
                    return ""

            
