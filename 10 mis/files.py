import os


def save_result(text):

    with open("results_mis.txt", "a+") as file:

        file.write(text)
    


def read_result():
    
    with open("results_mis.txt", "r") as file:

        content = file.readlines()
        return content


def reset_result():

    if os.path.exists("results_mis.txt"):

        os.remove("results_mis.txt")