from toolbox import easygui
# open a file box window 
# when we want to select a file

def open_window():
    read=easygui.fileopenbox()
    return read


open_window()