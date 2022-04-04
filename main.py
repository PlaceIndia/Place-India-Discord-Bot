import discord
import time
from discord.ext import commands
import credentials  # local file with all credentials
from generator import Screenshoter, Screenshoter2
from PIL import Image
import datetime


client = commands.Bot(command_prefix="i ")
client.remove_command('help')


@client.event
async def on_ready():
    print("im alive and working!!(logged in as {0.user})".format(client))
    channle = await client.fetch_channel(credentials.channle_id)
    # channle2 = await client.fetch_channel(credentials.channle_id2)
    while True:
        Screenshoter()
        Screenshoter2()

        im = Image.open('yo.png')
        im = im.crop((0, 100, im.width-10, im.height))
        im.save('yo.png')
        im2 = Image.open('yo2.png')
        im2 = im2.crop((0, 100, im2.width-10, im2.height))
        im2.save('yo2.png')
        message = await channle.send(f'our region as of {datetime.datetime.now()}', files=[discord.File("yo.png"),discord.File("yo2.png")])
        await message.publish()
        print('sui')

        '''
        im2 = Image.open('yo2.png')
        im2 = im2.crop((0, 100, im2.width-10, im2.height))
        im2.save('yo.png')
        await channle2.send(f'our region as of {datetime.datetime.now()}', file=discord.File("yo2.png"))
        message2 = await channle2.history(limit=1).flatten()
        await message2[0].publish()

        print(f'sent at {datetime.dateime.now()}')
        '''
        time.sleep(180)


@client.command()
async def test(ctx):
    await ctx.send("yes chef")

client.run(credentials.bot_token)
