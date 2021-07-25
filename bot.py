"""
    get_recent_changes.py

    MediaWiki API Demos
    Demo of `RecentChanges` module: Get the three most recent changes with
    sizes and flags

    MIT License
"""

import requests

bruh_string = None

S = requests.Session()

URL = "https://pl.scpslgame.com/api.php"

# change rclimit to get number of recent changes

PARAMS = {
    "format": "json",
    "rcprop": "title|ids|flags|user|timestamp|sizes|comment",
    "list": "recentchanges",
    "action": "query",
    "rclimit": "1",
    "rctype": "edit|new",
    "rcshow": "!minor|!anon"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

RECENTCHANGES = DATA['query']['recentchanges']

for rc in RECENTCHANGES:
    bruh_string = (str(rc['title']) + " at " + str(rc['timestamp']) + " by " + str(rc['user']) + " Comments: " + str(rc['comment']))

print(bruh_string)
