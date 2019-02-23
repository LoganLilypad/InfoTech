import requests
from random import randint as rand
import discord
import json


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
        embed.add_field(name="!q <type> [number]", value="Asks a random question if [number] is not supplied", inline=True)
        await message.channel.send(embed=embed)
    elif message.content == "!contribute":
        embed = discord.Embed(title="If you would like to help create this bot, click here:", description="https://github.com/LoganLilypad/InfoTech You will need a Github account to make any changes", color=0x38ff5f)
        await message.channel.send(embed=embed)
    elif "!q" in message.content:
        global a
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
            else:
                await message.channel.send(embed=sendError("Usage: `!q <hardware/networking/mobdev/trbsht>`"))
        else:
            await message.channel.send(embed=sendError("You must answer the previous question to move on!"))
    elif "!a" in message.content:
        if a != "":
            msg = message.content.replace("!a ", "")
            if msg[1] == a.lower():
                await message.channel.send("Correct! <:correct:548988506496696341>")
                a = ""
            else:
                await message.channel.send("Incorrect, the answer was **%s** <:incorrect:548988506467336192>" %a)
                a = ""
        else:
            await message.channel.send(embed=sendError("There is no question to answer! <:incorrect:548988506467336192>"))
            
        

@client.event
async def on_ready():
    print("Ready")

client.run(TOKEN)
