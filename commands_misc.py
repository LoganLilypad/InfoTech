import discord
import requests

def sendError(m):
    embed = discord.Embed(title="Error", description=m, color=0xfc4444)
    return embed

def commands_role(msg):
    return sendError("This command is currently disabled")
