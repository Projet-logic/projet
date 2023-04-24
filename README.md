# projet
python source codes

Variable and constant definition :
    the constants are T for True and F for False and they should be imported like ' from Vaiable_constant_d.constant import T,F'
    
    a variable is an object which has a attribute called name and in the case of assignment it will have anouther attrribute called value
    the class Variable has a mthode called 'affect' which should be imported with 'from Vaiable_constant_d.Variable import affect' or affectet to a local           variable with 'from Variable_constant_d import Variable      |    affect = Variable.affect'  and the usage is like  ' A affect T '
Connectors definition:
    as we are attempting to create the clauses so we are going to need only 'AND' and 'OR', you can import these logical connectors by 
    "from connector_d.connector import AND,OR"
Formula definition:
    a formula is a recursive type which is defined by its left subformula, right subformula, and its connector
    its subformulas could be either a Variable,constant Value or a formula
