# at this point the first 20 or so lines of code is a 3.5/47 according to gemma3. must get a higher rating at the end.

#Program to help learn the guitar fretboard.

from time import sleep
import random

notes = ["A", "B", "C", "D", "E", "F", "G", "Bb/A#", "C#/Db", "D#/Eb", "F#/Gb", "G#/Ab"]
estring_frets = ["5", "7", "8", "10", "12", "1", "3", "6", "9", "11", "2", "4"]
astring_frets = ["12", "2", "3", "5", "7", "8", "10", "1", "4", "6", "9", "11"]
dstring_frets = ["7", "9", "10", "12", "2", "3", "5", "8", "11", "1", "4", "6"]
gstring_frets = ["2", "4", "5", "7", "9", "10", "12", "3", "6", "8", "11", "1"]
bstring_frets = ["10", "12", "1", "3", "5", "6", "8", "11", "2", "4", "7", "9"]

print("ctrl-c to exit\n")

print("--Guitar Fretboard Teacher--\n")

print("Do you want auto or manual notes?\n")

manual_input = input("[a/m]: ").lower()

    

while manual_input != "a" and manual_input != "m":
    print("error, answer must be an a or m")
    manual_input = input("[a/m]: ").lower()
    

else:
    manual_input_error = 0


manual_input = (manual_input == 'm')

if manual_input != True:

    str_note_delay = input("What delay in seconds would you like?: ")
    note_delay = float(str_note_delay)


while True:

    if manual_input == True:
        input()
        print(random.choice(notes))
    else:
        print(random.choice(notes), "\n")
        sleep(note_delay)