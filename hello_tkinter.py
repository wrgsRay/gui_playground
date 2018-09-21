"""
@author: wrgsray
python 3.6
"""
from tkinter import *
from tkinter.ttk import *


def main():
    root = Tk()
    label = Label(root, text='Hello World')
    label.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
