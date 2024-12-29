def get_todos(filepath='todos.txt'):
    """ Open and read list of to-do items"""
    with open(filepath, "r") as local_file:
        local_items = local_file.readlines()
    return local_items


def write_todos(items_arg, filepath="todos.txt"):
    """ Open and write list of to-do items"""
    with open(filepath, "w") as file:
        file.writelines(items_arg)

