import requests
import time
import discord

# Hello! This version DOES connect to Discord!

# CUSTOM OPTIONS GO HERE!
apiurl = '' # Use api.minetools.eu
discordchannel = '' # Enable Discord developer options then right-click the channel you want to send to
discordtoken = '' # Set up a developer application using discordapp.com/developers/applications
updates = 30 # Time between updates of the API (keep in mind, it is cached and you will get ratelimited!)

prevcur = 0 # Defining the variables as 0 before they're used
runs = 0 # Defining the variables as 0 before they're used

client = discord.Client()

@client.event
async def on_ready():
    global runs
    global prevcur
    global apiurl
    global discordchannel
    global discordtoken

    channel = client.get_channel(int(discordchannel))
    print("Logged in to Disord successfully!")
    while True: # Keep looping!
        if apiurl == '' or discordchannel == '' or discordtoken == '': # Check the user has defined their variables properly
            print("Set your variables (look at the top of the python file)")
            time.sleep(10) # Don't spam the user (much)
            continue # Don't try and run the code below without the proper variables set

        players = "" # Empty the players variable
        try:
            response = requests.get(apiurl).json() # Get the api response
        except Exception as e:
            print("Looks like there's something wrong with the API server! Did you use api.minetools.eu? If so, try again in a while.")
            print("Here's the error from requests: " + str(e)) # This could be an error with the json decoding, accessing the internet or the api... lol
            time.sleep(600) # Don't try again for a while, give the user a chance to fix the error
            continue
        try:
            maxplayers = response['players']['max'] # Define the player amount variables using the json response
            curplayers = response['players']['online']
            onlplayers = response['players']['sample']
        except Exception as e:
            print("Looks like something went wrong with the json decoding. Are you using the right API server?")
            print("Here's the error from requests: " + str(e))

        if curplayers != prevcur:
            activity = discord.Game(name="Minecraft with " + str(curplayers) + "/" + str(maxplayers))
            await client.change_presence(status=discord.Status.idle, activity=activity)
            print("Updated Discord presence")
        else:
            print("No need to update Discord presence, players hasn't changed")

        for i in range(curplayers): # For all players currently online...
            if i+1 == curplayers and curplayers != 1: # If we are at the last player, and there is more than 1 player online...
                players = players + " and " + str(onlplayers[i]['name']) # Conclude the string with 'and <player>' to be gramatically correct :)
            elif i == 0: # If we are the first player...
                players = str(onlplayers[i]['name']) # Don't add 'and' or a comma before the name, we are the first in the list
            else: # Otherwise, we must be somewhere in the middle...
                players = players + ", " + str(onlplayers[i]['name']) # Add a comma then the player name to the string

        if curplayers == 1: # If there's only one player online
            players = players + " is" # Use is
        else: # Or if there is more than 1
            players = players + " are" # Use are

        if runs == 0 and curplayers == 0: # If this is our first run and nobody is online...
            await channel.send("First run. Nobody is online.")
        elif runs == 0 and curplayers != 0: # Or if this is our first run and there are people already online...
            await channel.send("First run. " + players + " already online.")
        elif prevcur < curplayers: # Or if the previous player amount is less than the current...
            await channel.send("Someone just logged on! " + players + " currently online.")
        elif curplayers < prevcur and curplayers == 0: # Or if the previous amount is more than the current and the current is now 0...
            await channel.send("Someone just logged off! Nobody is online anymore.")
        elif curplayers < prevcur and curplayers != 0: # Or if the previous amount is more than the current but people still online...
            await channel.send("Someone just logged off! " + players + " still online.")
        else: # Or if there was no change at all...
            print("Debugging test. There was no change in player count.")
        prevcur = curplayers # Replace prevcur with the current count
        time.sleep(updates) # Wait for x seconds (give the API a rest, we don't want to be ratelimited)
        runs = runs + 1 # Increment the run counter

try:
    client.run(discordtoken)
except Exception as e:
    print("Something went wrong while starting the Discord bot! Have you set your variables correctly?")
    print("Here's the error message from Discord.py: " + str(e))
