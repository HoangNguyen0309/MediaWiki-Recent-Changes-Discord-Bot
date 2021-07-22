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
        bruh_string = "**" + (str(rc['title']) + "**" + " at " + str(rc['timestamp']) + " by " + str(rc['user']) + " || **Comments:** " + str(rc['comment']))
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
        bruh_string = "**" + (str(rc['title']) + "**" + " at " + str(rc['timestamp']) + " by " + str(rc['user']) + " || **Comments:** " + str(rc['comment']))
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
        bruh_string = "**" + (str(rc['title']) + "**" + " at " + str(rc['timestamp']) + " by " + str(rc['user']) + " || **Comments:** " + str(rc['comment']))
    return bruh_string
    time.sleep(10)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        print("it has to reach here")
        channelEN = client.get_channel(867622165397897266)
        channelRU = client.get_channel(844898534184189973)
        channelPL = client.get_channel(867622185492545568)
        while True:
            messageEN = await channelEN.fetch_message(channelEN.last_message_id)
            messageRU = await channelRU.fetch_message(channelRU.last_message_id)
            messagePL = await channelPL.fetch_message(channelPL.last_message_id)
            messageEN1 = messageEN.content.strip()
            messageRU1 = messageRU.strip()
            messagePL1 = messagePL.strip()
            print("Reaches here!")
            recent_changes = None
            nice_cock_bro = getRC(recent_changes)
            nice_tits_bro = getRCRu(recent_changes)
            nice_balls_bro = getRCPl(recent_changes)
            if nice_cock_bro != None and nice_cock_bro != messageEN.content:
                print("letsss gooo")
                print(nice_cock_bro)
                await channelEN.send(nice_cock_bro)
            print(nice_tits_bro)
            print(messageRU.content)
            if nice_tits_bro != None and nice_tits_bro != messageRU.content:
                print("cyka blyat")
                await channelRU.send(nice_tits_bro)
            if nice_balls_bro != None and nice_balls_bro != messagePL.content:
                print("femboy")
                await channelPL.send(nice_balls_bro)
client = MyClient()
client.run('TOKEN')
