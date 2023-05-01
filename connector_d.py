# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:32:17 2023

@author: Kian Feizabadi

FILE DESCRIPTION:
       logical connectors type definition
"""
from enum import Enum
class connector(Enum):
        AND = '*'
        OR  = '+'
        NOT = '-'
        
