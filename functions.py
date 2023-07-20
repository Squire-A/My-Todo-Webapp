FILEPATH = "todos.txt"

def open_todos(filepath=FILEPATH):
    """
    Reads a text file and returns the todos list.
    """
    with open(filepath, 'r') as file:
        todos_list = file.readlines()
    return todos_list


def write_todos(todos_list, filepath=FILEPATH):
    """
    Write the to-do to the list in the text file.
    :param todos_list:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_list)


if __name__ == "__main__":
    print("Hello")
