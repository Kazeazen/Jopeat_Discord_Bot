'''
Author: James Thomason
Date: 2/4/2022
File: JopeatBot.py - A discord bot that simply repeats what the user Jodini#8531 says
'''
import discord
import random
import discord_jopeat_bot_token

# Make more silly commands for this bot

TOKEN = discord_jopeat_bot_token.TOKEN


client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    
    if message.author == client.user:
        return

    if str(message.author) == "Jodini#8531":
        stored_message = str(message.content)
        await message.channel.send(stored_message)
        return

    elif user_message.lower() in ["hello","hi","howdy","hey"]:
        await message.channel.send(f'Hello {username}, nyahhhhh')
        return

    elif user_message.lower() in ["bye","goodbye","cya","sayonara"]:
        await message.channel.send(f'See ya nyater! {username}')
        return

    elif user_message.lower() == "!random": # !random command
        response = f'This is your nyandom nyumber! {random.randrange(10000000)}'
        await message.channel.send(response)
        return

    elif user_message.lower() == "!catboy":
        response = f'Im just a catboy! I do nothing wrong! I love being a catboy nyahhhh'
        await message.channel.send(response)
        return

client.run(TOKEN)