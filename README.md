# Minecraft Discord Status

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2eb2f5bcda814bd5b8d6e38dcbf5bd82)](https://app.codacy.com/app/maxicc/minecraft-discord-status?utm_source=github.com&utm_medium=referral&utm_content=maxicc/minecraft-discord-status&utm_campaign=Badge_Grade_Settings)

![version](https://img.shields.io/badge/version-1.1.2-yellow.svg)
![made-with-python](https://img.shields.io/badge/Made%20with-Python-informational.svg)
![python-versions](https://img.shields.io/badge/python-3.5%20|%203.6%20|%203.7-critical.svg)
![MIT-license](https://img.shields.io/badge/license-MIT-green.svg)
![badges](https://img.shields.io/badge/obsessed%20with%20badges%3F-true-blueviolet.svg)

###### Nobody else will ever use this but it was fun to make the project from start/planning to finish/publishing and documenting I guess??

## About

This is a python script to run a Discord bot that updates a channel with the status of who's online.
It also uses Discord Presence to show how many people are online in the members sidebar.

I made this for fun in a couple of hours for my friend's smp, thought it could be useful to anyone else if they happen to stumble upon it ¯\_(ツ)_/¯

If you do use it, make sure you have the **rewrite** version of discord.py - not the old async version! ~~Proper readme/documentation incoming depending on how bored I get revising for exams~~ (Turns out I'm more bored than expected)

## Screenshots
![Server Status (bot) is online. 0/3 players are online.](https://i.imgur.com/gVLLibU.png)
![Server Status (bot) updating users on who's online.](https://i.imgur.com/wlTBBaM.png)

## Prerequisites
**You need to be ready to run this Python script.**
1. Clone this repo using `git clone https://github.com/maxicc/minecraft-discord-status.git` or whatever weird git client you use
2. Make sure you have the right requirements installed. You can check using `pip install -r requirements.txt`.

**You need a Discord server, channel, application and a bot user.**
*It sounds a lot more complicated than it is!*

 1. Go to [Discord's developer portal](https://www.discordapp.com/developers/applications).
 2. Hit **New Application** and give it a nice name - this will be your bot's name so make it presentable! [(img)](https://i.imgur.com/Kt8eDYN.png)
 3. Customise your application as necessary. [(img)](https://i.imgur.com/tRkXrzT.png)
 4. In the Bot submenu (navigate using the left sidebar), hit **Add Bot** and then confirm the dialog box. [(img)](https://i.imgur.com/Cw6sM22.png)
 5. **DO NOT GIVE OUT YOUR BOT TOKEN TO ANYONE PLEASE FOR THE LOVE OF GOD.**
 6. Now, go to the Oauth2 section and in the URL generator section, tick the "bot" scope. Then, copy the URL in the text box below and go to it in a new tab. [(img)](https://i.imgur.com/QEDd7xB.png)
 7. Select the server you want your bot to join, then accept the permissions prompt. You'll need **Manage Server** permissions wherever you want to add it - you can't just add it to any random server. [(img)](https://i.imgur.com/BW1IgeN.png)
 8. Copy your token (**the one you shouldn't give out to anyone, remember?**) and open the `with-discord.py` file. Paste it between the two `'` quote marks next to `discordtoken`.
 9. In your Discord settings, go to **Appearance** then toggle on **Developer Mode**. *This doesn't change anything about how your Discord app works, it just allows extra options for when you're developing stuff with the Discord API.* [(img)](https://i.imgur.com/fspwlrk.png)
 10. Almost there! Now, go to the server you authorised your bot in and find the channel you want to send the login messages to. Right-click this channel in the left sidebar and click **Copy ID**. Paste this ID between the two `'` quote marks next to `discordchannel` in the `with-discord.py` file. [(img)](https://i.imgur.com/jOdsPuf.png)

**You need a Minecraft server and you need to set it up with the MineTools API.**
*This also sounds complicated...*

 1. You should already have a Minecraft server ready to go... if you don't idk why you're here. Make sure your server is online and connectable.
 2. Get your server's IP/hostname and port number (if you never connect with a specific port, it's 25565).
 3. Substitute your server IP/hostname and port number in to the MineTools base URL (`https://api.minetools.eu/ping/<ip/hostname>/<port>`) and visit it in your browser.
 4. The page might look a bit confusing (this is called JSON), but all you need to make sure is that it shows information that looks like it relates to your server; if it says `Errno xyz` or any sort of error, you've got the wrong IP/hostname or port or your server is offline.
 5. Once you have this URL working, copy it from your browser and paste it in between the two `'` quote marks next to `url`.

**You're done! 🎉**
Now, just run the bot and it should work!
