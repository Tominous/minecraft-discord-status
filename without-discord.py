import requests
import time

# Hello! This version just outputs to the console. It doesn't connect to Discord. I made it for testing.

# CUSTOM OPTIONS GO HERE!
apiurl = '' # Use api.minetools.eu
updates = 30 # Time between updates of the API (keep in mind, it is cached and you will get ratelimited!)

prevcur = 0 # Defining the variables as 0 before they're used
runs = 0 # Defining the variables as 0 before they're used

while True: # Keep looping!
    if apiurl == '' or discordchannel == '' or discordtoken == '': # Check the user has defined their variables properly
        print("Set your variables (look at the top of the python file)")
        time.sleep(10) # Don't spam the user (much)
        continue # Don't try and run the code below without the proper variables set

    players = "" # Empty the players variable
    response = requests.get(apiurl).json() # Get the api response
    maxplayers = response['players']['max'] # Define the player amount variables using the json response
    curplayers = response['players']['online']
    onlplayers = response['players']['sample']

    print("Playing Minecraft with " + str(curplayers) + "/" + str(maxplayers)) # Set the discord playing status

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
        print("First run. Nobody is online.")
    elif runs == 0 and curplayers != 0: # Or if this is our first run and there are people already online...
        print("First run. " + players + " already online.")
    elif prevcur < curplayers: # Or if the previous player amount is less than the current...
        print("Someone just logged on! " + players + " currently online.")
    elif curplayers < prevcur and curplayers == 0: # Or if the previous amount is more than the current and the current is now 0...
        print("Someone just logged off! Nobody is online anymore.")
    elif curplayers < prevcur and curplayers != 0: # Or if the previous amount is more than the current but people still online...
        print("Someone just logged off! " + players + " still online.")
    else: # Or if there was no change at all...
        print("Debugging test. There was no change in player count.")
    prevcur = curplayers # Replace prevcur with the current count
    time.sleep(updates) # Wait for 30 seconds (give the API a rest, we don't want to be ratelimited)
    runs = runs + 1 # Increment the run counter
