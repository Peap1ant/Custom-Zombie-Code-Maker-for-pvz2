# ------ import module ------

import tkinter
import tkinter.font
import os
import sys

# ------ main code -------

# Window
win = tkinter.Tk()

# Title
win.title('Audio Generator')

# Resolution
win.geometry('400x300+0+0')
win.resizable(False, False)

# Font
font = tkinter.font.Font(family="Arial", size=10)

# Title
title_text = tkinter.Label(win, text='Audio Generator')
title_text.pack(side='top')

# Maker
maker = tkinter.Label(win, text='by Peaplant')
maker.place(x=300, y=30)

# Formats
audio_format_1 = '''{0}'''

audio_format_2 = '''{0},
            {1}'''

audio_format_3 = '''{0},
            {1},
            {2}'''

audio_format_4 = '''{0},
            {1},
            {2},
            {3}'''

audio_format_5 = '''{0},
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
if "\\Sub-programs" in path:
    path = path.replace('\\Sub-programs', '').strip()
file_name = fr'{path}/Result json/Audio Generator.json'

# Dropbox options

with open(f"{path}/Options\Audio options.txt", "r") as file:
    audio_options = file.read().split(", ")

# ------ Audio Groups ------

# Audio Groups Text
audio_text = tkinter.Label(win, text='Audio Groups')
audio_text.place(x=150, y=30)

# 1
audio_1_text = tkinter.Label(win, text='1 : ')
audio_1_text.place(x=50, y=70)

audio_1_drop = tkinter.StringVar()

audio_1_drop.set(audio_options[0])
drop_1 = tkinter.OptionMenu(win, audio_1_drop, *audio_options)
drop_1.place(x=100, y=65)

# 2
audio_2_text = tkinter.Label(win, text='2 : ')
audio_2_text.place(x=50, y=100)

audio_2_drop = tkinter.StringVar()

audio_2_drop.set(audio_options[0])
drop_2 = tkinter.OptionMenu(win, audio_2_drop, *audio_options)
drop_2.place(x=100, y=95)

# 3
audio_3_text = tkinter.Label(win, text='3 : ')
audio_3_text.place(x=50, y=130)

audio_3_drop = tkinter.StringVar()

audio_3_drop.set(audio_options[0])
drop_3 = tkinter.OptionMenu(win, audio_3_drop, *audio_options)
drop_3.place(x=100, y=125)

# 4
audio_4_text = tkinter.Label(win, text='4 : ')
audio_4_text.place(x=50, y=160)

audio_4_drop = tkinter.StringVar()

audio_4_drop.set(audio_options[0])
drop_4 = tkinter.OptionMenu(win, audio_4_drop, *audio_options)
drop_4.place(x=100, y=155)

# 5
audio_5_text = tkinter.Label(win, text='5 : ')
audio_5_text.place(x=50, y=190)

audio_5_drop = tkinter.StringVar()

audio_5_drop.set(audio_options[0])
drop_5 = tkinter.OptionMenu(win, audio_5_drop, *audio_options)
drop_5.place(x=100, y=185)

# Audio Groups Lines
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

    # Command for codes and port as json files

    def making_codes(self):

        # Delete "Done!" message
        if self.use_count == 1:
            self.done.destroy()

        # Collect all things
        self.audio_1 = audio_1_drop.get()
        self.audio_2 = audio_2_drop.get()
        self.audio_3 = audio_3_drop.get()
        self.audio_4 = audio_4_drop.get()
        self.audio_5 = audio_5_drop.get()
        self.lines = lines_drop.get()

        # For multiple audios

        if self.lines == 1:
            self.code_format = audio_format_1

        elif self.lines == 2:
            self.code_format = audio_format_2

        elif self.lines == 3:
            self.code_format = audio_format_3

        elif self.lines == 4:
            self.code_format = audio_format_4

        else:
            self.code_format = audio_format_5

        self.codes = self.code_format.format(
            self.audio_1, self.audio_2, self.audio_3, self.audio_4, self.audio_5)

        # Make json file & Write Code
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
