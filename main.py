# import
import discord
from discord.ext import commands
import os

# intents
intents = discord.Intents.all()
intents.members = True

# command prefix
client = commands.Bot(command_prefix='.')

# load/unload files 

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

with open("data.txt", "r") as myfile:
    data = myfile.read().splitlines()

# client.run(BOT_TOKEN)