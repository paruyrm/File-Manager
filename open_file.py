from toolbox import os
from toolbox import mb
def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File not found!")