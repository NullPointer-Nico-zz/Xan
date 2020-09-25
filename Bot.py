import re
import discord
import asyncio
import datetime as d
import os
import sqlite3

from discord.ext import commands
from Secrets import BOT_TOKEN
from googletrans import Translator

def trans(message, text=''):
    db = sqlite3.connect("DatenBank.sqlite")
    cursor = db.cursor()
    translator = Translator()
    cursor.execute(f'SELECT lang FROM lang WHERE guild_id = {message.guild.id}')
    sprache = cursor.fetchone()

    if sprache is None:
        cursor.execute('INSERT INTO lang(guild_id, lang) VALUES(?, ?)', (message.guild.id, "en"))
        db.commit()
        return 
    else:
        end = translator.translate(text, dest=sprache[0]).text
        return end

def getPrefix(message):
    datenbank = sqlite3.connect('DatenBank.sqlite')
    cursor = datenbank.cursor()
    cursor.execute(f'SELECT prefix FROM Prefixe WHERE guild_id = {message.guild.id}')
    result = cursor.fetchone()
    return result[0]
        

def prefix(client, message):
    datenbank = sqlite3.connect('DatenBank.sqlite')
    cursor = datenbank.cursor()
    cursor.execute(f'SELECT prefix FROM Prefixe WHERE guild_id = {message.guild.id}')
    result = cursor.fetchone()

    if result is None:
        cursor.execute('INSERT INTO Prefixe (guild_id, prefix) VALUES (?, ?)', (message.guild.id, "$"))
        datenbank.commit()
        return
    else:
        return result


client = commands.Bot(command_prefix=prefix, case_insensitive=True)
client.remove_command('help')

s = set([])
members = set([])

todo_ids = set([])
todos = set([])

@client.event
async def on_ready():
    print('<====Xan====>')
    print(f'Name: {client.user.name}')
    print(f'ID: {client.user.id}')
    print('<====Xan====>')
    await Activity_Task()


start_time = d.datetime.utcnow()


async def Activity_Task():
    while True:
        s.clear()

        for server in client.guilds:
            s.add(server.id)

        await asyncio.sleep(2)
        await client.change_presence(
            activity=discord.Streaming(name=f'Auf {str(len(s))} Servern!', url='https://www.twitch.tv/#'))
        await asyncio.sleep(28)

        members.clear()

        for guild in client.guilds:
            for member in guild.members:
                members.add(member.id)

        await asyncio.sleep(2)
        await client.change_presence(
            activity=discord.Streaming(name=f'Mit {str(len(members))} Usern!', url='https://www.twitch.tv/#'))
        await asyncio.sleep(28)


for admin in os.listdir('./Admin_Commands'):
    if admin.endswith('.py'):
        client.load_extension(f'Admin_Commands.{admin[:-3]}')
        print(f'{admin[:-3]} Command wurde geladen!')

for allgemeine in os.listdir('./Allgemeine_commands'):
    if allgemeine.endswith('.py'):
        client.load_extension(f'Allgemeine_commands.{allgemeine[:-3]}')
        print(f'{allgemeine[:-3]} Command wurde geladen!')

for mod in os.listdir('./Mod_Commands'):
    if mod.endswith('.py'):
        client.load_extension(f'Mod_Commands.{mod[:-3]}')
        print(f'{mod[:-3]}  Command wurde geladen!')

for owner in os.listdir('./Owner_Commands'):
    if owner.endswith('.py'):
        client.load_extension(f'Owner_Commands.{owner[:-3]}')
        print(f'{owner[:-3]} Command wurde geladen!')

for e in os.listdir('./events'):
    if e.endswith('.py'):
        client.load_extension(f'events.{e[:-3]}')
        print(f'{e[:-3]} event wurde geladen!')

for fun in os.listdir('./fun'):
    if fun.endswith('.py'):
        client.load_extension(f'fun.{fun[:-3]}')
        print(f'{fun[:-3]} Command wurde geladen!')

client.run(BOT_TOKEN)
