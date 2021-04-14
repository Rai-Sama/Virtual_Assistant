This was made as a project for my Semester IV course Open Source Technology Lab.

Virtual Assistant
=============
This is a voice-recognition based virtual assistant made in python that listens to users' queries, analyzes the command and responds accordingly.

The assistant can answer general queries like "Who is Albert Einstein?" or "What is the weather forecast today?"

The assistant can also solve mathematical queries utilizing the WolframAlpha API. 

The Assistant can understand and speak all 108 languages Google Translate supports.

I have set both input and output languages to be english because my target audience was english-speaking. You can add the shorthand to any language you want supported in main.py and Conversing.py

You can also ask the assistant to write an essay for you on any topic. ( It will fetch you some paras on the provided topic from Wikipedia).

There is also support for recording audio. This was added as a specific use case where lectures on certain topics had to be recorded.

Layout of the project
=============
### Main.py ###
Main interface that integrates all the modules.

### Conversing.py ###
This module handles speech recognition and Text To Speech conversions

### Online.py ###
This module handles the web searches and APIs used to get results for the queries. The supported actions here include:

Getting any information you would expect to find on Wikipedia.

Getting solutions to Mathematical problems.

Asking for a specific website.

Getting a search engine results (Supports Google and duckduckgo).

Searching Youtube.

### FileExploration.py ###
A very simple module for navigating some of the offline queries. These include - 

Opening the college folder (You can make it any folder you may need)

Watching a saved movie (I have a movie folder on my system; you can use multiple folders or a file explorer search)

Playing chess - I have included a small chess game module that can be invoked from here. It is a fairly good chess engine that uses one of minimax or alpha-beta algorithms. If you want a tougher opponent I would recommend using the minimax algo.

### Corona.py ###
This module was added to help get statistics on Covid cases in India (The support for this module is unstable and may not work in the future as it completely depends on the website I have used to scrape the stats from)

### Chess.py and GUI.py ###
These are the chess game modules mentioned in FileExploration Section.

Flowchart
=============
![Flowchart](https://user-images.githubusercontent.com/48092867/114603877-e16d9180-9cb5-11eb-8523-4649ec916c74.png)
