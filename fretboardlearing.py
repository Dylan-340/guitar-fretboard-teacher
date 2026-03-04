# at this point the first 20 or so lines of code is a 3.5/47 according to gemma3. must get a higher rating at the end.
 
#Program to help learn the guitar fretboard.

from time import sleep

import random

notes = ["A", "B", "C", "D", "E", "F", "G", "Bb/A#", "C#/Db", "D#/Eb", "F#/Gb", "G#/Ab"] #Note names
estring_frets = ["5", "7", "8", "10", "12", "1", "3", "6", "9", "11", "2", "4"] # Fret numbers for e strings
astring_frets = ["12", "2", "3", "5", "7", "8", "10", "1", "4", "6", "9", "11"] # Fret numbers for a string
dstring_frets = ["7", "9", "10", "12", "2", "3", "5", "8", "11", "1", "4", "6"] # Fret numbers for d string
gstring_frets = ["2", "4", "5", "7", "9", "10", "12", "3", "6", "8", "11", "1"] # Fret numbers for g string
bstring_frets = ["10", "12", "1", "3", "5", "6", "8", "11", "2", "4", "7", "9"] # Fret numbers for b string

print("ctrl-c to exit\n")

print("--Guitar Fretboard Teacher--\n")


def manual_setup():                                     # Asks the user if they want the notes to scroll automatically or manually
    print("Do you want auto or manual notes?\n")
    manual_input = input("[a/m]: ").lower()
    while manual_input != "a" and manual_input != "m":
        print("error, answer must be an a or m")
        manual_input = input("[a/m]: ").lower()
    manual_input = (manual_input == 'm')
    return manual_input

def fret_hints_setup():                                 # Asks the user if they want the notes to show the coresponding fret number
    
    fret_hints_input = input("Do you want fret hints?\n[y/n]:").lower()
    while fret_hints_input != "y" and fret_hints_input != "n":
        print("error, answer must be a y or n")
        fret_hints_input = input("[y/n]: ").lower()       
    fret_hints_input = (fret_hints_input == 'y')
    return fret_hints_input
    
    
manual_input = manual_setup() 
#fret_hints_input = fret_hints_setup()


if manual_input != True:

    str_note_delay = input("What delay in seconds would you like?: ") # Sets the delay between notes being printed if automatic notes are chosen
    if str_note_delay == "": # If user leaves delay blank it defaults to 1 second
        note_delay = 1
    else:
        note_delay = float(str_note_delay) 



while True:

    if manual_input == True:
        input()
        print(random.choice(notes))
    else:
        print(random.choice(notes), "\n")
        sleep(note_delay)
