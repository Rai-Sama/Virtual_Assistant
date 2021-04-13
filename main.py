import os
import getpass
from Conversing import speak_no_space, speak_free, assistant_talks, record_notes
from FileExploration import exploring
from Online import searcher, search_wolf, surf_web, emailing, weather, summary
import webbrowser
import keyboard
from corona import live_updates
import time
access = False
human = ""
assistant = "Better Alexa"
language = ""
os.startfile('listening.gif')
n = 0
iterations = 0
language = "en"
assistant_talks(f"Hello, I'm your personal assistant, {assistant}", language)
assistant_talks("What should i call you?", language)
name = speak_free(language)
assistant_talks(f"Welcome, {name}", language, 1)

assistant_talks(f"Please verify your identity by inputting the code to access my services, {name}", language)
password = getpass.getpass("Password: ")

if password == "password123":
    access = True
    assistant_talks("You have been granted access.")
else:
    access = False
    assistant_talks("Sorry, that was not the correct password. Your access has been denied.")

while access:
    assistant_talks(f"I'm now ready for your commands. Press enter whenever you have one for me.", language)
    while not keyboard.is_pressed('enter'):
        continue
    human = speak_free(language)
    time.sleep(1)
    if "hi " in human.lower() or "hello" in human.lower() or "how are you" in human.lower():
        if "hi" in human.lower() or "hello" in human.lower():
            assistant_talks(f"Hello, {name}. It is a pleasure assisting you.", language)
        else:
            assistant_talks("I'm doing fine. Thank you for asking.", language)
    elif "explorer" in human.lower():
        assistant_talks("Understood. Opening file explorer", language)
        exploring("explorer", language)  # Go to exploring in FileExploration.py module and change the path according to your system
    elif "college" in human.lower():
        assistant_talks("Understood. Opening your college study folder", language)
        exploring("college", language) # Go to exploring in FileExploration.py module and change the path according to your system
    elif "movie" in human.lower():
        assistant_talks("Understood. Here's a good movie for you to watch.", language)
        exploring("movie", language) # Go to exploring in FileExploration.py module and change the path according to your system
    elif "play" in human.lower() or "game" in human.lower() or "chess" in human.lower():
        assistant_talks("Understood. I accept your challenge.", language)
        exploring("chess", language) # Go to exploring in FileExploration.py module and change the path according to your system
    elif "notes" in human.lower() or "record" in human.lower() or "audio" in human.lower():
        assistant_talks("Understood", language)
        record_notes(language)

    elif "google" in human.lower():
        assistant_talks("Understood.", language)
        searcher("google", language)
    elif "youtube" in human.lower():
        assistant_talks("Understood.", language)
        searcher("youtube", language)
    elif "duck duck go" in human.lower() or "duck" in human.lower():
        assistant_talks("Understood.", language)
        searcher("duckduckgo", language)
    elif "reddit" in human.lower():
        assistant_talks("Understood.", language)
        searcher("reddit", language)
    elif "wikipedia" in human.lower():
        assistant_talks("Understood.", language)
        searcher("wikipedia", language)
    elif "website" in human.lower() or "site" in human.lower():
        assistant_talks("Understood.", language)
        surf_web(language)
    elif "what is an" in human.lower() or "what is a" in human.lower() or "what is" in human.lower() or "tell me about" in human.lower()\
            or "who is" in human.lower() or "who was" in human.lower():
        if "what is a" in human.lower():
            human = human.lower().replace("what is a ", "")
        elif "what is" in human.lower():
            human = human.lower().replace("what is ", "")
        elif "what is an" in human.lower():
            human = human.lower().replace("what is an ", "")
        elif "who is" in human.lower():
            human = human.lower().replace("who is ", "")
        elif "who was" in human.lower():
            human = human.lower().replace("who was ", "")
        else:
            human = human.lower().replace("tell me about ", "")
        summary(human, language)
    elif "email" in human.lower() or "e-mail" in human.lower() or "mail" in human.lower():
        assistant_talks("Understood.", language)
        emailing(language)
    elif "solve" in human.lower() or "calculate" in human.lower():
        assistant_talks("Understood.", language)
        search_wolf(human, language)
    elif "weather" in human.lower() or "forecast" in human.lower():
        assistant_talks("Understood.", language)
        weather(language)
    elif "essay" in human.lower() or "assignment" in human.lower() or "summary" in human.lower():
        assistant_talks("Understood. I will fetch some info for you.", language)
        searcher("wiki", language)
    elif "where is" in human.lower():
        location = human
        location = location.replace("where is ", "")
        assistant_talks("Understood. Looking up " + location)
        tab_url = "https://www.google.com/maps/place/" + location
        webbrowser.open(tab_url, new=2)
    elif "corona" in human.lower() or "virus" in human.lower() or "coronavirus" in human.lower() or "nineteen" in human.lower()\
            or "19" in human.lower() or "covid" in human.lower() or "covid 19" in human.lower() or "covid-19" in human.lower()\
            or "pandemic" in human.lower() or "epidemic" in human.lower() or "live update" in human.lower():
        live_updates(language)

    elif ("stop" in human.lower()) or ("quit" in human.lower()) or ("goodbye" in human.lower()) or ("bye" in human.lower()):
        assistant_talks(f"Goodbye, {name}. It was nice talking to you. I hope your experience was pleasant.", language)
        break
    else:
        assistant_talks("Sorry, I couldn't understand you.", language)