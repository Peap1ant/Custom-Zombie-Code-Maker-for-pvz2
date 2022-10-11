# ------ import module ------

import tkinter
import tkinter.font
import os
import sys

# ------ main code -------

# Window
win = tkinter.Tk()

# Title
win.title('Resource Generator')

# Resolution
win.geometry('400x300+240+100')
win.resizable(False, False)

# Font
font = tkinter.font.Font(family="Arial", size=10)

# Title
title_text = tkinter.Label(win, text='Resource Generator')
title_text.pack(side='top')

# Maker
maker = tkinter.Label(win, text='by Peaplant')
maker.place(x=300, y=30)

# Formats
resource_format_1 = '''{0}'''

resource_format_2 = '''{0},
            {1}'''

resource_format_3 = '''{0},
            {1},
            {2}'''

resource_format_4 = '''{0},
            {1},
            {2},
            {3}'''

resource_format_5 = '''{0},
            {1},
            {2},
            {3},
            {4}'''

# File path
if getattr(sys, "frozen", False):
    path = os.path.dirname(sys.executable)
else:
    path = sys.path[0]
# Fix path for .py
if "CZCM python\Sub-programs" in path:
    path = path.replace('\\Sub-programs', '').strip()
else:
    path = path.replace("\\Sub-programs", "").strip()
file_name = fr'{path}/Result json/Resource Generator.json'


# Dropbox options

with open(f"{path}\Options\Resource options.txt", "r") as file:
    resource_options = file.read().split(", ")

# ------ Resource Groups ------

# Resource Groups Text
resource_text = tkinter.Label(win, text='Resource Groups')
resource_text.place(x=150, y=30)

# 1
resource_1_text = tkinter.Label(win, text='1 : ')
resource_1_text.place(x=50, y=70)

resource_1_drop = tkinter.StringVar()

resource_1_drop.set(resource_options[0])
drop_1 = tkinter.OptionMenu(win, resource_1_drop, *resource_options)
drop_1.place(x=100, y=65)

# 2
resource_2_text = tkinter.Label(win, text='2 : ')
resource_2_text.place(x=50, y=100)

resource_2_drop = tkinter.StringVar()

resource_2_drop.set(resource_options[0])
drop_2 = tkinter.OptionMenu(win, resource_2_drop, *resource_options)
drop_2.place(x=100, y=95)

# 3
resource_3_text = tkinter.Label(win, text='3 : ')
resource_3_text.place(x=50, y=130)

resource_3_drop = tkinter.StringVar()

resource_3_drop.set(resource_options[0])
drop_3 = tkinter.OptionMenu(win, resource_3_drop, *resource_options)
drop_3.place(x=100, y=125)

# 4
resource_4_text = tkinter.Label(win, text='4 : ')
resource_4_text.place(x=50, y=160)

resource_4_drop = tkinter.StringVar()

resource_4_drop.set(resource_options[0])
drop_4 = tkinter.OptionMenu(win, resource_4_drop, *resource_options)
drop_4.place(x=100, y=155)

# 5
resource_5_text = tkinter.Label(win, text='5 : ')
resource_5_text.place(x=50, y=190)

resource_5_drop = tkinter.StringVar()

resource_5_drop.set(resource_options[0])
drop_5 = tkinter.OptionMenu(win, resource_5_drop, *resource_options)
drop_5.place(x=100, y=185)

# Resource Groups Lines
lines_text = tkinter.Label(win, text='Lines : ')
lines_text.place(x=50, y=220)

lines_drop = tkinter.IntVar()
lines_options = [1, 2, 3, 4, 5]

lines_drop.set(lines_options[0])
drop = tkinter.OptionMenu(win, lines_drop, *lines_options)
drop.place(x=100, y=215)

# ------ Commands Class ------

# Class for commands


class commands:

    def __init__(self):

        # For delete "Done!" message
        self.use_count = 0

    # Command for codes and port as txt files

    def making_codes(self):

        # Delete "Done!" message
        if self.use_count == 1:
            self.done.destroy()

        # Collect all things
        self.resource_1 = resource_1_drop.get()
        self.resource_2 = resource_2_drop.get()
        self.resource_3 = resource_3_drop.get()
        self.resource_4 = resource_4_drop.get()
        self.resource_5 = resource_5_drop.get()
        self.lines = lines_drop.get()

        # For multiple resources

        if self.lines == 1:
            self.code_format = resource_format_1

        elif self.lines == 2:
            self.code_format = resource_format_2

        elif self.lines == 3:
            self.code_format = resource_format_3

        elif self.lines == 4:
            self.code_format = resource_format_4

        else:
            self.code_format = resource_format_5

        self.codes = self.code_format.format(
            self.resource_1, self.resource_2, self.resource_3, self.resource_4, self.resource_5)

        # Make txt file & Write Code
        with open(file_name, "w") as out_file:
            out_file.write(str(self.codes))

        # Place "Done!" message
        self.done = tkinter.Label(win, text='Done!')
        self.done.place(x=250, y=255)

        self.use_count = 1


# Load commands as c
c = commands()


# ------ Make json file ------

# Button for make json file
make_file_btn = tkinter.Button(text="make json file", width=10)
make_file_btn.config(command=c.making_codes)
make_file_btn.place(x=300, y=250)

# ------ Open Window ------

win.mainloop()
