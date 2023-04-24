# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:16:23 2023

@author: Kian Feizabadi

FILE DESCRIPTION:
       formula type definition
"""
from connector_d import connector

class formula :
        def __init__(self):
            self._left=None
            self._right=None
            self._connector=connector.AND 
        def _set_left(self,left):
            self._lef=left
        def _set_right(self,right):
            self._right=right   
        def _set_connector(self,connector=connector.AND):
            self._connector=connector
        def __add__(self,f):
            res=formula()
            res._set_left(self)
            res._set_right(f)
            res._set_connector(connector.OR)
            return res
        def __mul__(self,f):
            res=formula()
            res._set_left(self)
            res._set_right(f)
            res._set_connector(connector.AND)
            return res
        def __str__(self):
            if(self._left==None):
                if(self._right==None):
                    return ""
                else:
                    return f"({self._right.__str__()})"
            elif(self._right==None):
                return f"({self._left.__str__()})"
            
            return f"({self._left.__str__()}) {self._connector.name} ({self._right.__str__()})\n"
        
