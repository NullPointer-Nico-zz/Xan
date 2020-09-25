import discord
import sqlite3 as sql

from discord.ext import commands
from discord.ext.commands import Cog
from Bot import trans
from Bot import getPrefix


class Sprache(Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True, case_insensitive=True)
    async def setlang(self, ctx):
        if not ctx.message.author.guild_permissions.administrator:
            no_permission = discord.Embed(
                title=trans(ctx.message, 'Dazu hast du keine Berechtigung!'), 
                description=f'{trans(ctx.message, "Sie haben nicht die folgende Berechtigung")}:\n`Administrator`', 
                color=discord.Color.dark_red())
            no_permission.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
            await ctx.send(embed=no_permission)

        embed = discord.Embed(title=trans(ctx.message, 'Sprache'), colour=ctx.message.author.colour)
        embed.add_field(name=trans(ctx.message, 'Sprache Ändern zu Deutsch'), value=f'`{getPrefix(ctx.message)}setlang de`', inline=False)
        embed.add_field(name=trans(ctx.message, 'Sprache Ändern zu Englisch'), value=f'`{getPrefix(ctx.message)}setlang en`', inline=False)
        await ctx.send(embed=embed)

    @setlang.command()
    async def de(self, ctx):
        datenbank = sql.connect('DatenBank.sqlite')
        cursor = datenbank.cursor()

        if not ctx.message.author.guild_permissions.administrator:
            no_permission = discord.Embed(
                title=trans(ctx.message, 'Dazu hast du keine Berechtigung!'), 
                description=f'{trans(ctx.message, "Sie haben nicht die folgende Berechtigung")}:\n`Administrator`', 
                color=discord.Color.dark_red())
            no_permission.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
            await ctx.send(embed=no_permission)
            return True

        cursor.execute(f'SELECT lang FROM lang WHERE guild_id = {ctx.guild.id}')
        result = cursor.fetchone()

        if result is None:
            cursor.execute(f'INSERT INTO lang(guild_id, lang) VALUES(?, ?)', (ctx.guild.id, "de"))
        else:
            cursor.execute(f'UPDATE lang SET lang = ? WHERE guild_id = ?', ("de", ctx.guild.id))

        datenbank.commit()

        embed = discord.Embed(title=trans(ctx.message, "Neue Sprache"), description=trans(ctx.message, '`Deutsch | de`'), color=discord.Color.dark_magenta())
        await ctx.send(embed=embed)

        cursor.close()
        datenbank.close()

    @setlang.command()
    async def en(self, ctx):
        datenbank = sql.connect('DatenBank.sqlite')
        cursor = datenbank.cursor()

        if not ctx.message.author.guild_permissions.administrator:
            no_permission = discord.Embed(
                title=trans(ctx.message, 'Dazu hast du keine Berechtigung!'), 
                description=f'{trans(ctx.message, "Sie haben nicht die folgende Berechtigung")}:\n`Administrator`', 
                color=discord.Color.dark_red())
            no_permission.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
            await ctx.send(embed=no_permission)
            return True

        cursor.execute(f'SELECT lang FROM lang WHERE guild_id = {ctx.guild.id}')
        result = cursor.fetchone()

        if result is None:
            cursor.execute(f'INSERT INTO lang(guild_id, lang) VALUES(?, ?)', (ctx.guild.id, "en"))
        else:
            cursor.execute(f'UPDATE lang SET lang = ? WHERE guild_id = ?', ("en", ctx.guild.id))

        datenbank.commit()

        embed = discord.Embed(title=trans(ctx.message, "Neue Sprache"), description=trans(ctx.message, '`Englisch | en`'), color=discord.Color.dark_magenta())
        await ctx.send(embed=embed)

        cursor.close()
        datenbank.close()

def setup(client):
    client.add_cog(Sprache(client))