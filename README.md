# Game overview
- Hashiwokakero (or Bridges) is a puzzle and logic game of Japanese origin.
- In this game you are given a grid of squares with a number of columns and rows containing the number of decks. Your objective is to connect all the islands by bridges to form an indivisible network.
- Each island in the grid has a number of bridges attached to it, and bridges can only be attached in horizontal or vertical directions. No bridge is allowed to cross and a line cannot cross another bridge.
- The Hashiwokakero game requires players to think logically and develop problem-solving skills. It can be a fun and challenging game for puzzle lovers.

# Variable and constant definition :
- the constants are T for True and F for False and they should be imported like  "from Vaiable_constant_d.constant import T,F"
    
- Variable is an object which has a attribute called name and in the case of assignment it will have anouther attrribute called value
- Class Variable has a mthode called 'affect' which should be imported with "from Vaiable_constant_d.Variable import affect" or affectet to a local          - Variables with 'from Variable_constant_d import Variable      |    affect = Variable.affect'  and the usage is like  ' A affect T '
- Connectors definition:
    - as we are attempting to create the clauses so we are going to need only 'AND' and 'OR', you can import these logical connectors by 
    - "from connector_d.connector import AND,OR"
- Formula definition:
    - a formula is a recursive type which is defined by its left subformula, right subformula, and its connector
    - its subformulas could be either a Variable,constant Value or a formula
