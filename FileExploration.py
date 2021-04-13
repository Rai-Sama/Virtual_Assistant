import os
from Conversing import speak_free, speak_no_space, assistant_talks
import speech_recognition as sr
import wolframalpha
import keyboard


def exploring(query, language):
    notes = ""
    if "explorer" in query.lower():
        os.system('explorer')
        assistant_talks("Press enter when you're done with the current task.", language)
        while not keyboard.is_pressed('enter'):
            continue
    elif "college" in query.lower():
        os.startfile("D:\\College")     # Change path as needed
        assistant_talks("Press enter when you're done studying.", language)
        while not keyboard.is_pressed('enter'):
            continue
    elif "movie" in query.lower():
        os.startfile("D:\\Movies n Shows\\Your name\\Kimi No Nawa.mp4") # Change path as needed
        assistant_talks("Press enter when you're done watching this great movie.", language)
        while not keyboard.is_pressed('enter'):
            continue
    elif "chess" in query.lower():
        os.system('python gui.py')   # Change path as needed or save the gui.py script in the same directory as this script
        assistant_talks("That was a good game", language)