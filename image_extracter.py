import discord
import time
from discord.ext import commands
import credentials  # local file with all credentials
from generator import Screenshoter
from PIL import Image
import datetime

client = commands.Bot(command_prefix="i ")
client.remove_command('help')


@client.event
async def on_ready():
    c = 0
    print("im alive and working!!(logged in as {0.user})".format(client))
    channle = await client.fetch_channel(credentials.channle_id)
    async for message in channle.history(limit=None, oldest_first=True):
        for attachment in message.attachments:
            await attachment.save(f'images/{c}.png')
        # print(message)
        c += 1
    print(c)


@client.command()
async def test(ctx):
    await ctx.send("yes chef")

client.run(credentials.bot_token)
