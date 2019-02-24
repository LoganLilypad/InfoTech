import requests
from random import randint as rand
import os
import discord
import json
from textwrap import wrap


TOKEN = open("../conf.txt").read().replace("\n", "")

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
        embed.add_field(name="!contribute", value="Wanna help with this bot? Run this command", inline=True)
        await message.channel.send(embed=embed)
    elif message.content == "!contribute":
        embed = discord.Embed(title="If you would like to help improve me, click here:", description="https://github.com/LoganLilypad/InfoTech\n*Don't worry, you dont need to code to help :)*", color=0x38ff5f)
        await message.channel.send(embed=embed)
    elif "!exec" in message.content:
        msg = message.content.replace("!exec ", "")
        os.system("%s > exec.txt" %msg)
        if open("exec.txt", "r").read() != "":
            out = wrap(open("exec.txt", "r").read(), 1500)
            for i in range(len(out)):
                await message.channel.send(out[i])
        else:
            await message.channel.send(embed=sendError("Either the command is unknown, output is too long or there was a general error"))
    elif "!q" in message.content:
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
                    rq = cq[rand(0, len(q) + 1)]
                    await message.channel.send(str(rq))
            elif msg == "t":
                await message.channel.send(embed=sendError("There are no questions available for troubleshooting yet. Maybe you could add some?"))
            else:
                await message.channel.send(embed=sendError("Usage: `!q <(g)eneral/(h)ardware/(n)etworking/(t)roubleshooting>`"))
        else:
            await message.channel.send(embed=sendError("You must answer the previous question to move on!"))
    elif "!a" in message.content:
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
