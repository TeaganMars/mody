import glob
import tkinter as tk
from tkinter import filedialog


def get_first_number(taco):
    """Returns the first numbers of the line as an integer"""
    result = ''
    for char in taco:
        if char.isdigit():
            # The character is a number
            result += char
        else:
            # The character is not a number
            break
    if result == '':
        return 0
    x = int(result)
    return x


def list_out_lines(file):
    line_list = []
    with open(file, 'r+') as g:
        lines = g.read().splitlines()
        for line in lines:
            if get_first_number(line) < 1347:
                line_list.append(line)
            else:
                break
    return line_list
"""Takes the lines that match the parameter and folds them into a list.
In this case it was all lines that started with a letter or a year earlier than 1347 AD"""


def end_of_history():
    saved_list = list_out_lines(Eu4)
    f = open(Eu4, 'w')
    f.writelines(["%s\n" % item for item in saved_list])
    f.close()
"""Overwrites file with the list"""


def black_plague():
    fk = open(Eu4, 'a+')
    fk.writelines(['\n',
                       '1444.1.1 = {    owner = XXX\n',
                       '                controller = XXX\n',
                       '                citysize = 0\n',
                       '                base_tax = 1\n',
                       '                base_production = 1\n',
                       '                base_manpower = 1} # Final Death is complete, this makes the provence empty\n'])
    fk.close()

root = tk.Tk()
root.withdraw()
selected_list = filedialog.askopenfilename()
"""asks for list of prov ID's"""


with open(selected_list, 'r+') as g:
    """opens the list and turns it into another list"""
    list_files = g.read().splitlines()


for line in list_files:
    """Takes that list and commits genocide"""
    Eu4 = ''.join(glob.glob(line + " *"))
    """makes each number a string and adds a space to ensure that 1, 10, 100 and 1000 are not read the same"""
    if Eu4 is '':
        """cause sometimes they leave a space between number and -, and sometimes they don't"""
        Eu4 = ''.join(glob.glob(line + "-*"))
        end_of_history()
        black_plague()
        print(Eu4)
    else:
        end_of_history()
        black_plague()
        print(Eu4)
