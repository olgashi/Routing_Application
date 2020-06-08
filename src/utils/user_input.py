def user_input():
    command = input("""
    id - look up details for a specific package;
    time - display package status of all packages at a specific time (only accepts am/pm format, for example 8:25 am);
    distance - display total distance for all trucks;
    clear - clear screen;
    exit - to exit;\n >>>\t""")

    return command
