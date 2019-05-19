import requests
import time
import discord
import sys
import datetime

version = '1.1.2'

class config():
    serverip = '' # Input your server IP or hostname (e.g. mc.mywebsite.tld or 1.2.3.4)
    serverport = '' # Leave as 25565 unless you know what you're doing
    api = '' + serverip + '/' + serverport + '/' # DO NOT EDIT THIS LINE
    channel = '' # Enable Discord developer view then right-click the channel you want to send to
    token = '' # Set up a developer application
    updates = 5 # Time between updates of the API (keep in mind, it is cached and you will get ratelimited!)
    prevcur = 0 # Defining the variables as 0 before they're used
    runs = 0 # Defining the variables as 0 before they're used

class emojis():
    allow = '' # Indicates success
    deny = '' # Alternative error
    join = '' # User joined
    leave = '' # User left
    empty = '' # Empty server

client = discord.Client()

def timenow():
    return str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

try:
    if int(config.updates) == config.updates and int(config.prevcur) == config.prevcur and int(config.runs) == config.runs:
        print("[INFO  | " + timenow() + "] Checked variables successfully.")
except Exception as e:
    print("[ERROR | " + timenow() + "] Looks like you didn't leave the integer values as integers! Try again.")
    sys.exit(0) # Exit to prevent unexpected behaviour

print("[INFO  | " + timenow() + "] Starting Minecraft Discord Status v" + version + " by @maxicc :)")
print("[INFO  | " + timenow() + "] Something broken? Moan at me: https://git.io/fj810")
print("[INFO  | " + timenow() + "] Checking for new Discord commands and Minecraft player changes every " + str(config.updates) + " seconds.")

@client.event
async def on_message(message):
    dchannel = client.get_channel(int(config.channel))
    if message.content.startswith("!kill") or message.content.startswith("!shutdown") or message.content.startswith("!stop"):
        await dchannel.send(emojis.allow + " Shutting down!")
        time.sleep(5)
        sys.exit(0)


@client.event
async def on_ready():
    dchannel = client.get_channel(int(config.channel))
    print("[INFO  | " + timenow() + "] Logged in to Discord as "+ client.user.name + "#" + client.user.discriminator + " ("+ str(client.user.id) + ") successfully!")
    while True: # Keep looping!
        if config.api == '' or config.channel == '' or config.token == '': # Check the user has defined their variables properly
            print("[ERROR | " + timenow() + "] Please ensure you have set the variables correctly.")
            time.sleep(config.updates) # Don't spam the user (much)
            continue # Don't try and run the code below without the proper variables set

        players = "" # Empty the players variable
        try:
            response = requests.get(config.api).json() # Get the api response
        except Exception as e:
            print("[ERROR | " + timenow() + "] Problem with the API response")
            print("[ERROR | " + timenow() + "] " + str(e)) # This could be an error with the json decoding, accessing the internet or the api... lol
            time.sleep(600) # Don't try again for a while, give the user a chance to fix the error
            continue

        if "error" in response:
            print("[WARN  | " + timenow() + "] Your server is offline, or MineTools couldn't establish a connection to it.")
            await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Server is offline :("))
            await dchannel.send(emojis.deny + " Uh oh, your server is offline!")
            time.sleep(30)
            continue

        try:
            maxplayers = response['players']['max'] # Define the player amount variables using the json response
            curplayers = response['players']['online']
            onlplayers = response['players']['sample']
        except Exception as e:
            print("[ERROR | " + timenow() + "] Problem with the JSON response")
            print("[ERROR | " + timenow() + "] " + str(e))

        if curplayers != config.prevcur:
            await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Minecraft with " + str(curplayers) + "/" + str(maxplayers)))
            print("[INFO  | " + timenow() + "] Number of players has changed, Discord status updated")
        else:
            print("[INFO  | " + timenow() + "] Number of players has not changed, Discord status not updated")

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

        if config.runs == 0 and curplayers == 0: # If this is our first run and nobody is online...
            await dchannel.send(emojis.allow + " We're up and running! Nobody is online.")
        elif config.runs == 0 and curplayers != 0: # Or if this is our first run and there are people already online...
            await dchannel.send(emojis.allow + " We're up and running! " + players + " already online.")
        elif config.prevcur < curplayers: # Or if the previous player amount is less than the current...
            await dchannel.send(emojis.join + " Someone just logged on! " + players + " currently online.")
        elif curplayers < config.prevcur and curplayers == 0: # Or if the previous amount is more than the current and the current is now 0...
            await dchannel.send(emojis.empty + " Someone just logged off! Nobody is online anymore.")
        elif curplayers < config.prevcur and curplayers != 0: # Or if the previous amount is more than the current but people still online...
            await dchannel.send(emojis.leave + " Someone just logged off! " + players + " still online.")
        config.prevcur = curplayers # Replace prevcur with the current count
        time.sleep(config.updates) # Wait for x seconds (give the API a rest, we don't want to be ratelimited)
        config.runs = config.runs + 1 # Increment the run counter

try:
    client.run(config.token)
except Exception as e:
    print("[ERROR | " + timenow() + "] Could not start Discord client")
    print("[ERROR | " + timenow() + "] " + str(e))
