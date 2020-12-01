import os


fileDir = os.path.dirname(os.path.realpath('__file__'))

def save_result(file_name, text):
    """Permite guardar resultados en un archivo txt.

    Parameters
    ----------
    file_name : Str
        Nombre del archivo
    
    text : Str
        Resultados a guardar
    """

    filename = os.path.join(fileDir, 'tools/results/{}.txt'.format(file_name))

    with open(filename, "a+") as file:
        file.write(text)


def read_result(file_name):
    """Permite leer resultados de un archivo txt.

    Parameters
    ----------
    file_name : Str
        Nombre del archivo
    
    Returns
    ----------
    content : Str
        Contenido del archivo
    """

    filename = os.path.join(fileDir, 'tools/results/{}.txt'.format(file_name))

    with open(filename, "r") as file:
        content = file.readlines()

        return content


def reset_result(file_name):
    """Permite resetear un archivo txt.

    Parameters
    ----------
    file_name : Str
        Nombre del archivo
    """

    filename = os.path.join(fileDir, 'tools/results/{}.txt'.format(file_name))

    if os.path.exists(filename):
        os.remove(filename)
    
    with open(filename, "w"): pass