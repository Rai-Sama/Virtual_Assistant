import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import numpy as np
import keyboard
import matplotlib.pyplot as plt
from Conversing import speak_free, speak_no_space, assistant_talks


def live_updates(language):
    contents = lambda row: [x.text.replace('\n', '') for x in row]
    URL = 'https://www.mohfw.gov.in/'

    SHORT_HEADERS = ['SNo', 'State', 'Confirmed cases',
                     'Cured/ Discharged/ Migrated', 'Death']

    response = requests.get(URL).content
    soup = BeautifulSoup(response, 'html.parser')
    header = contents(soup.tr.find_all('th'))

    stats = []
    all_rows = soup.find_all('tr')
    states = []
    cases = []

    for row in all_rows[1:-1]:
        stat = contents(row.find_all('td'))
        stats.append(stat)

    assistant_talks("Here is a table showing the live updated stats for the coronavirus pandemic in India", language)

    table = tabulate(stats[0: len(stats) - 5], headers=SHORT_HEADERS)
    print(table)
    print("\n\n")
    assistant_talks(f"Total confirmed cases: {stats[-4][-1]}", language)
    assistant_talks(f"Total number of cured/discharged/migrated cases: {stats[-4][-3]}", language)
    assistant_talks(f"Total deaths: {stats[-4][-2]}", language)

    for row in stats[0:-5]:
        states.append(row[1])
        cases.append(int(row[2]) + int(row[3]))

    y_pos = np.arange(len(states))

    plt.barh(y_pos, cases, align='center', alpha=0.5,
             color=(234 / 256.0, 128 / 256.0, 252 / 256.0),
             edgecolor=(106 / 256.0, 27 / 256.0, 154 / 256.0))
    assistant_talks("Press enter when you're done with the current task.", language)
    while not keyboard.is_pressed('enter'):
        continue

    assistant_talks("Would you like me to plot a bar-graph of the state-wise stats?", language)
    plotting = ""
    plotting = speak_free()
    if "yes" in plotting.lower() or "plot" in plotting.lower():
        plt.yticks(y_pos, states)
        plt.xlim(1, max(cases) * 1.5)
        plt.xlabel('Number of Cases')
        plt.title('Corona Virus Cases')
        plt.show()


