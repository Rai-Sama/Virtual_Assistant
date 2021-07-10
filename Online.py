import webbrowser
from os import path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass
from Conversing import speak_free, speak_no_space, assistant_talks
import wolframalpha
import wikipedia
import random
import keyboard


def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


def searcher(site, language):
    query = ""
    lang = "en"
    if site.lower() == "google":
        tabUrl = "https://google.com/?#q="
        assistant_talks("What would you like to search on Google?", language)
        query = speak_free()
        assistant_talks("Searching Google for " + query, language)
        webbrowser.open(tabUrl + query, new=2)

    elif site.lower() == "reddit":
        tabUrl = "https://www.reddit.com/r/"
        assistant_talks("Which subreddit would you like to visit?", language)
        query = speak_no_space()
        assistant_talks("Opening r/" + query)
        webbrowser.open(tabUrl + query, new=2)

    elif site.lower() == "duckduckgo":
        tabUrl = "https://duckduckgo.com/?q="
        assistant_talks("What would you like to search on DuckDuckGo?", language)
        query = speak_free()
        assistant_talks("Searching DuckDuckGo for " + query)
        webbrowser.open(tabUrl + query, new=2)

    elif site.lower() == "youtube":
        tabUrl = "https://www.youtube.com/results?search_query="
        assistant_talks("What would you like to search for on Youtube?", language)
        query = speak_free()
        assistant_talks(f"Searching for {query} on youtube", language)
        webbrowser.open(tabUrl + query, new=2)

    elif site.lower() == "wikipedia" or site.lower() == "wiki":
        tabUrl = "https://en.wikipedia.org/wiki/"
        if "wikipedia" in site.lower():
            assistant_talks("What would you like to look for on Wikipedia?", language)
        else:
            assistant_talks("What would you like information on?", language)
        query = speak_free()
        assistant_talks(f"Searching for information on {query}", language)
        webbrowser.open(tabUrl + query, new=2)
        info = wikipedia.summary(query, sentences=1)
        if "wikipedia" in site.lower():
            # assistant_talks(info, language)
            pass
        else:
            n = ""
            n = f"{query}" + str(random.randint(1, 100))
            while path.exists(n + ".txt"):
                n = f"{query}" + random.randint(1, 100)
            f = open(n + ".txt", "w", encoding='utf-8')
            f.write(info)
            f.close()

    assistant_talks("Press enter when you're done with the current task.", language)
    while not keyboard.is_pressed('enter'):
        continue


def surf_web(language):
    website = ""
    assistant_talks("Tell me the name of the website along with it's extension, like .com or .org", language)
    website = speak_no_space()
    assistant_talks(f"{website}, it is", language)
    tabUrl = "https://"  # Can be changed to simply www.
    webbrowser.open(tabUrl + website, new=2)
    assistant_talks("Press enter when you're done exploring the website.", language)
    while not keyboard.is_pressed('enter'):
        continue


def emailing(language):
    msg = MIMEMultipart()

    assistant_talks("Please tell me the subject of this E-mail", language)
    msg['Subject'] = speak_free()

    assistant_talks("Please dictate the body of your E-mail", language)
    message = speak_free()
    assistant_talks("Please type in your email address", language)
    flush_input()
    msg['From'] = input("From: ")
    assistant_talks("Now enter your password. Make sure no one is watching you.", language)
    password = getpass.getpass(prompt="Password: ", stream=None)
    assistant_talks("Please type in the E-mail address you want to contact.", language)
    msg['To'] = input("To: ")
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    assistant_talks("Your email has been successfully sent.", language)


def search_wolf(query, language):

    client = wolframalpha.Client('enter your api key')
    # A Wolfram Alpha api key is fairly easy to get just make an account and go to the api section
    result = client.query(query)
    try:
        output = next(result.results).text
    except StopIteration:
        output = "No results"
    assistant_talks(output, language)
    assistant_talks("Press enter when you're done with the current task.", language)
    while not keyboard.is_pressed('enter'):
        continue


def weather(language):

    client = wolframalpha.Client('enter your api key here')

    assistant_talks("Where do you want the weather forecast of?", language)
    result = client.query("Weather forecast for" + speak_free())

    try:
        output = next(result.results).text
    except StopIteration:
        output = "No results"
    assistant_talks(output, "english")
    assistant_talks("Press enter when you're done with the current task.", language)
    while not keyboard.is_pressed('enter'):
        continue


def summary(query, language):
    info = wikipedia.summary(query, sentences=5)
    assistant_talks(info, language)
