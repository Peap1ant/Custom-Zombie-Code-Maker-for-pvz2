# ------ import module ------

import tkinter
import tkinter.font
import os
import sys


# ------ main code -------

# Window
win = tkinter.Tk()

# Title
win.title('ECG')

# Resolution
win.geometry('1000x700+0+0')
win.resizable(False, False)

# Font
font = tkinter.font.Font(family="Arial", size=10)

# Title
title_text = tkinter.Label(win, text='Extra Code Generator')
title_text.pack(side='top')

# Maker
maker = tkinter.Label(win, text='by Peaplant')
maker.place(x=900, y=30)

# File path
if getattr(sys, "frozen", False):
    path = os.path.dirname(sys.executable)
else:
    path = sys.path[0]

# Fix path for .py
if "\\Sub-programs" in path:
    path = path.replace('\\Sub-programs', '').strip()


# ------ Buttons ------

# Button for load options
load_btn = tkinter.Button(text="load", width=10)
load_btn.place(x=82, y=130)

# Button for destroy options
reset_btn = tkinter.Button(text="destroy all", width=10)
reset_btn.place(x=82, y=155)

# Button for make json file
make_file_btn = tkinter.Button(text="make json file", width=10)


# ------ Select options dropbox & code ------

# Dropbox format
'''
with open(f"{path}\Options\ECG\", "r") as file:
        _options = file.read().split(", ")

_label = tkinter.Label(win, text = '')

 = tkinter.StringVar()

.set(_options[0])
_drop = tkinter.OptionMenu(win, , *_options)
'''

with open(f"{path}\Options\ECG\ECG options.txt", "r") as file:
        select_options = file.read().split(", ")

# Option dropbox
option_text = tkinter.Label(win, text = 'Extra Code Type')
option_text.place(x=80, y=80)

option = tkinter.StringVar()

option.set(select_options[0])
drop = tkinter.OptionMenu(win, option, *select_options)
drop.place(x=80, y=100)

tf_options = ["true", "false"]
tfn_options = ["true", "false", "none"]

# ------ Zombie Types Extra ------

# Placeable
type_place_label = tkinter.Label(win, text = 'Placeable?')

type_place = tkinter.StringVar()

type_place.set(tfn_options[0])
type_place_drop = tkinter.OptionMenu(win, type_place, *tfn_options)

# Is Basic Zombie?
type_basic_label = tkinter.Label(win, text = 'Is Basic Zombie?')

type_basic = tkinter.StringVar()

type_basic.set(tfn_options[0])
type_basic_drop = tkinter.OptionMenu(win, type_basic, *tfn_options)

# Almanac Backdrop Name
with open(f"{path}\Options\ECG\Type\Almanac Backdrop Name options.txt", "r") as file:
        type_al_options = file.read().split(", ")

type_al_label = tkinter.Label(win, text = 'Almanac Backdrop Name :')

type_al = tkinter.StringVar()

type_al.set(type_al_options[0])
type_al_drop = tkinter.OptionMenu(win, type_al, *type_al_options)

# Hasty On Start
type_hasty_label = tkinter.Label(win, text = 'Hasty On Start?')

type_hasty = tkinter.StringVar()

type_hasty.set(tfn_options[0])
type_hasty_drop = tkinter.OptionMenu(win, type_hasty, *tfn_options)

# Flag Type
with open(f"{path}\Options\ECG\Type\Flag Type options.txt", "r") as file:
        type_flag_options = file.read().split(", ")

type_flag_label = tkinter.Label(win, text = 'Flag Type : ')

type_flag = tkinter.StringVar()

type_flag.set(type_flag_options[0])
type_flag_drop = tkinter.OptionMenu(win, type_flag, *type_flag_options)


# ------ Zombie Properties Extra ------

# Can Be Plant Tossed Strong
prop_tossed_strong_label = tkinter.Label(win, text='Can be plant tossed strong : ')

prop_tossed_strong = tkinter.StringVar()

prop_tossed_strong.set(tfn_options[0])
prop_tossed_strong_drop = tkinter.OptionMenu(win, prop_tossed_strong, *tfn_options)

# Can Be Plant Tossed Weak
prop_tossed_weak_label = tkinter.Label(win, text='Can be plant tossed weak : ')

prop_tossed_weak = tkinter.StringVar()

prop_tossed_weak.set(tfn_options[0])
prop_tossed_weak_drop = tkinter.OptionMenu(win, prop_tossed_weak, *tfn_options)

# Is Spawned Flying
prop_fly_label = tkinter.Label(win, text='Is Spawned Flying : ')

prop_fly = tkinter.StringVar()

prop_fly.set(tfn_options[0])
prop_fly_drop = tkinter.OptionMenu(win, prop_fly, *tfn_options)

# Can Surrender
prop_surren_label = tkinter.Label(win, text='Can Surrender : ')

prop_surren = tkinter.StringVar()

prop_surren.set(tfn_options[0])
prop_surren_drop = tkinter.OptionMenu(win, prop_surren, *tfn_options)

# Can Trigger Zombie Win
prop_win_label = tkinter.Label(win, text='Can Trigger Zombie Win : ')

prop_win = tkinter.StringVar()

prop_win.set(tfn_options[0])
prop_win_drop = tkinter.OptionMenu(win, prop_win, *tfn_options)

# Explodes When Mowed
prop_explo_label = tkinter.Label(win, text='Explodes When Mowed : ')

prop_explo = tkinter.StringVar()

prop_explo.set(tfn_options[0])
prop_explo_drop = tkinter.OptionMenu(win, prop_explo, *tfn_options)

# Shrunken Scale
prop_shrunken_label = tkinter.Label(win, text = 'Shrunken Scale : \n(none for blank)  ')

prop_shrunken_entry = tkinter.Entry(win, width=20)

# Fire Damage Multiplier
prop_fire_label = tkinter.Label(win, text = 'Fire Damage Multiplier : \n(none for blank)             ')

prop_fire_entry = tkinter.Entry(win, width=20)

# Chill Instead Of Freeze
prop_chill_label = tkinter.Label(win, text='Chill Instead of Freeze : ')

prop_chill = tkinter.StringVar()

prop_chill.set(tfn_options[0])
prop_chill_drop = tkinter.OptionMenu(win, prop_chill, *tfn_options)

# Condition Immunities

# Immu Format

immu_format = '''"ConditionImmunities": [{0}
        ]'''

# For Current Immus

prop_immu_list = []
prop_immu_list_use = 0
prop_current_immu_label = tkinter.Label(win, text = f'Current Condition Immunities : {prop_immu_list}')

with open(f"{path}\Options\ECG\Prop\Condition Immunities options.txt", "r") as file:
        prop_immu_options = file.read().split(", ")

# For add Condition Immunities to list

def prop_immu_add():
    global prop_immu_list_use
    global armor_current_immu_label
    if prop_immu_list_use == 1:
        armor_current_immu_label.place_forget()
    temp = prop_immu.get()
    prop_immu_list.append(temp)
    armor_current_immu_label = tkinter.Label(win, text = f"Current Condition Immunities : {prop_immu_list}")
    armor_current_immu_label.place(x=82, y=540)
    prop_immu_list_use = 1

# For remove Condition Immunities from list

def prop_immu_remove():
    global prop_immu_list_use
    global armor_current_immu_label
    if prop_immu_list_use == 1:
        armor_current_immu_label.place_forget()
    prop_immu_list_len = len(prop_immu_list)
    del prop_immu_list[prop_immu_list_len - 1]
    armor_current_immu_label = tkinter.Label(win, text = f"Current Condition Immunities : {prop_immu_list}")
    armor_current_immu_label.place(x=82, y=540)
    prop_immu_list_use = 1

prop_immu_label = tkinter.Label(win, text = 'Condition Immunities : ')

prop_immu = tkinter.StringVar()

prop_immu.set(prop_immu_options[0])
prop_immu_drop = tkinter.OptionMenu(win, prop_immu, *prop_immu_options)

# Add Immu Button
prop_immu_add_btn = tkinter.Button(text="add", width=5)
prop_immu_add_btn.config(command=prop_immu_add)

# Remove Immu Button
prop_immu_remove_btn = tkinter.Button(text="remove", width=5)
prop_immu_remove_btn.config(command=prop_immu_remove)

# Condition Immunities Value

prop_immu_value_list = []
prop_immu_value_list_use = 0
prop_current_immu_value_label = tkinter.Label(win, text = f'Current Condition Immunities Value : {prop_immu_value_list}')

# For add Condition Immunities Value to list

def prop_immu_value_add():
    global prop_immu_value_list_use
    global armor_current_immu_value_label
    if prop_immu_value_list_use == 1:
        armor_current_immu_value_label.place_forget()
    temp = prop_immu_value_entry.get()
    prop_immu_value_list.append(temp)
    armor_current_immu_value_label = tkinter.Label(win, text = f"Current Condition Immunities Value : {prop_immu_value_list}")
    armor_current_immu_value_label.place(x=82, y=570)
    prop_immu_value_list_use = 1

# For remove Condition Immunities Value from list

def prop_immu_value_remove():
    global prop_immu_value_list_use
    global armor_current_immu_value_label
    if prop_immu_value_list_use == 1:
        armor_current_immu_value_label.place_forget()
    prop_immu_value_list_len = len(prop_immu_value_list)
    del prop_immu_value_list[prop_immu_value_list_len - 1]
    armor_current_immu_value_label = tkinter.Label(win, text = f"Current Condition Immunities Value : {prop_immu_value_list}")
    armor_current_immu_value_label.place(x=82, y=570)
    prop_immu_value_list_use = 1

prop_immu_value_label = tkinter.Label(win, text = 'Condition Immunities Value : ')

prop_immu_value_entry = tkinter.Entry(win, width= 20)

# Add Immu Button
prop_immu_value_add_btn = tkinter.Button(text="add", width=5)
prop_immu_value_add_btn.config(command=prop_immu_value_add)

# Remove Immu Button
prop_immu_value_remove_btn = tkinter.Button(text="remove", width=5)
prop_immu_value_remove_btn.config(command=prop_immu_value_remove)


# ------ Custom Armor ------

# For description current list 

armor_flag_list = []
armor_layer_list = []
armor_layer_hp_list = []
armor_parti_list = []

armor_flag_list_use = 0
armor_layer_list_use = 0
armor_layer_hp_list_use = 0
armor_parti_list_use = 0

armor_current_flag_label = tkinter.Label(win, text = f"Current Armor Flag : {armor_flag_list}")
armor_current_armor_layer_label = tkinter.Label(win, text = f"Current Armor Layer : {armor_layer_list}")
armor_current_armor_layer_hp_label = tkinter.Label(win, text = f"Current Armor Layer hp : {armor_layer_hp_list}")
armor_current_armor_parti_label = tkinter.Label(win, text = f"Current Particle Layer Override : {armor_parti_list}")

# For add Armor Flag to list

def armor_flag_add():
    global armor_flag_list_use
    global armor_current_flag_label
    if armor_flag_list_use == 1:
        armor_current_flag_label.place_forget()
    temp = armor_flag.get()
    armor_flag_list.append(temp)
    armor_current_flag_label = tkinter.Label(win, text = f"Current Armor Flag : {armor_flag_list}")
    armor_current_flag_label.place(x=82, y=540)
    armor_flag_list_use = 1

# For remove Armor Flag from list

def armor_flag_remove():
    global armor_flag_list_use
    global armor_current_flag_label
    if armor_flag_list_use == 1:
        armor_current_flag_label.place_forget()
    armor_flag_list_len = len(armor_flag_list)
    del armor_flag_list[armor_flag_list_len - 1]
    armor_current_flag_label = tkinter.Label(win, text = f"Current Armor Flag : {armor_flag_list}")
    armor_current_flag_label.place(x=82, y=540)
    armor_flag_list_use = 1

# For add Armor Layer to list

def armor_layer_add():
    global armor_layer_list_use
    global armor_current_layer_label
    if armor_layer_list_use == 1:
        armor_current_layer_label.place_forget()
    temp = armor_layer.get()
    armor_layer_list.append(temp)
    armor_current_layer_label = tkinter.Label(win, text = f"Current Armor Layer : {armor_layer_list}")
    armor_current_layer_label.place(x=82, y=570)
    armor_layer_list_use = 1

# For remove Armor Layer from list

def armor_layer_remove():
    global armor_layer_list_use
    global armor_current_layer_label
    if armor_layer_list_use == 1:
        armor_current_layer_label.place_forget()
    armor_layer_list_len = len(armor_layer_list)
    del armor_layer_list[armor_layer_list_len - 1]
    armor_current_layer_label = tkinter.Label(win, text = f"Current Armor Layer : {armor_layer_list}")
    armor_current_layer_label.place(x=82, y=570)
    armor_layer_list_use = 1

# For add Armor Layer Health to list

def armor_layer_hp_add():
    global armor_layer_hp_list_use
    global armor_current_layer_hp_label
    if armor_layer_hp_list_use == 1:
        armor_current_layer_hp_label.place_forget()
    temp = armor_layer_hp_entry.get()
    armor_layer_hp_list.append(temp)
    armor_current_layer_hp_label = tkinter.Label(win, text = f"Current Armor Layer hp : {armor_layer_hp_list}")
    armor_current_layer_hp_label.place(x=82, y=600)
    armor_layer_hp_list_use = 1

# For remove Armor Layer Health from list

def armor_layer_hp_remove():
    global armor_layer_hp_list_use
    global armor_current_layer_hp_label
    if armor_layer_hp_list_use == 1:
        armor_current_layer_hp_label.place_forget()
    armor_layer_hp_list_len = len(armor_layer_hp_list)
    del armor_layer_hp_list[armor_layer_hp_list_len - 1]
    armor_current_layer_hp_label = tkinter.Label(win, text = f"Current Armor Layer hp : {armor_layer_hp_list}")
    armor_current_layer_hp_label.place(x=82, y=600)
    armor_layer_hp_list_use = 1

    # For add Particle Layer Override to list

def armor_parti_add():
    global armor_parti_list_use
    global armor_current_parti_label
    if armor_parti_list_use == 1:
        armor_current_parti_label.place_forget()
    temp = armor_parti.get()
    armor_parti_list.append(temp)
    armor_current_parti_label = tkinter.Label(win, text = f"Current Particle Layer Override : {armor_parti_list}")
    armor_current_parti_label.place(x=82, y=630)
    armor_parti_list_use = 1

# For remove Particle Layer Override from list

def armor_parti_remove():
    global armor_parti_list_use
    global armor_current_parti_label
    if armor_parti_list_use == 1:
        armor_current_parti_label.place_forget()
    armor_parti_list_len = len(armor_parti_list)
    del armor_parti_list[armor_parti_list_len - 1]
    armor_current_parti_label = tkinter.Label(win, text = f"Current Particle Layer Override : {armor_parti_list}")
    armor_current_parti_label.place(x=82, y=630)
    armor_parti_list_use = 1

# Armor Aliases
armor_ali_label = tkinter.Label(win, text = 'Armor Aliases : ')

armor_ali_entry = tkinter.Entry(win, width=20)

# Comment
armor_comment_label = tkinter.Label(win, text = 'Comment : ')

armor_comment_entry = tkinter.Entry(win, width=20)

# Armor type
with open(f"{path}\Options\ECG\Armor\Armor Type options.txt", "r") as file:
        armor_type_options = file.read().split(", ")

armor_type_label = tkinter.Label(win, text = 'Armor Type : ')

armor_type = tkinter.StringVar()

armor_type.set(armor_type_options[0])
armor_type_drop = tkinter.OptionMenu(win, armor_type, *armor_type_options)

# Class Name
with open(f"{path}\Options\ECG\Armor\Class Name options.txt", "r") as file:
        armor_class_options = file.read().split(", ")

armor_class_label = tkinter.Label(win, text = 'Class Name : ')

armor_class = tkinter.StringVar()

armor_class.set(armor_class_options[0])
armor_class_drop = tkinter.OptionMenu(win, armor_class, *armor_class_options)

# Base Health
armor_hp_label = tkinter.Label(win, text = 'Base Heath : ')

armor_hp_entry = tkinter.Entry(win, width=20)

# Armor Flag
with open(f"{path}\Options\ECG\Armor\Armor Flag options.txt", "r") as file:
        armor_flag_options = file.read().split(", ")

armor_flag_label = tkinter.Label(win, text = 'Armor Flag :')

armor_flag = tkinter.StringVar()

armor_flag.set(armor_flag_options[0])
armor_flag_drop = tkinter.OptionMenu(win, armor_flag, *armor_flag_options)

# Add Flag Button
armor_flag_add_btn = tkinter.Button(text="add", width=5)
armor_flag_add_btn.config(command=armor_flag_add)

# Remove Flag Button
armor_flag_remove_btn = tkinter.Button(text="remove", width=5)
armor_flag_remove_btn.config(command=armor_flag_remove)

# Armor Layers
with open(f"{path}\Options\ECG\Armor\Armor Layer options.txt", "r") as file:
        armor_layer_options = file.read().split(", ")

armor_layer_label = tkinter.Label(win, text = 'Armor Layer :')

armor_layer = tkinter.StringVar()

armor_layer.set(armor_layer_options[0])
armor_layer_drop = tkinter.OptionMenu(win, armor_layer, *armor_layer_options)

# Add Armor Layer Button
armor_layer_add_btn = tkinter.Button(text="add", width=5)
armor_layer_add_btn.config(command=armor_layer_add)

# Remove Armor Layer Button
armor_layer_remove_btn = tkinter.Button(text="remove", width=5)
armor_layer_remove_btn.config(command=armor_layer_remove)

# Armor Layer Health
armor_layer_hp_label = tkinter.Label(win, text = 'Armor Layer Heath : ')

armor_layer_hp_entry = tkinter.Entry(win, width=20)

# Add Armor Layer Health Button
armor_layer_hp_add_btn = tkinter.Button(text="add", width=5)
armor_layer_hp_add_btn.config(command=armor_layer_hp_add)

# Remove Armor Layer Health Button
armor_layer_hp_remove_btn = tkinter.Button(text="remove", width=5)
armor_layer_hp_remove_btn.config(command=armor_layer_hp_remove)

# Particle Layer Override
with open(f"{path}\Options\ECG\Armor\Armor Particle Layer options.txt", "r") as file:
        armor_parti_options = file.read().split(", ")

armor_parti_label = tkinter.Label(win, text = 'Particle Layer Override : ')

armor_parti = tkinter.StringVar()

armor_parti.set(armor_parti_options[0])
armor_parti_drop = tkinter.OptionMenu(win, armor_parti, *armor_parti_options)

# Add Particle Layer Override Button
armor_parti_add_btn = tkinter.Button(text="add", width=5)
armor_parti_add_btn.config(command=armor_parti_add)

# Remove Particle Layer Override Button
armor_parti_remove_btn = tkinter.Button(text="remove", width=5)
armor_parti_remove_btn.config(command=armor_parti_remove)

# Impact Sound Event
with open(f"{path}\Options\ECG\Armor\Impact Sound options.txt", "r") as file:
        armor_impact_options = file.read().split(", ")

armor_impact_label = tkinter.Label(win, text = 'Impact Sound Event : ')

armor_impact = tkinter.StringVar()

armor_impact.set(armor_impact_options[0])
armor_impact_drop = tkinter.OptionMenu(win, armor_impact, *armor_impact_options)

# Drop Sound Event
with open(f"{path}\Options\ECG\Armor\Drop Sound options.txt", "r") as file:
        armor_drop_options = file.read().split(", ")

armor_drop_label = tkinter.Label(win, text = 'Drop Sound Event : ')

armor_drop = tkinter.StringVar()

armor_drop.set(armor_drop_options[0])
armor_drop_drop = tkinter.OptionMenu(win, armor_drop, *armor_drop_options)

# Fire Layer
with open(f"{path}\Options\ECG\Armor\Fire Layer option.txt", "r") as file:
        armor_fire_options = file.read().split(", ")

armor_fire_label = tkinter.Label(win, text = 'Fire Layer : ')

armor_fire = tkinter.StringVar()

armor_fire.set(armor_fire_options[0])
armor_fire_drop = tkinter.OptionMenu(win, armor_fire, *armor_fire_options)

# Armor Fomrat, {3} for class name, {8} for particle layer override, {9} for FireLayer
armor_format = '''"#comment : copy-paste below to Zombie Properties Extra",
"ZombieArmorProps": [
            "RTID({0}@CurrentLevel)"
        ],
"#comment : copy-paste below to level json",
{{
    "objclass": "ArmorPropertySheet",
    "#comment": "{1} | ECG",
    "aliases": [
        "{0}"
    ],
    "objdata": {{
        "ArmorType": {2},{3}
        "BaseHealth": {4},
        "ArmorFlags": [
            {5}
        ],
        "ArmorLayers": [
            {6}
        ],
        "ArmorLayerHealth": [
            {7}
        ],{8}{9}
        "ImpactSoundEvent": {10},
        "DropSoundEvent": {11}
    }}
}},'''


# ------ Commands Class ------

class Commands ():

    def __init__(self):

        # For use count
        self.use_count = 0

        # For code
        self.code = ''
        self.code_list = []

        # For unpacking armor list
        self.flag_str = ''
        self.layer_str = ''
        self.layer_hp_str = ''
        self.parti_str = ''

        # For unpacking prop immu
        self.immu_list = []
        self.immu_list_str = ''

    # For making code

    def making_code(self):

        # Delete "Done!" message
        if self.use_count == 1:
            self.done.place_forget()

        self.option_str = option.get()

        # Bring element & Fill codes

        # Zombie Types Extra
        if self.option_str == 'Zombie Types Extra':
            self.place = type_place.get()
            self.basic = type_basic.get()
            self.al = type_al.get()
            self.hasty = type_hasty.get()
            self.flag = type_flag.get()

            if self.place == 'none':
                pass
            else:
                self.code_list.append(f'"Placeable" : {self.place}')

            if self.basic == 'none':
                pass
            else:
                self.code_list.append(f'"IsBasicZombie" : {self.basic}')

            if self.al == 'none':
                pass
            else:
                self.code_list.append(f'"AlmanacBackDropName" : {self.al}')

            if self.hasty == 'none':
                pass
            else:
                self.code_list.append(f'"HastyOnStart" : {self.hasty}')

            if self.flag == 'none':
                pass
            else:
                self.code_list.append(f'"FlagType" : {self.flag}')

            self.len_code_list = len(self.code_list)

            for self.i in range(0, self.len_code_list):
                if self.i == 0:
                    if self.len_code_list == 1:
                        self.code = self.code + self.code_list[self.i]
                    else:
                        self.code = self.code + self.code_list[self.i] + ','

                elif self.i > 0 and self.i < self.len_code_list - 1:
                    self.code = self.code +  "\n            " + self.code_list[self.i] + ","

                else:
                    self.code = self.code +  "\n            " + self.code_list[self.i]
            
            self.file_name = fr'{path}/Result json/Extra Code Generator - Zombie Types Extra.json'

        # Zombie Properties Extra
        if self.option_str == 'Zombie Properties Extra':
            self.tossed_strong = prop_tossed_strong.get()
            self.tossed_weak = prop_tossed_weak.get()
            self.fly = prop_fly.get()
            self.surren = prop_surren.get()
            self.zombie_win = prop_win.get()
            self.explo = prop_explo.get()
            self.shrunken = prop_shrunken_entry.get()
            self.fire = prop_fire_entry.get()
            self.chill = prop_chill.get()
            self.immu = prop_immu_list
            self.immu_value = prop_immu_value_list

            if self.tossed_strong == 'none':
                pass
            else:
                self.code_list.append(f'"CanBePlantTossedStrong" : {self.tossed_strong}')

            if self.tossed_weak == 'none':
                pass
            else:
                self.code_list.append(f'"CanBePlantTossedWeak" : {self.tossed_weak}')

            if self.fly == 'none':
                pass
            else:
                self.code_list.append(f'"IsSpawnedFlying" : {self.fly}')

            if self.surren == 'none':
                pass
            else:
                self.code_list.append(f'"CanSurrender" : {self.surren}')

            if self.zombie_win == 'none':
                pass
            else:
                self.code_list.append(f'"CanTriggerZombieWin" : {self.zombie_win}')

            if self.explo == 'none':
                pass
            else:
                self.code_list.append(f'"ExplodesWhenMowed" : {self.explo}')

            if self.shrunken == 'none':
                pass
            else:
                self.code_list.append(f'"ShrunkenScale" : {self.shrunken}')

            if self.fire == 'none':
                pass
            else:
                self.code_list.append(f'"FireDamageMultiplier" : {self.fire}')

            if self.chill == 'none':
                pass
            else:
                self.code_list.append(f'"ChillInsteadOfFreeze" : {self.chill}')

            # For Condition
            self.len_immu = len(self.immu)
            self.len_immu_value = len(self.immu_value)

            if "none" in self.immu or "none" in self.immu_value or self.len_immu == 0 or self.len_immu_value == 0:
                pass
            else:
                for self.n in range(0, self.len_immu):
                    if self.n == 0:
                        if self.len_immu == 0:
                            self.immu_list_str = self.immu_list_str + f'            {{\n                "Condidion" : "{self.immu[self.n]}",\n                "Percent" : {self.immu_value[self.n]}\n            }}'

                        else:
                            self.immu_list_str = self.immu_list_str + f'\n            {{\n                "Condidion" : "{self.immu[self.n]}",\n                "Percent" : {self.immu_value[self.n]}\n            }},'
                    
                    elif self.n > 0 and self.n < self.len_immu:
                            self.immu_list_str = self.immu_list_str + f'\n            {{\n                "Condidion" : "{self.immu[self.n]}",\n                "Percent" : {self.immu_value[self.n]}\n            }},'
                    
                    else:
                            self.immu_list_str = self.immu_list_str + f'\n            {{\n                "Condidion" : "{self.immu[self.n]}",\n                "Percent" : {self.immu_value[self.n]}\n            }}'
                self.code_list.append(immu_format.format(self.immu_list_str))

            self.len_code_list = len(self.code_list)

            for self.i in range(0, self.len_code_list):
                if self.i == 0:
                    if self.len_code_list == 1:
                        self.code = self.code + self.code_list[self.i]
                    else:
                        self.code = self.code + self.code_list[self.i] + ','

                elif self.i > 0 and self.i < self.len_code_list - 1:
                    self.code = self.code +  "\n            " + self.code_list[self.i] + ","

                else:
                    self.code = self.code +  "\n            " + self.code_list[self.i]
                
            self.immu_list_str = ''
            self.immu_list = []

            self.file_name = fr'{path}/Result json/Extra Code Generator - Zombie Properties Extra.json'
            
        # Custom Armor
        if self.option_str == 'Custom Armor':
            self.ali = armor_ali_entry.get()
            self.comment = armor_comment_entry.get()
            self.armor_type = armor_type.get()
            self.hp = armor_hp_entry.get()
            self.impact = armor_impact.get()
            self.drop = armor_drop.get()

            if self.impact == 'none':
                self.impact = '""'

            if self.drop == 'none':
                self.drop = '""'

            # These are need to unpack list to str
            self.flag = armor_flag_list
            self.layer = armor_layer_list
            self.layer_hp = armor_layer_hp_list
            self.parti = armor_parti_list

            # Len all elements
            self.len_flag = len(self.flag)
            self.len_layer = len(self.layer)
            self.len_layer_hp = len(self.layer_hp)
            self.len_parti = len(self.parti)

            # Add all resources as string
            if "none" in self.flag or self.len_flag == 0:
                self.flag = ''
            else:
                for self.i in range(0, self.len_flag):
                    if self.i == 0:
                        if self.len_flag == 1:
                            self.flag_str = self.flag_str + self.flag[self.i]
                        else:
                            self.flag_str = self.flag_str + self.flag[self.i] + ','
                    elif self.i > 0 and self.i < self.len_flag - 1:
                        self.flag_str = self.flag_str +  "\n            " + self.flag[self.i] + ","
                    else:
                        self.flag_str = self.flag_str +  "\n            " + self.flag[self.i]
            
            if "none" in self.layer or self.len_layer == 0:
                self.layer = ''
            else:
                for self.i in range(0, self.len_layer):
                    if self.i == 0:
                        if self.len_layer == 1:
                            self.layer_str = self.layer_str + self.layer[self.i]
                        else:
                            self.layer_str = self.layer_str + self.layer[self.i] + ','
                    elif self.i > 0 and self.i < self.len_layer - 1:
                        self.layer_str = self.layer_str +  "\n            " + self.layer[self.i] + ","
                    else:
                        self.layer_str = self.layer_str +  "\n            " + self.layer[self.i]

            if "none" in self.layer_hp or self.len_layer_hp == 0:
                self.layer_hp = ''
            else:
                for self.i in range(0, self.len_layer_hp):
                    if self.i == 0:
                        if self.len_layer_hp == 1:
                            self.layer_hp_str = self.layer_hp_str + self.layer_hp[self.i]
                        else:
                            self.layer_hp_str = self.layer_hp_str + self.layer_hp[self.i] + ','
                    elif self.i > 0 and self.i < self.len_layer_hp - 1:
                        self.layer_hp_str = self.layer_hp_str +  "\n            " + self.layer_hp[self.i] + ","
                    else:
                        self.layer_hp_str = self.layer_hp_str +  "\n            " + self.layer_hp[self.i]

            if "none" in self.parti or self.len_parti == 0:
                self.parti_str = ''
            else:
                for self.i in range(0, self.len_parti):
                    if self.i == 0:
                        if self.len_parti ==1:
                            self.parti_str = self.parti_str + self.parti[self.i]
                        else:
                            self.parti_str = self.parti_str + self.parti[self.i] + ','
                    elif self.i > 0 and self.i < self.len_parti - 1:
                        self.parti_str = self.parti_str +  "\n            " + self.parti[self.i] + ","
                    else:
                        self.parti_str = self.parti_str +  "\n            " + self.parti[self.i]
                        
            # These are need to add as str instead of format
            self.class_name = armor_class.get()
            self.fire = armor_fire.get()

            if "none" in self.class_name:
                self.class_name = ''
            else:
                self.class_name = f'\n        "ClassName": {self.class_name},'

            if "none" in self.parti:
                self.parti_str = ''
            else:
                self.parti_str = f'\n        "ParticleLayerOverride": [\n            {self.parti_str}\n        ],'
                
            if "none" in self.fire:
                self.fire = ''
            else:
                self.fire = f'\n        "FireLayer": "{self.fire}",'

            self.code = armor_format.format(self.ali, self.comment, self.armor_type, self.class_name, self.hp, self.flag_str, self.layer_str, self.layer_hp_str, self.parti_str, self.fire, self.impact, self.drop)

            self.file_name = fr'{path}/Result json/Extra Code Generator - Custom Armor.json'

            self.flag_str = ''
            self.layer_str = ''
            self.layer_hp_str = ''
            self.parti_str = ''

        # Make json file & Write Code
        with open(self.file_name, "w") as out_file:
            out_file.write(str(self.code))

        # Place "Done!" message
        self.done = tkinter.Label(win, text='Done!')
        self.done.place(x=850, y=655)

        self.use_count = 1
        self.code_list = []
        self.code =''

    # Show entries
    def show_entries(self):
        self.option_str = option.get()

        # Zombie Types Extra
        if self.option_str == 'Zombie Types Extra':
            type_place_label.place(x=300, y=100)
            type_place_drop.place(x=300, y=120)
            type_basic_label.place(x=300, y=180)
            type_basic_drop.place(x=300, y=200)
            type_al_label.place(x=300, y=260)
            type_al_drop.place(x=300, y=280)
            type_hasty_label.place(x=300, y=340)
            type_hasty_drop.place(x=300, y=360)
            type_flag_label.place(x=300, y=420)
            type_flag_drop.place(x=300, y=440)

        # Zombie Properties Extra
        if self.option_str == 'Zombie Properties Extra':
            prop_tossed_strong_label.place(x=300, y=100)
            prop_tossed_strong_drop.place(x=300, y=120)
            prop_tossed_weak_label.place(x=300, y=180)
            prop_tossed_weak_drop.place(x=300, y=200)
            prop_fly_label.place(x=300, y=260)
            prop_fly_drop.place(x=300, y=280)
            prop_surren_label.place(x=300, y=340)
            prop_surren_drop.place(x=300, y=360)
            prop_explo_label.place(x=300, y=420)
            prop_explo_drop.place(x=300, y=440)
            prop_win_label.place(x=500, y=100)
            prop_win_drop.place(x=500, y=120)
            prop_shrunken_label.place(x=500, y=180)
            prop_shrunken_entry.place(x=500, y=220)
            prop_fire_label.place(x=500, y=260)
            prop_fire_entry.place(x=500, y=300)
            prop_chill_label.place(x=500, y=340)
            prop_chill_drop.place(x=500, y=360)
            prop_immu_label.place(x=700, y=100)
            prop_immu_drop.place(x=700, y=120)
            prop_immu_add_btn.place(x=700, y=150)
            prop_immu_remove_btn.place(x=745, y=150)
            prop_current_immu_label.place(x=82, y=540)
            prop_immu_value_label.place(x=700, y=200)
            prop_immu_value_entry.place(x=700, y=220)
            prop_immu_value_add_btn.place(x=700, y=240)
            prop_immu_value_remove_btn.place(x=745, y=240)
            prop_current_immu_value_label.place(x=82, y=570)

        # Custom Armor
        if self.option_str == 'Custom Armor':
            armor_ali_label.place(x=300, y=100)
            armor_ali_entry.place(x=300, y=120)
            armor_comment_label.place(x=300, y=160)
            armor_comment_entry.place(x=300, y=180)
            armor_type_label.place(x=300, y=220)
            armor_type_drop.place(x=300, y=240)
            armor_class_label.place(x=300, y=280)
            armor_class_drop.place(x=300, y=300)
            armor_hp_label.place(x=300, y=340)
            armor_hp_entry.place(x=300, y=360)
            armor_flag_label.place(x=300, y=400)
            armor_flag_drop.place(x=300, y=420)
            armor_flag_add_btn.place(x=300, y=450)
            armor_flag_remove_btn.place(x=345, y=450)
            armor_current_flag_label.place(x=82, y=540)
            armor_layer_label.place(x=500, y=100)
            armor_layer_drop.place(x=500, y=120)
            armor_layer_add_btn.place(x=500, y=150)
            armor_layer_remove_btn.place(x=545, y=150)
            armor_current_armor_layer_label.place(x=82, y=570)
            armor_layer_hp_label.place(x=500, y=200)
            armor_layer_hp_entry.place(x=500, y=220)
            armor_layer_hp_add_btn.place(x=500, y=250)
            armor_layer_hp_remove_btn.place(x=545, y=250)
            armor_current_armor_layer_hp_label.place(x=82, y=600)
            armor_parti_label.place(x=500, y=300)
            armor_parti_drop.place(x=500, y=320)
            armor_parti_add_btn.place(x=500, y=350)
            armor_parti_remove_btn.place(x=545, y=350)
            armor_current_armor_parti_label.place(x=82, y=630)
            armor_impact_label.place(x=500, y=400)
            armor_impact_drop.place(x=500, y=420)
            armor_drop_label.place(x=500, y=460)
            armor_drop_drop.place(x=500, y=480)
            armor_fire_label.place(x=700, y=200)
            armor_fire_drop.place(x=700, y=220)
            
            
        make_file_btn.place(x=900, y=650)

    def reset_all(self):
        
        # Add all things and do .place_forget()
        if self.use_count == 1:
            self.done.place_forget()
        type_place_label.place_forget()
        type_place_drop.place_forget()
        type_basic_label.place_forget()
        type_basic_drop.place_forget()
        type_al_label.place_forget()
        type_al_drop.place_forget()
        type_hasty_label.place_forget()
        type_hasty_drop.place_forget()
        type_flag_label.place_forget()
        type_flag_drop.place_forget()
        make_file_btn.place_forget()
        prop_tossed_strong_label.place_forget()
        prop_tossed_strong_drop.place_forget()
        prop_tossed_weak_label.place_forget()
        prop_tossed_weak_drop.place_forget()
        prop_fly_label.place_forget()
        prop_fly_drop.place_forget()
        prop_surren_label.place_forget()
        prop_surren_drop.place_forget()
        prop_win_label.place_forget()
        prop_win_drop.place_forget()
        prop_explo_label.place_forget()
        prop_explo_drop.place_forget()
        prop_shrunken_label.place_forget()
        prop_shrunken_entry.place_forget()
        prop_fire_label.place_forget()
        prop_fire_entry.place_forget()
        prop_chill_label.place_forget()
        prop_chill_drop.place_forget()
        prop_immu_label.place_forget()
        prop_immu_drop.place_forget()
        prop_immu_add_btn.place_forget()
        prop_immu_remove_btn.place_forget()
        prop_current_immu_label.place_forget()
        prop_immu_value_label.place_forget()
        prop_immu_value_entry.place_forget()
        prop_immu_value_add_btn.place_forget()
        prop_immu_value_remove_btn.place_forget()
        prop_current_immu_value_label.place_forget()
        armor_ali_label.place_forget()
        armor_ali_entry.place_forget()
        armor_comment_label.place_forget()
        armor_comment_entry.place_forget()
        armor_type_label.place_forget()
        armor_type_drop.place_forget()
        armor_class_label.place_forget()
        armor_class_drop.place_forget()
        armor_hp_label.place_forget()
        armor_hp_entry.place_forget()
        armor_flag_label.place_forget()
        armor_flag_drop.place_forget()
        armor_flag_add_btn.place_forget()
        armor_flag_remove_btn.place_forget()
        armor_current_flag_label.place_forget()
        armor_layer_label.place_forget()
        armor_layer_drop.place_forget()
        armor_layer_add_btn.place_forget()
        armor_layer_remove_btn.place_forget()
        armor_current_armor_layer_label.place_forget()
        armor_layer_hp_label.place_forget()
        armor_layer_hp_entry.place_forget()
        armor_layer_hp_add_btn.place_forget()
        armor_layer_hp_remove_btn.place_forget()
        armor_current_armor_layer_hp_label.place_forget()
        armor_parti_label.place_forget()
        armor_parti_drop.place_forget()
        armor_parti_add_btn.place_forget()
        armor_parti_remove_btn.place_forget()
        armor_current_armor_parti_label.place_forget()
        armor_impact_label.place_forget()
        armor_impact_drop.place_forget()
        armor_drop_label.place_forget()
        armor_drop_drop.place_forget()
        armor_fire_label.place_forget()
        armor_fire_drop.place_forget()
        

c = Commands()

# Butoon Commands
load_btn.config(command=c.show_entries)
reset_btn.config(command=c.reset_all)
make_file_btn.config(command=c.making_code)


# ------ Open Window ------

win.mainloop()
