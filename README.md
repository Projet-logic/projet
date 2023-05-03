# Game overview
- Hashiwokakero (or Bridges) is a puzzle and logic game of Japanese origin.
- In this game you are given a grid of squares with a number of columns and rows containing the number of decks. Your objective is to connect all the islands by bridges to form an indivisible network.
- Each island in the grid has a number of bridges attached to it, and bridges can only be attached in horizontal or vertical directions. No bridge is allowed to cross and a line cannot cross another bridge.
- The Hashiwokakero game requires players to think logically and develop problem-solving skills. It can be a fun and challenging game for puzzle lovers.

![image](https://user-images.githubusercontent.com/78409997/234302292-ab4b6b0c-988f-47c8-80dc-1861a78916af.png)


# Variable and constant definition :
- Variable constant definition:
    - the constants are T for True and F for False and they should be imported like  "from Vaiable_constant_d.constant import T,F"
    
    - Variable is an object which has a attribute called name and in the case of assignment it will have anouther attrribute called value
    - Class Variable has a methode called "affect" which should be imported with "from Vaiable_constant_d.Variable import affect" or affectet to a local          - Variables with 'from Variable_constant_d import Variable      |    affect = Variable.affect'  and the usage is like  " A affect T "
- Connectors definition:
    - as we are attempting to create the clauses so we are going to need only 'AND' and 'OR', you can import these logical connectors by 
    - "from connector_d.connector import AND,OR"
- Formula definition:
    - a formula is a recursive type which is defined by its left subformula, right subformula, and its connector
    - its subformulas could be either a Variable,constant Value or a formula
# exécuter les étapes:
1.ctrl f5 pour lancer le test
2.entrez la largeur de la grille entre 1 et 8
3.entrez la longueur de la grille entre 1 et 8
4.Détermine si un nouveau cercle doit être ajouté(y<=>oui,n<=>non)
5.si oui,insérer le numéro de ligne,
si non,Il va vérifier s'il existe une solution, et si oui, donner la formule
6.insérer le numéro de colonne
7.insérer un nombre limité de ponts
8.aficher le jeu et retour à 4ème étapes
