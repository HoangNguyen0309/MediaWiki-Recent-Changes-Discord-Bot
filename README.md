# MediaWiki-Recent-Changes-Discord-Bot

Using the MediaWiki API, the bot automatically gets recent changes to the wiki every 10 seconds and outputs a line with the following format: Title of page changed + time + username + comments

d-bot.py contains the bot for discord <br>
bot.py contains the code to get recent changes using MediaWiki api. <br>
Bot works by comparing last text message in channel and compare them to most recent change to the wiki. <br>
