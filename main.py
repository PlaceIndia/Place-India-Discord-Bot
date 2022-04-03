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
    print("im alive and working!!(logged in as {0.user})".format(client))
    channle = await client.fetch_channel(credentials.channle_id)
    while True:
        Screenshoter()
        im = Image.open('yo.png')
        im = im.crop((0, 100, im.width-10, im.height))
        im.save('yo.png')
        await channle.send(f'our region as of {datetime.datetime.now()}', file=discord.File("yo.png"))
        print('sent ss')
        time.sleep(180)


@client.command()
async def test(ctx):
    await ctx.send("yes chef")

client.run(credentials.bot_token)
