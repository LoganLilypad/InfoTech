import requests
from random import randint as rand
import discord
import json


TOKEN = open("../conf.txt").read().replace("\n", "")

q = open("General.txt", "r").read().split("\n")

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
        msg = message.content.replace("!q ", "").lower()
        if msg == "g":
            ask = rand(0, len(q))
            a = q[ask][len(q[ask]) - 1]
            await message.channel.send(embed=discord.Embed(title=q[ask], description=str(q[ask]), color=0x609dff))
        else:
            await message.channel.send(embed=sendError("Usage: `!q <hardware/networking/mobdev/trbsht>`"))
            
        

@client.event
async def on_ready():
    print("Ready")

client.run(TOKEN)
