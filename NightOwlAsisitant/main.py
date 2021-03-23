# bot.py
import os

import discord

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if 'wszystkiego najelpszego' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')


@client.event
async def on_message(message):
    if 'NightOwlAsistant' == message.content:
        await message.channel.send("W czyms pomóc?")


@client.event
async def on_message(message):
    mention = f'<@!{client.user.id}>'
    if mention in message.content:
        await message.channel.send("W czymś pomóc?")

@client.event
async def on_message(message):
        await message.channel.send("Link do sieci na hamahi: https://secure.logmein.com/i?l=en&c=01_4oxy4bpw7w0bfuj4k4hz4g74tsj1z1oz7run2")


@client.event
async def on_message(message):
    if '!ip' == message.content:
        emoji = '✔'
        await message.add_reaction(emoji)
        await message.channel.send('Ip servera minecraft: 25.67.242.145:12345')
        await message.channel.send('Zapraszamy!')
client.run('ODIyMTgyNjM4NDQ5NTkwMzQy.YFOjQA.7ceoAHwn8fmoJheI2ykfP34Olg4')
