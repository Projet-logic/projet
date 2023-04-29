


def save_dimacs(formule, filename):
    """Saves the clauses provided in the first argument to the file provided in the
    second argument in DIMACS format.
    Expected format of clauses: list of integers (DIMACS format compatible with a DPLL solveur, 
    i think pycosat or python-sat but i dont try to test yet)"""
    
    # Initialize the number of clauses and a set to store the variables in the formula
    nb_clauses = 0
    variables = set()

    # Count the number of clauses and add each variable to the set
    for clause in formule:
        nb_clauses += 1
        variables |= set(map(abs, clause))

    # Write the formula in DIMACS format to the file
    with open(filename, "w") as file:
        # Write the header
        file.write("c Fichier DIMACS\n")
        file.write(f"p cnf {len(variables)} {nb_clauses}\n")

        # Write each clause
        for clause in formule:
            file.write(" ".join(str(v) for v in clause) + " 0\n")
