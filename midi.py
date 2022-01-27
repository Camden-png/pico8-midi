import os, sys, math, platform
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

try: import pygame, pygame.midi
except: error("Pygame library")

try: import pydirectinput
except: error("Pydirectinput library")

chars = ["Z", "S", "X", "D", "C",
         "V", "G", "B", "H", "N",
         "J", "M", "Q", "2", "W",
         "3", "E", "R", "5", "T",
         "6", "Y", "7", "U", "I",
         "9", "O", "0", "P"]

keys = ["C0", "C#0", "D0", "D#0", "E0",
        "F0", "F#0", "G0", "G#0", "A0",
        "A#0", "B0", "C1", "C#1", "D1",
        "D#1", "E1", "F1", "F#1", "G1",
        "G#1", "A1", "A#1", "B1", "C2",
        "C#2", "D2", "D#2", "E2"]

def clear():
    if platform.system() == "Windows": os.system("cls")
    else: os.system("clear")

def error(message):
    print(f"Error: {message} not found!")
    sys.exit(1)

def number_to_note(number):
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    octave = math.floor(number / 12) - 4
    note = f"{notes[number % 12]}{octave}"
    return note

def read_input(device, queue):
    global keys, chars
    while True:
        if device.poll() and pygame.KEYDOWN:
            data = device.read(1)[0]
            number = data[0][1]
            if number >= 48 and number <= 76:
                note = number_to_note(number)
                if note not in queue:
                    queue.append(note)
                    char = chars[keys.index(note)].lower()
                    pydirectinput.press(char)
                    print(f"Pressed: {note}")
                else: queue.remove(note)

if __name__ == "__main__":
    clear()
    queue = []
    print("Midi to Pico-8 Python Edition\nBy Camden")
    try:
        pygame.midi.init()
        read_input(pygame.midi.Input(1), queue)
    except: pass
