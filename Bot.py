import discord
import asyncio
import datetime as d
import os
import json
import sqlite3

from discord.ext import commands
from Secrets import BOT_VERSION
from Secrets import BOT_TOKEN


def prefix(client, message):
    datenbank = sqlite3.connect('DatenBank.sqlite')
    cursor = datenbank.cursor()
    cursor.execute(f'SELECT prefix FROM Prefixe WHERE guild_id = {message.guild.id}')
    result = cursor.fetchone()

    if result is None:
        return
    else:
        return result

client = commands.Bot(command_prefix=prefix, case_insensitive=True)
client.remove_command('help')

s = set([])
members = set([])


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
        for server in client.guilds:
            s.add(server.id)

        await asyncio.sleep(2)
        await client.change_presence(activity=discord.Streaming(name=f'Auf {str(len(s))} Servern!', url='https://www.twitch.tv/#'))
        await asyncio.sleep(60)

        for guild in client.guilds:
            for member in guild.members:
                members.add(member.id)

        await asyncio.sleep(2)
        await client.change_presence(activity=discord.Streaming(name=f'Mit {str(len(members))} Usern!', url='https://www.twitch.tv/#'))
        await asyncio.sleep(60)


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
        print(f'{e[:-3]} Command wurde geladen!')


client.run(BOT_TOKEN)
