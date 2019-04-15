import discord
import requests

def sendError(m):
    embed = discord.Embed(title="Error", description=m, color=0xfc4444)
    return embed

def commands_role(msg):
    msg = msg.replace("!role", "")
    if msg == "":
        return sendError("Usage: `!role <name> <session (1/3)>`")
    else:
        #Really need to either delete this, or actually find how to assign roles/nicknames using Discord Rewrite; directly using the API is ugly
        msg = msg.split(" ")
        if len(msg) < 2:
            return emed=sendError("Usage: `!role <name> <session (1/3)>`")
        elif msg[2] == "1" or msg[2] == "3":
            r = requests.patch("https://discordapp.com/api/v6/guilds/%s/members/%s" %(message.guild.id, message.author.id), headers={"Authorization":"Bot %s" %TOKEN,"Content-Type":"application/json"}, data=json.dumps({"nick":msg[1]}))
            if msg[2] == "1":
                r2 = requests.patch("https://discordapp.com/api/v6/guilds/%s/members/%s" %(message.guild.id, message.author.id), headers={"Authorization":"Bot %s" %TOKEN,"Content-Type":"application/json"}, data=json.dumps({"roles":["487250811496431617"]}))
            elif msg[2] == "3":
                r2 = requests.patch("https://discordapp.com/api/v6/guilds/%s/members/%s" %(message.guild.id, message.author.id), headers={"Authorization":"Bot %s" %TOKEN,"Content-Type":"application/json"}, data=json.dumps({"roles":["522884365177585686"]}))
            if "Missing Permissions" in r.text:
                embed = discord.Embed(title=":x: Looks like I don't have permission to change your nickname :shrug:", description="", color=0xfc4444)
                return embed
            if "Missing Permissions" in r2.text:
                embed = discord.Embed(title=":x: Looks like I don't have permission to change your role :shrug:", description="", color=0xfc4444)
                return embed
            else:
                embed = discord.Embed(title="<:correct:548988506496696341> Success!", description="", color=0x56ff67)
                return embed
        else:
            return sendError("Valid sessions are 1 and 3")
