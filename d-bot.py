import time
import requests
import discord

def getRC(recent_changes): 
    bruh_string = recent_changes
    URL = "https://en.scpslgame.com/api.php"
    S = requests.Session()
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
        bruh_string = "**" + (str(rc['title']) + "**" + " at " + str(rc['timestamp']) + " by " + str(rc['user']) + "|| **Comments:** " + str(rc['comment']))
    f = open("changes.txt", "r")
    compare = f.read()
    f.close()
    if (compare != bruh_string):
        f2 = open("changes.txt", "w")
        f2.write(bruh_string)
        f2.close()
        print(bruh_string)
        return bruh_string
    time.sleep(10)

def getRCRu(recent_changes):
    bruh_string = recent_changes
    URL = "https://ru.scpslgame.com/api.php"
    S = requests.Session()
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
        bruh_string = "**" + (str(rc['title']) + "**" + " at " + str(rc['timestamp']) + " by " + str(rc['user']) + "|| **Comments:** " + str(rc['comment']))
    f = open("changesRU.txt", "r")
    compare = f.read()
    f.close()
    if (compare != bruh_string):
        f2 = open("changesRU.txt", "w")
        f2.write(bruh_string)
        f2.close()
        print(bruh_string)
        return bruh_string
    time.sleep(10)

def getRCPl(recent_changes):
    bruh_string = recent_changes
    URL = "https://pl.scpslgame.com/api.php"
    S = requests.Session()
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
        bruh_string = "**" + (str(rc['title']) + "**" + " at " + str(rc['timestamp']) + " by " + str(rc['user']) + "|| **Comments:** " + str(rc['comment']))
    f = open("changesPL.txt", "r")
    compare = f.read()
    f.close()
    if (compare != bruh_string):
        f2 = open("changesPL.txt", "w")
        f2.write(bruh_string)
        f2.close()
        print(bruh_string)
        return bruh_string
    time.sleep(10)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        print("it has to reach here")
        channel = client.get_channel(748233192523300976)
        channel2 = client.get_channel(748232391256047616)
        channel3 = client.get_channel(748232966571819008)
        while True:
            print("Reaches here!")
            recent_changes = None
            nice_cock_bro = getRC(recent_changes)
            nice_tits_bro = getRCRu(recent_changes)
            nice_balls_bro = getRCPl(recent_changes)
            if nice_cock_bro != None and nice_cock_bro != "":
                print("letsss gooo")
                print(nice_cock_bro)
                await channel.send(nice_cock_bro)
            if nice_tits_bro != None and nice_tits_bro != "":
                print("cyka blyat")
                await channel2.send(nice_tits_bro)
            if nice_balls_bro != None and nice_balls_bro != "":
                print("femboy")
                await channel3.send(nice_balls_bro)
client = MyClient()
client.run('TOKEN')