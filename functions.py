def todos_from_file(filename='todos.txt'):
    """Read a test file and return the list of Todo items"""
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
