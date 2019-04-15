import discord
import requests

def commands_role(msg):
    msg = msg.replace("!role", "")
    if msg == "":
        await return(sendError("Usage: `!role <name> <session (1/3)>`"))
    else:
        msg = msg.split(" ")
        if len(msg) < 2:
            await message.channel.send(emed=sendError("Usage: `!role <name> <session (1/3)>`"))
        elif msg[2] == "1" or msg[2] == "3":
            r = requests.patch("https://discordapp.com/api/v6/guilds/%s/members/%s" %(message.guild.id, message.author.id), headers={"Authorization":"Bot %s" %TOKEN,"Content-Type":"application/json"}, data=json.dumps({"nick":msg[1]}))
            if msg[2] == "1":
                r2 = requests.patch("https://discordapp.com/api/v6/guilds/%s/members/%s" %(message.guild.id, message.author.id), headers={"Authorization":"Bot %s" %TOKEN,"Content-Type":"application/json"}, data=json.dumps({"roles":["487250811496431617"]}))
            elif msg[2] == "3":
                r2 = requests.patch("https://discordapp.com/api/v6/guilds/%s/members/%s" %(message.guild.id, message.author.id), headers={"Authorization":"Bot %s" %TOKEN,"Content-Type":"application/json"}, data=json.dumps({"roles":["522884365177585686"]}))
            if "Missing Permissions" in r.text:
                embed = discord.Embed(title=":x: Looks like I don't have permission to change your nickname :shrug:", description="", color=0xfc4444)
                await message.channel.send(embed=embed)
            if "Missing Permissions" in r2.text:
                embed = discord.Embed(title=":x: Looks like I don't have permission to change your role :shrug:", description="", color=0xfc4444)
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(title="<:correct:548988506496696341> Success!", description="", color=0x56ff67)
                await message.channel.send(embed=embed)
        else:
            await message.channel.send(emed=sendError("Valid sessions are 1 and 3"))
