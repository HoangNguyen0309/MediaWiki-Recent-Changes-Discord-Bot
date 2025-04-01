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
        channelEN = client.get_channel(CHANNEL TOKEN)
        channelRU = client.get_channel(CHANNEL TOKEN)
        channelPL = client.get_channel(CHANNEL TOKEN)
        while True:
            messageEN = await channelEN.fetch_message(channelEN.last_message_id)
            messageRU = await channelRU.fetch_message(channelRU.last_message_id)
            messagePL = await channelPL.fetch_message(channelPL.last_message_id)
            messageEN1 = messageEN.content.strip()
            messageRU1 = messageRU.content.strip()
            messagePL1 = messagePL.content.strip()
            print("Reaches here!")
            recent_changes = None
            nice_cock_bro = getRC(recent_changes).strip()
            nice_tits_bro = getRCRu(recent_changes).strip()
            nice_balls_bro = getRCPl(recent_changes).strip()
            if nice_cock_bro != None and nice_cock_bro != messageEN1:
                print("letsss gooo")
                print(nice_cock_bro)
                await channelEN.send(nice_cock_bro)
            if nice_tits_bro != None and nice_tits_bro != messageRU1:
                print("cyka blyat")
                await channelRU.send(nice_tits_bro)
            if nice_balls_bro != None and nice_balls_bro != messagePL1:
                print("femboy")
                await channelPL.send(nice_balls_bro)
client = MyClient()
client.run(TOKEN) 
