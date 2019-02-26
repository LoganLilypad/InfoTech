import requests
from random import randint as rand
import os
import discord
import json
from time import sleep
from textwrap import wrap


TOKEN = json.loads(open("../config.json").read().replace("\n", ""))["bot_token"]
TOKEN_GIPHY = json.loads(open("../config.json").read().replace("\n", ""))["giphy_token"]
TOKEN_IMGUR = json.loads(open("../config.json").read().replace("\n", ""))["imgur_token"]

q = open("General.txt", "r").read().split("\n")
a = ""

def sendError(m):
    embed = discord.Embed(title="Error", description=m, color=0xfc4444)
    return embed

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        embed = discord.Embed(title="Help", description="List of the available commands:\n", color=0x609dff)
        embed.add_field(name="!help", value="Shows this menu", inline=True)
        embed.add_field(name="!q <type>", value="Asks a random question of the said category", inline=True)
        embed.add_field(name="!a <answer>", value="Answer a question (case does not matter)", inline=True)
        embed.add_field(name="!gif <query>", value="Search for a gif from Giphy", inline=True)
        embed.add_field(name="!img <query>", value="Search for an image from Imgur", inline=True)
        embed.add_field(name="!del <message ID>", value="Deletes a message by ID", inline=True)
        embed.add_field(name="!contribute", value="Wanna help with this bot? Run this command", inline=True)
        await message.channel.send(embed=embed)
    elif message.content.startswith("!del"):
        msg = message.content.replace("!del", "")
        if msg == "":
            await message.channel.send(embed=sendError("Usage: `!del <message ID>`"))
        else:
            r = requests.delete("https://discordapp.com/api/v6/channels/487233747008094229/messages/%s" %message.id, headers={"Authorization":"Bot %s" %TOKEN,"Content-Type":"application/json"})
            r = requests.delete("https://discordapp.com/api/v6/channels/487233747008094229/messages/%s" %msg, headers={"Authorization":"Bot %s" %TOKEN,"Content-Type":"application/json"})
    

    
    elif message.content.startswith("!contribute"):
        embed = discord.Embed(title="If you would like to help improve me, click here:", description="https://github.com/LoganLilypad/InfoTech\n*Don't worry, you dont need to code to help :)*", color=0x38ff5f)
        await message.channel.send(embed=embed)
    elif message.content.startswith("!exec"):
        msg = message.content.replace("!exec", "")
        if msg == "":
            await message.channel.send(embed=sendError("Usage: `!exec <Linux command>`"))
        else:
            if msg == "sudo reboot":
                embed = discord.Embed(title="Server", description="Restarting the server...", color=0xfc4444)
                await message.channel.send(embed=embed)
            os.system("%s > exec.txt" %msg)
            if open("exec.txt", "r").read() != "":
                await message.channel.send(open("exec.txt", "r").read())
            else:
                await message.channel.send(embed=sendError("Either the command is unknown, output is too long or there was a general error"))
    elif message.content.startswith("!gif"):
        msg = message.content.replace("!gif", "")
        if msg == "":
            await message.channel.send(embed=sendError("You need to define some text to use this!"))
        else:
            t = rand(0, 11)
            r = r = requests.get("http://api.giphy.com/v1/gifs/translate?api_key=%s&s=%s&weirdness=%s" %(TOKEN_GIPHY, msg.replace(" ", "+"), t))
            data = json.loads(r.text)
            embed = discord.Embed()
            embed.set_image(url=data["data"]["images"]["downsized_large"]["url"])
            await message.channel.send(embed=embed)
    elif message.content.startswith("!img"):
        msg = message.content.replace("!img", "")
        if msg == "":
            await message.channel.send(embed=sendError("You need to define some text to use this!"))
        else:
            r = requests.get("https://api.imgur.com/3/gallery/t/%s" %msg.replace(" ", "%20"), headers={"Authorization":"Client-ID %s" %TOKEN_IMGUR})
            data = json.loads(r.text)
            t = rand(0, len(data["data"]["items"]))
            embed = discord.Embed()
            embed.set_image(url=data["data"]["items"][t]["images"][0]["link"])
            await message.channel.send(embed=embed)
    elif message.content.startswith("!insult"):
        msg = message.content.replace("!insult ", "")
        if msg == "":
            await message.channel.send(embed=sendError("You need to define the amount of insults to generate!"))
        else:
            if int(msg) <= 25:
                embed = discord.Embed(title="Generating %s insult(s)..." %msg, description="", color=0x609dff)
                await message.channel.send(embed=embed)
                out = ""
                for i in range(int(msg)):
                    print("Yes")
                    r = requests.get("https://insult.mattbas.org/api/insult")
                    out += "%s\n" %r.text
                embed = discord.Embed(title="Insults:" %msg, description="%s" %out, color=0x38ff5f)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(embed=sendError("Insult count must be less than 26!")
            

            
    elif message.content.startswith("!q"):
        global a
        global q
        if a == "":
            msg = message.content.replace("!q ", "").lower()
            if msg == "g":
                ask = rand(0, len(q))
                qs = q[ask].split("||")
                if len(qs) == 6:
                    a = qs[len(qs) - 1]
                    embed = discord.Embed(title=qs[0], description="**A** %s\n**B** %s\n**C** %s\n**D** %s\n" %(qs[1], qs[2], qs[3], qs[4]), color=0x609dff)
                    embed.set_thumbnail(url="https://www.emoji.co.uk/files/google-emojis/symbols-android/8046-black-question-mark-ornament.png")
                    await message.channel.send(embed=embed)
                else:
                    a = qs[len(qs) - 1]
                    embed = discord.Embed(title=qs[0], description="**A** %s\n**B** %s\n**C** %s\n**D** %s\n**E** %s" %(qs[1], qs[2], qs[3], qs[4], qs[5]), color=0x609dff)
                    embed.set_thumbnail(url="https://www.emoji.co.uk/files/google-emojis/symbols-android/8046-black-question-mark-ornament.png")
                    await message.channel.send(embed=embed)
            elif msg == "h":
                await message.channel.send(embed=sendError("There are no questions available for hardware yet. Maybe you could add some?"))
            elif msg == "n":
                t = rand(0, 2)
                if t == 0:
                    cq = open("Ports.txt", "r").read().split("\n")
                    rq = cq[rand(0, len(cq) + 1)]
                    rq = rq.split("||")
                    t = rand(0, 2)
                    if t == 0:
                        embed = discord.Embed(title="What port is dedicated to **%s**?" %rq[1], description="", color=0x609dff)
                        embed.set_thumbnail(url="https://www.emoji.co.uk/files/google-emojis/symbols-android/8046-black-question-mark-ornament.png")
                        await message.channel.send(embed=embed)
                        a = rq[0]
                    else:
                        embed = discord.Embed(title="What protocol is dedicated to the port **%s**?" %rq[0], description="", color=0x609dff)
                        embed.set_thumbnail(url="https://www.emoji.co.uk/files/google-emojis/symbols-android/8046-black-question-mark-ornament.png")
                        await message.channel.send(embed=embed)
                        a = rq[1]
            elif msg == "t":
                await message.channel.send(embed=sendError("There are no questions available for troubleshooting yet. Maybe you could add some?"))
            else:
                await message.channel.send(embed=sendError("Usage: `!q <(g)eneral/(h)ardware/(n)etworking/(t)roubleshooting>`"))
        else:
            await message.channel.send(embed=sendError("You must answer the previous question to move on!"))
    elif message.content.startswith("!a"):
        if a != "":
            msg = message.content.replace("!a ", "")
            if msg.lower() == a.lower():
                embed = discord.Embed(title="<:correct:548988506496696341> Correct!", description="", color=0x56ff67)
                await message.channel.send(embed=embed)
                a = ""
            else:
                embed = discord.Embed(title=":x: Incorrect, the answer was **%s**" %a, description="", color=0xfc4444)
                await message.channel.send(embed=embed)
                a = ""
        else:
            await message.channel.send(embed=sendError(":x: There is no question to answer!"))
            
        

@client.event
async def on_ready():
    print("Ready")

client.run(TOKEN)
