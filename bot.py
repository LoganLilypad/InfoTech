import requests
import discord
import json


TOKEN = open("../conf.txt").read()

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
    elif message.content.startswith("!q"):
        msg = message.content.split(" ")
        

@client.event
async def on_ready():
    print("I'm ready!!!")

client.run(TOKEN)
