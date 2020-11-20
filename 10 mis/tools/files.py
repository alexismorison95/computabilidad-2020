import os


fileDir = os.path.dirname(os.path.realpath('__file__'))

def save_result(file_name, text):

    filename = os.path.join(fileDir, 'tools/results/{}.txt'.format(file_name))

    with open(filename, "a+") as file:
        file.write(text)


def read_result(file_name):

    filename = os.path.join(fileDir, 'tools/results/{}.txt'.format(file_name))

    with open(filename, "r") as file:
        content = file.readlines()

        return content


def reset_result(file_name):

    filename = os.path.join(fileDir, 'tools/results/{}.txt'.format(file_name))

    if os.path.exists(filename):
        os.remove(filename)
    
    with open(filename, "w"): pass