# ------ import module ------

import tkinter
import tkinter.font
import os
import sys
import subprocess


# ------ main code -------

# Window
win = tkinter.Tk()

# Title
win.title('CZCM')

# Resolution
win.geometry('1000x600+0+0')
win.resizable(False, False)

# Font
font = tkinter.font.Font(family="Arial", size=10)

# Title
title_text = tkinter.Label(win, text='Custom Zombie Code Maker Ver.0.3')
title_text.pack(side='top')

# Maker
maker = tkinter.Label(win, text='by Peaplant')
maker.place(x=900, y=30)

# Format
cz_format = '''{{
    "#comment": "{0} | CZCM Ver 0.3",
    "objclass": "ZombieType",
    "aliases": ["{1}"],
    "objdata": {{
        "TypeName": "tutorial",
        "ZombieClass": {2},
        "Properties": "RTID({3}@CurrentLevel)",
        "ResourceGroups": [
            {4}
        ],
        "AudioGroups": [
            {5}
        ],
        "AnimRigClass": {6},
        "PopAnim": {7},
        "HomeWorld": {8}
    }}
}},
{{
    "aliases": [
        "{3}"
    ],
    "objclass": "ZombiePropertySheet",
    "objdata": {{
        "Cost": {9},
        "EatDPS": {10},
        "Hitpoints": {11},
        "Speed": {12},
        "WavePointCost": {13},
        "Weight": {14},
        "ArtCenter": {{
            "x": {15},
            "y": {16}
        }},
        "AttackRect": {{
            "mHeight": {17},
            "mWidth": {18},
            "mX": {19},
            "mY": {20}
        }},
        "GroundTrackName": "{21}",
        "HitRect": {{
            "mHeight": {22},
            "mWidth": {23},
            "mX": {24},
            "mY": {25}
        }},
        "ShadowOffset": {{
            "x": {26},
            "y": {27},
            "z": {28}
        }},
        "CanSpawnPlantFood": {29}
    }}
}},'''

cz_format_cc = '''{{
    "#comment": "{0} | CZCM Ver 0.3",
    "objclass": "ZombieType",
    "aliases": ["{1}"],
    "objdata": {{
        "TypeName": "tutorial",
        "ZombieClass": {2},
        "Properties": "RTID({3}@CurrentLevel)",
        "ResourceGroups": [
            {4}
        ],
        "AudioGroups": [
            {5}
        ],
        "AnimRigClass": {6},
        "PopAnim": {7},
        "HomeWorld": {8},
        {30}
    }}
}},
{{
    "aliases": [
        "{3}"
    ],
    "objclass": "ZombiePropertySheet",
    "objdata": {{
        "Cost": {9},
        "EatDPS": {10},
        "Hitpoints": {11},
        "Speed": {12},
        "WavePointCost": {13},
        "Weight": {14},
        "ArtCenter": {{
            "x": {15},
            "y": {16}
        }},
        "AttackRect": {{
            "mHeight": {17},
            "mWidth": {18},
            "mX": {19},
            "mY": {20}
        }},
        "GroundTrackName": "{21}",
        "HitRect": {{
            "mHeight": {22},
            "mWidth": {23},
            "mX": {24},
            "mY": {25}
        }},
        "ShadowOffset": {{
            "x": {26},
            "y": {27},
            "z": {28}
        }},
        "CanSpawnPlantFood": {29},
        {31}
    }}
}},'''

# File path
if getattr(sys, "frozen", False):
    path = os.path.dirname(sys.executable)
else:
    path = sys.path[0]
file_name = fr'{path}/Result json/CZCM.json'


# ------ Zombie Types ------

"""
Copy-paste for fast label and entry box

_label = tkinter.Label(win, text = '')
_label.place(x = , y = )

_entry = tkinter.Entry(win, width = 20)
_entry.place(x = , y = )

"""

# Zombie Types Text
zombie_types_text = tkinter.Label(win, text='Zombie Types Code')
zombie_types_text.place(x=150, y=30)

# Comment
comment_label = tkinter.Label(win, text='Comments : ')
comment_label.place(x=50, y=50)

comment_entry = tkinter.Entry(win, width=20)
comment_entry.place(x=200, y=51)

# Aliase types
aliases_type_label = tkinter.Label(win, text='Zombie Type aliases : ')
aliases_type_label.place(x=50, y=70)

aliases_entry = tkinter.Entry(win, width=20)
aliases_entry.place(x=200, y=71)

# Zombie Class
zombie_class_label = tkinter.Label(win, text='Zombie Class: ')
zombie_class_label.place(x=50, y=95)

zc_drop = tkinter.StringVar()
with open(f"{path}\Options\Zombie Class options.txt", "r") as file:
    zombie_class_options = file.read().split(", ")

zc_drop.set(zombie_class_options[0])
drop = tkinter.OptionMenu(win, zc_drop, *zombie_class_options)
drop.place(x=198, y=90)

# Properties
props_label = tkinter.Label(win, text='Zombie Properties : ')
props_label.place(x=50, y=120)

props_entry = tkinter.Entry(win, width=20)
props_entry.place(x=200, y=121)

# Resource Groups
resource_label = tkinter.Label(win, text='Resource Groups : ')
resource_label.place(x=50, y=140)

resource_entry = tkinter.Entry(win, width=20)
resource_entry.place(x=200, y=141)

# Audio Groups
audio_label = tkinter.Label(win, text='Audio Groups : ')
audio_label.place(x=50, y=160)

audio_entry = tkinter.Entry(win, width=20)
audio_entry.place(x=200, y=161)

# Anim Rig Class
anim_label = tkinter.Label(win, text='Anim Rig Class : ')
anim_label.place(x=50, y=185)

anim_drop = tkinter.StringVar()
with open(f"{path}\Options\Anim Rig options.txt", "r") as file:
    anim_options = file.read().split(", ")

anim_drop.set(anim_options[0])
drop = tkinter.OptionMenu(win, anim_drop, *anim_options)
drop.place(x=198, y=180)

# Home World
home_label = tkinter.Label(win, text='Home World : ')
home_label.place(x=50, y=215)

home_drop = tkinter.StringVar()
with open(f"{path}\Options\Home World options.txt", "r") as file:
    home_options = file.read().split(", ")

home_drop.set(home_options[0])
drop = tkinter.OptionMenu(win, home_drop, *home_options)
drop.place(x=198, y=210)

# Extra Code
extype_label = tkinter.Label(win, text='Extra Code for Types : ')
extype_label.place(x=50, y=240)

extype_entry = tkinter.Entry(win, width=20)
extype_entry.place(x=200, y=241)

# Pop Anim
pop_label = tkinter.Label(win, text='Pop Anim : ')
pop_label.place(x=50, y=425)

pop_drop = tkinter.StringVar()
with open(f"{path}\Options\Pop Anim options.txt", "r") as file:
    pop_options = file.read().split(", ")

pop_drop.set(pop_options[0])
drop = tkinter.OptionMenu(win, pop_drop, *pop_options)
drop.place(x=198, y=420)


# ------ Zombie Properties ------

# Zombie Properties Text
zombie_props_text = tkinter.Label(win, text='Zombie Properties Code')
zombie_props_text.place(x=550, y=30)

# Cost
cost_label = tkinter.Label(win, text='Cost : ')
cost_label.place(x=450, y=50)

cost_entry = tkinter.Entry(win, width=20)
cost_entry.place(x=600, y=51)

# Eat Dps
eat_label = tkinter.Label(win, text='Eat DPS : ')
eat_label.place(x=450, y=70)

eat_entry = tkinter.Entry(win, width=20)
eat_entry.place(x=600, y=71)

# HP
hp_label = tkinter.Label(win, text='Hit Points : ')
hp_label.place(x=450, y=90)

hp_entry = tkinter.Entry(win, width=20)
hp_entry.place(x=600, y=91)

# Speed
speed_label = tkinter.Label(win, text='Speed : ')
speed_label.place(x=450, y=110)

speed_entry = tkinter.Entry(win, width=20)
speed_entry.place(x=600, y=111)

# Wave Point Cost
wave_label = tkinter.Label(win, text='Wave Point Cost : ')
wave_label.place(x=450, y=130)

wave_entry = tkinter.Entry(win, width=20)
wave_entry.place(x=600, y=131)

# Weight
weight_label = tkinter.Label(win, text='Weight : ')
weight_label.place(x=450, y=150)

weight_entry = tkinter.Entry(win, width=20)
weight_entry.place(x=600, y=151)

# Art Center
art_label = tkinter.Label(win, text='Art Center x, y : ')
art_label.place(x=450, y=170)

art_x_entry = tkinter.Entry(win, width=10)
art_x_entry.place(x=600, y=171)

art_y_entry = tkinter.Entry(win, width=10)
art_y_entry.place(x=670, y=171)

attack_label = tkinter.Label(win, text='x')
attack_label.place(x=632, y=191)

attack_label = tkinter.Label(win, text='y')
attack_label.place(x=702, y=191)

# Attack Rect
attack_label = tkinter.Label(win, text='Attack Rect : ')
attack_label.place(x=450, y=210)

attack_mh_entry = tkinter.Entry(win, width=5)
attack_mh_entry.place(x=600, y=211)

attack_mw_entry = tkinter.Entry(win, width=5)
attack_mw_entry.place(x=635, y=211)

attack_mx_entry = tkinter.Entry(win, width=5)
attack_mx_entry.place(x=670, y=211)

attack_my_entry = tkinter.Entry(win, width=5)
attack_my_entry.place(x=705, y=211)

attack_label = tkinter.Label(win, text='mHeight')
attack_label.place(x=600, y=231)

attack_label = tkinter.Label(win, text='mWidth')
attack_label.place(x=650, y=231)

attack_label = tkinter.Label(win, text='mX')
attack_label.place(x=696, y=231)

attack_label = tkinter.Label(win, text='mY')
attack_label.place(x=717, y=231)


# Ground Track Name 
ground_label = tkinter.Label(win, text='Ground Track Name : ')
ground_label.place(x=450, y=255)

ground_drop = tkinter.StringVar()
with open(f"{path}\Options\Ground Track options.txt", "r") as file:
    ground_options = file.read().split(", ")

ground_drop.set(ground_options[0])
drop = tkinter.OptionMenu(win, ground_drop, *ground_options)
drop.place(x=598, y=250)

# Hit Rect
hit_label = tkinter.Label(win, text='Hit Rect : ')
hit_label.place(x=450, y=280)

hit_mh_entry = tkinter.Entry(win, width=5)
hit_mh_entry.place(x=600, y=281)

hit_mw_entry = tkinter.Entry(win, width=5)
hit_mw_entry.place(x=635, y=281)

hit_mx_entry = tkinter.Entry(win, width=5)
hit_mx_entry.place(x=670, y=281)

hit_my_entry = tkinter.Entry(win, width=5)
hit_my_entry.place(x=705, y=281)

hit_label = tkinter.Label(win, text='mHeight')
hit_label.place(x=600, y=301)

hit_label = tkinter.Label(win, text='mWidth')
hit_label.place(x=650, y=301)

hit_label = tkinter.Label(win, text='mX')
hit_label.place(x=696, y=301)

hit_label = tkinter.Label(win, text='mY')
hit_label.place(x=717, y=301)

# Shadow Offset
shadow_label = tkinter.Label(win, text='Shadow Offset : ')
shadow_label.place(x=450, y=320)

shadow_x_entry = tkinter.Entry(win, width=7)
shadow_x_entry.place(x=600, y=321)

shadow_y_entry = tkinter.Entry(win, width=7)
shadow_y_entry.place(x=649, y=321)

shadow_z_entry = tkinter.Entry(win, width=6)
shadow_z_entry.place(x=698, y=321)

shadow_label = tkinter.Label(win, text='x')
shadow_label.place(x=623, y=341)

shadow_label = tkinter.Label(win, text='y')
shadow_label.place(x=666, y=341)

shadow_label = tkinter.Label(win, text='z')
shadow_label.place(x=709, y=341)


# Plant Food
pf_label = tkinter.Label(win, text='Can drop PF? :')
pf_label.place(x=450, y=360)

pf_drop = tkinter.StringVar()
pf_options = ["true", "false"]

pf_drop.set(pf_options[0])
drop = tkinter.OptionMenu(win, pf_drop, *pf_options)
drop.place(x=598, y=360)

# Extra Code
exprop_label = tkinter.Label(win, text='Extra Code')
exprop_label.place(x=450, y=390)

exprop_entry = tkinter.Entry(win, width=20)
exprop_entry.place(x=600, y=391)


# ------ Commands Class ------

# Class for commands
class commands:

    def __init__(self):

        # Var for checkbox
        self.cc_use_var = tkinter.IntVar()

        # Check box for use custom code
        self.cc_checkbox = tkinter.Checkbutton(
            win, text='Use custom code?', variable=self.cc_use_var)
        self.cc_checkbox.place(x=850, y=520)

        # For delete "Done!" message
        self.use_count = 0

    # Command for codes and port as json files

    def making_codes(self):

        # Delete "Done!" message
        if self.use_count == 1:
            self.done.destroy()

        # Button command for Custom Codes check
        self.cc_use = self.cc_use_var.get()

        # Collect all things
        self.comment = comment_entry.get()
        self.aliases = aliases_entry.get()
        self.zombie_class = zc_drop.get()
        self.props = props_entry.get()
        self.resource = resource_entry.get()
        self.audio = audio_entry.get()
        self.anim = anim_drop.get()
        self.pop = pop_drop.get()
        self.home = home_drop.get()
        self.cost = cost_entry.get()
        self.eat = eat_entry.get()
        self.hp = hp_entry.get()
        self.speed = speed_entry.get()
        self.wave = wave_entry.get()
        self.weight = weight_entry.get()
        self.art_x = art_x_entry.get()
        self.art_y = art_y_entry.get()
        self.attack_mh = attack_mh_entry.get()
        self.attack_mw = attack_mw_entry.get()
        self.attack_mx = attack_mx_entry.get()
        self.attack_my = attack_my_entry.get()
        self.ground = ground_drop.get()
        self.hit_mh = hit_mh_entry.get()
        self.hit_mw = hit_mw_entry.get()
        self.hit_mx = hit_mx_entry.get()
        self.hit_my = hit_my_entry.get()
        self.shadow_x = shadow_x_entry.get()
        self.shadow_y = shadow_y_entry.get()
        self.shadow_z = shadow_z_entry.get()
        self.pf = pf_drop.get()
        self.extype = extype_entry.get()
        self.exprop = exprop_entry.get()

        if self.ground == 'blank':
            self.ground = '""'
        else:
            pass

        # For custom commands
        if self.cc_use == 0:
            self.codeformat = cz_format
            self.codes = self.codeformat.format(self.comment, self.aliases, self.zombie_class, self.props, self.resource, self.audio, self.anim, self.pop, self.home, self.cost, self.eat, self.hp, self.speed, self.wave, self.weight,
                                                self.art_x, self.art_y, self.attack_mh, self.attack_mw, self.attack_mx, self.attack_my, self.ground, self.hit_mh, self.hit_mw, self.hit_mx, self.hit_my, self.shadow_x, self.shadow_y, self.shadow_z, self.pf)

        else:
            self.codeformat = cz_format_cc
            self.codes = self.codeformat.format(self.comment, self.aliases, self.zombie_class, self.props, self.resource, self.audio, self.anim, self.pop, self.home, self.cost, self.eat, self.hp, self.speed, self.wave, self.weight, self.art_x,
                                                self.art_y, self.attack_mh, self.attack_mw, self.attack_mx, self.attack_my, self.ground, self.hit_mh, self.hit_mw, self.hit_mx, self.hit_my, self.shadow_x, self.shadow_y, self.shadow_z, self.pf, self.extype, self.exprop)

        # Make json file & Write Code
        with open(file_name, "w") as out_file:
            out_file.write(str(self.codes))

        # Place "Done!" message
        self.done = tkinter.Label(win, text='Done!')
        self.done.place(x=850, y=555)

        self.use_count = 1


# Load commands as c
c = commands()


# ------ Make json file ------

# Button for make json file
make_file_btn = tkinter.Button(text="make json file", width=10)
make_file_btn.config(command=c.making_codes)
make_file_btn.place(x=900, y=550)


# ------ Open Window ------

win.mainloop()

# ------ Note for make exe files because I`m forgot every update ... dumb so ignore this------
# pyinstaller -w -F 