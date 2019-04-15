import discord

def sendError(m):
    embed = discord.Embed(title="Error", description=m, color=0xfc4444)
    return embed

def command_help():
    embed = discord.Embed(title="Help", description="List of the available commands:\n", color=0x609dff)
    embed.add_field(name="!help", value="Shows this menu", inline=False)
    embed.add_field(name="!role <name> <session (1/3)>", value="Setup your name and session so you can talk in the Discord", inline=False)
    embed.add_field(name="!q <type>", value="Asks a random question of the said category", inline=False)
    embed.add_field(name="!a <answer>", value="Answer a question (case does not matter)", inline=False)
    embed.add_field(name="!gif <query>", value="Search for a gif from Giphy", inline=False)
    embed.add_field(name="!img <query>", value="Search for an image from Imgur", inline=False)
    embed.add_field(name="!del <message ID>", value="Deletes a message by ID", inline=False)
    embed.add_field(name="!contribute", value="Wanna help with this bot? Run this command", inline=False)
    return embed
