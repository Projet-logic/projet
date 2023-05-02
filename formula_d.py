# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:16:23 2023

@author: Kian Feizabadi & Tang Khac Vinh & ZHANG Yuchen

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
Il s'agit d'une classe auxiliaire pour définir un opérateur spécifique.

- Ce code définit une classe appelée "Infix" qui vous permet de définir des opérateurs infix personnalisés en Python.

- La méthode "init" initialise une instance de la classe avec une fonction donnée.

- La méthode "ror" surcharge l'opérateur OR binaire "|". Elle prend en entrée un autre objet "other" et renvoie une nouvelle instance de la classe "Infix" avec une fonction lambda qui appelle la fonction originale avec "other" en tant que deuxième argument et le résultat de l'opération OR binaire entre l'objet original et "other" en tant que premier argument.

- La méthode "or" surcharge l'opérateur OR "or". Elle prend en entrée un autre objet "other" et renvoie le résultat de l'appel de la fonction originale avec "other" en tant qu'argument.
"""
class Infix:
    def __init__(self,function):
        self.function=function
    def __ror__(self,other):
        return Infix(lambda x , self=self, other=other:self.function(other,x))
    def __or__(self,other):
        return self.function(other)
    
    
"""
La Formule est un type qui utilise des paramètres optionnels pour créer différentes instances (variables ou formules). 
Si vous créez une instance en utilisant une chaîne de caractères comme paramètre, 
l'instance sera une variable portant le nom spécifié dans le paramètre. En revanche, si vous créez l'instance en utilisant un autre type de paramètre.

- Le constructeur de la classe Formule a deux paramètres, f et connecteur. Si f est une chaîne de caractères, 
elle est traitée comme une variable et ajoutée à la table de l'objet courant. Si f est un objet formule, l'objet courant contiendra l'objet f. 
Si f n'est ni une chaîne de caractères ni un objet formule, l'objet courant n'a pas de table, se voit attribuer un connecteur et n'est pas initialisé.

- La formule add_subf est utilisée pour ajouter un nouvel élément à la table de la formule courante. 
Si la formule courante est une variable, le nouvel élément sera ajouté après la variable.
Si la formule courante n'est pas une variable, le nouvel élément sera inséré à la position d'indice dans la table.

- La formule remove_subf est utilisée pour supprimer un élément de la table de la formule courante. 
Si la formule courante est une variable ou non initialisée, elle lèvera une exception. 
Si l'élément à supprimer n'est pas dans la table, cette méthode renverra None, sinon elle renverra l'élément supprimé.

- set_connector(self, connector=AND): Cette méthode est utilisée pour définir la valeur de la propriété _connector de l'objet formule. 
Si l'objet est une variable (avec la propriété is_variable=True), la méthode lèvera une erreur. La valeur par défaut du connecteur est AND.

- get_subf(self, i): Cette méthode renvoie le i-ème élément de la table contenant les éléments de l'objet formule.
Si l'objet est une variable et que la table n'a pas été initialisée (not_initiated=True), la méthode lèvera une erreur.

- get_connector(self): Cette méthode renvoie la valeur de la propriété _connector de l'objet formule. Si l'objet est une variable, la méthode lèvera une erreur.

- __affect(self, Value): Cette méthode est utilisée pour affecter une valeur à une variable d'instance. 
Cette méthode ne peut être appelée que lorsque l'objet est une variable (is_variable=True), sinon une erreur sera levée.

- refr(self): Cette méthode est utilisée pour mettre à jour l'objet formule. Si l'objet est une variable ou que la table n'a pas été initialisée (not_initiated=True), 
la méthode ne effectuera aucune opération. Sinon, la méthode itérera sur chaque élément de la table, et si l'élément n'est pas une variable, 
la méthode mettra à jour l'élément en regroupant à nouveau les éléments enfants s'ils ont la même connexion logique.

- __add__(self,f):Cette méthode effectue l'opération OR entre l'objet self et l'objet f. Si l'un des objets est un objet non initialisé (not_initiated=True), 
la méthode renverra l'autre. Si les deux objets sont initialisés, la méthode renverra un nouvel objet formule avec les éléments de self et f comme ses deux enfants. 
La connexion logique entre ces deux éléments enfants sera définie sur OR.

- Function __mul__(self, f):Cette fonction est appelée lors de la multiplication entre deux objets self et f. Si self ou f n'est pas initialisé, 
il renvoie l'objet initialisé. Sinon, il crée un nouvel objet dont le connecteur est AND, ajoute f à la table contenant les modificateurs et rafraîchit l'objet renvoyé.

- __neg__(self):Cette fonction est appelée lors de la négation d'un objet self. Elle renvoie un nouvel objet créé à partir de self, 
avec les propriétés de nom, is_neg, _table, is_variable et not_initiated mises à jour respectivement. Si self est une variable logique, is_neg sera converti entre True et False. 
Si self est une expression logique (formule), elle niera toute l'expression et changera le connecteur en OR si le connecteur était précédemment AND, et vice versa.

- dev(self) est une méthode récursive qui effectue l'algorithme d'expansion de Shannon pour l'objet formule. 
Elle divise la formule en une représentation somme de produits (SOP) en appliquant récursivement la loi distributive. Si l'objet formule a un connecteur OR, 
elle applique la loi distributive pour le convertir en une représentation produit de sommes (POS). Si elle a un connecteur AND, 
elle appelle la méthode refr() et applique récursivement la méthode dev() à ses sous-formules.

__str__(self) est utilisée pour convertir l'objet de formule en une représentation de chaîne de caractères. 
Si la formule est une variable, elle renvoie son nom ou sa valeur, selon que la variable ait été affectée ou non. 
Si c'est une négation, elle renvoie le symbole de négation suivi du nom de la variable. 
Si c'est une formule composée, elle itère à travers ses sous-formules et construit une chaîne en concaténant la représentation de chaîne de chaque sous-formule et le symbole de connexion.
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

            
