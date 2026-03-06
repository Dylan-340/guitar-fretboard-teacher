# at this point the first 20 or so lines of code is a 3.5/47 according to gemma3. must get a higher rating at the end.
 
# Program to help learn the guitar fretboard.

from time import sleep

import random

notes = ["A", "B", "C", "D", "E", "F", "G", "Bb/A#", "C#/Db", "D#/Eb", "F#/Gb", "G#/Ab"] #Note names
estring_frets = ["5", "7", "8", "10", "12", "1", "3", "6", "9", "11", "2", "4"] # Fret numbers for e strings
astring_frets = ["12", "2", "3", "5", "7", "8", "10", "1", "4", "6", "9", "11"] # Fret numbers for a string
dstring_frets = ["7", "9", "10", "12", "2", "3", "5", "8", "11", "1", "4", "6"] # Fret numbers for d string
gstring_frets = ["2", "4", "5", "7", "9", "10", "12", "3", "6", "8", "11", "1"] # Fret numbers for g string
bstring_frets = ["10", "12", "1", "3", "5", "6", "8", "11", "2", "4", "7", "9"] # Fret numbers for b string

string_frets = {
    "e": estring_frets,
    "a": astring_frets,
    "d": dstring_frets,
    "g": gstring_frets,
    "b": bstring_frets
}

print("ctrl-c to exit\n")

print("--Guitar Fretboard Teacher--\n")


def manual_setup():        # Asks the user if they want the notes to scroll automatically or manually, and gets the automatic delay if chosen, returns the bool of if manual mode is active, and if not the auto delay for the strings.
    
    note_delay = ""
    str_note_delay = ""
    
    print("Do you want auto or manual notes?\n")       
    manual_input = input("[a/m]: ").lower()
    while manual_input != "a" and manual_input != "m":
        print("error, answer must be an a or m")
        manual_input = input("[a/m]: ").lower()
    manual_input = (manual_input == 'm')

    if manual_input != True:

        str_note_delay = input("What delay in seconds would you like?: ") # Sets the delay between notes being printed if automatic notes are chosen
    if str_note_delay == "":                                              # If user leaves delay blank it defaults to 1 second
        note_delay = 1
    else:
        note_delay = float(str_note_delay)

    return manual_input, note_delay

def fret_hints_setup():                                 # Asks the user if they want the notes to show the coresponding fret number, returns the bool of if fret hints are active, and the string for the fret hints.

    fret_hints_input = False
    used_string = ""

    fret_hints_input = input("Do you want fret hints?\n[y/n]:").lower()

    while fret_hints_input != "y" and fret_hints_input != "n":
        print("error, answer must be a y or n")
        fret_hints_input = input("[y/n]: ").lower()      

    fret_hints_input = (fret_hints_input == 'y')

    if fret_hints_input == True:
        used_string = input("What string would you like the hints for? [E/A/D/G/B]").lower()
        while used_string != "e" and used_string != "a" and used_string != "d" and used_string != "g" and used_string != "b":
            print("error, answer must be an e, a, d, g, or b")
            used_string = input("What string would you like the hints for? [E/A/D/G/B]").upper()

    return fret_hints_input, used_string
    
def manual_notes():             # Runs if manual mode is active
    while True:
        if fret_hints_input == True:
            input()
            index = random.randint(0, 11)
            print(notes[index], selected_fret_hints[index])
        else:
            input()
            print(random.choice(notes), "\n")

def automatic_notes():          # Runs if automatic mode is active
    while True:
        if fret_hints_input == True:
            index = random.randint(0, 11)
            print(notes[index], selected_fret_hints[index], "\n")
            sleep(note_delay)
        else:
            print(random.choice(notes), "\n")
            sleep(note_delay)

manual_input, note_delay = manual_setup() # get the variables from the manual setup function
fret_hints_input, used_string = fret_hints_setup() # gets the variables from the fret hints setup

if fret_hints_input == True:        # chooses the string that should be used for fret hints
    selected_fret_hints = string_frets[used_string]

if manual_input == True:            # runs the proper auto/manual mode
    manual_notes()
else:
    print("auto")
    automatic_notes()