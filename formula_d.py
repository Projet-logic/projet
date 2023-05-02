# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:16:23 2023

@author: Kian Feizabadi & Tang Khac Vinh

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
This is an auxiliary class to define a specific operator.

- This code defines a class called "Infix" which allows you to define custom infix operators in Python.

- The "init" method initializes an instance of the class with a given function.

- The "ror" method overloads the bitwise OR operator "|". It takes in another object "other" 
and returns a new instance of the "Infix" class with a lambda function that calls the original function with "other" 
as the second argument and the result of the bitwise OR operation between the original object and "other" as the first argument.

- The "or" method overloads the OR operator "or". It takes in another object "other" and returns the result of calling the original function with "other" as the argument.
"""
class Infix:
    def __init__(self,function):
        self.function=function
    def __ror__(self,other):
        return Infix(lambda x , self=self, other=other:self.function(other,x))
    def __or__(self,other):
        return self.function(other)
    
    
"""
Formula is a type using the optional parameters to make different instance(variable or formula)
if you make an instance using a string as parameter, the instance will be a variable using the parameter for its name
while if you make the instance using another.

- The constructor of the class formula has two parameters, f and connector. If f is a string, it is treated as a variable and added to the current object's table. 
If f is a formula object, the current object will contain the object f. If f is not a string or formula object, 
the current object has no table, is assigned a connector, and is not initialized.

- The formula's add_subf method is used to add a new element to the table of the current formula. If the current formula is a variable, 
the new element will be added after the variable. If the current formula is not a variable, 
the new element will be inserted at the index position in the table.

- The formula's remove_subf method is used to remove an element from the current formula's table. 
If the current formula is variable or uninitialized, it will raise an exception. If the element to be deleted is not in the table, this method will return None, 
otherwise it will return the deleted element.

- set_connector(self,connector=AND): This method is used to set the value of the _connector property of the formula object. 
If the object is a variable (with the is_variable=True property), the method will throw an error. The default value of the connector is AND.

- get_subf(self,i): This method returns the i-th element in the table containing the elements of the formula object. 
If the object is a variable and has not initialized the table (not_initiated=True), the method will throw an error.

- get_connector(self): This method returns the value of the _connector property of the formula object. 
If the object is a variable, the method will throw an error.

- __affect(self,Value): This method is used to assign a value to an instance variable. 
This method can only be called when the object is a variable (is_variable=True), otherwise an error will be thrown.

- refr(self): This method is used to update the formula object. If the object is a variable or has not initialized the table (not_initiated=True), 
the method will not perform any operations. Otherwise, the method will iterate over each element of the table, and if the element is not a variable, the method will update the element again by grouping the child elements if they have the same logical connection.

- __add__(self,f): This method performs the OR operation between object self and object f. 
If either object is an uninitialized object (not_initiated=True), the method will return the other. 
If both objects are initialized, the method will return a new formula object with the elements of self and f as its two children. 
The logical connection between these two child elements will be set to OR.

- Function __mul__(self, f): This function is called when performing multiplication between two objects self and f. If self or f is uninitialized, 
it returns the initialized object. Otherwise, it creates a new object whose connector is AND, adds f to the table containing the modifiers, and refreshes the returned object.

- __neg__(self): This function is called when performing the negation of an object self. 
It returns a new object created from self, with the updated name, is_neg, _table, is_variable and not_initiated properties respectively. 
If self is a logical variable, is_neg will be converted between True and False. If self is a logical expression (formula), 
it will negate the entire expression and change the connector to OR if the connector was previously AND, and vice versa.

- dev(self) function is a recursive method that performs the Shannon expansion algorithm for the formula object. 
It divides the formula into a sum of products (SOP) representation by recursively applying the distributive law. 
If the formula object has an OR connector, it applies the distributive law to convert it into a product of sums (POS) representation. 
If it has an AND connector, it calls the refr() method and recursively applies the dev() method to its subformulas.

__str__(self) function is used to convert the formula object to a string representation. If the formula is a variable, it returns its name or value, 
depending on whether the variable has been assigned a value. If it is a negation, it returns the negation symbol followed by the variable name. 
If it is a compound formula, it iterates through its subformulas and builds a string by concatenating the string representation of each subformula and the connector symbol.
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

            
