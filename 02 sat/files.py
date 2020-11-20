import os


def save_result(text):
    with open("results_sat.txt", "a+") as file:
        file.write(text)


def read_result():
    with open("results_sat.txt", "r") as file:
        content = file.readlines()

        return content


def reset_result():
    if os.path.exists("results_sat.txt"):
        os.remove("results_sat.txt")