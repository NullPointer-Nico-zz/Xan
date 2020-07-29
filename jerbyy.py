import discord
import asyncio


from discord.ext import commands


client = commands.Bot(command_prefix='!', case_insensitive=True)
client.remove_command('help')


@client.command()
async def dm(ctx):
    for member in ctx.guild.members:
        try:
            await member.send('Dies ist ein Test für ein Freund')
        except:
            print(f'User {member.name} hat seine Dms closed!')


@client.event
async def on_guild_remove(guild):
    print(f'Der Bot hat den Server {guild.name} verlassen!')


client.run('NzM1NjIyNjc3OTcyMTIzNzI4.Xxi8Bw.MXRFK1C9AFqTyLyjz95wFrwfSoU')
