import asyncio
import discord
import sqlite3 as sql
from nanoid import generate
from Bot import todo_ids, todos

from discord.ext import commands

class TODOList(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True, case_insensitive=True)
    async def todo(self, ctx):
        datenbank = sql.connect('DatenBank.sqlite')
        cursor = datenbank.cursor()
        cursor.execute(f'SELECT prefix FROM Prefixe WHERE guild_id = {ctx.guild.id}')
        result = cursor.fetchone()

        if ctx.message.author.id == 346952827970781185:
            embed = discord.Embed(title='TODO List', colour=ctx.message.author.colour)
            embed.add_field(name='TODO Add', value=f'`{result[0]}todo add [todo]`', inline=False)
            embed.add_field(name='TODO Remove', value=f'`{result[0]}todo remove [id]`', inline=False)
            embed.add_field(name='TODO Show', value=f'`{result[0]}todo show`', inline=False)
            await ctx.send(embed=embed)
        else:
            no_permission = discord.Embed(
                title='No Permission', description='Du bist nicht der Bot Owner!', color=discord.Color.dark_red())
            no_permission.set_footer(
                text=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url_as(size=512)}')
            await ctx.send(embed=no_permission)

    @todo.command()
    async def add(self, ctx, *, args=None):
        def id_generator():
            return generate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYT1234567890', 15)

        if ctx.message.author.id == 346952827970781185:
            datenbank = sql.connect('DatenBank.sqlite')
            cursor = datenbank.cursor()
            
            if args is None:
                embed = discord.Embed(title='TODO LIST', description='Du hast keine todo angegeben!', colour=ctx.message.author.colour)
                await ctx.send(embed=embed)
                return True

            uniqe_id = id_generator()

            try:
                cursor.execute('INSERT INTO todo(ID, TODO) VALUES (?, ?)', (uniqe_id, args))
                datenbank.commit()
                cursor.close()
                datenbank.close()
            except Exception as e:
                print(f'[ERROR] {e}')

            e = discord.Embed(title='TODO LIST', description=f'TODO: `{args}`\nID: `{uniqe_id}`\n\nDeine TODO wurde zur List eingetragen!', colour=ctx.message.author.colour)
            await ctx.send(embed=e)

        else:
            no_permission = discord.Embed(
                title='No Permission', description='Du bist nicht der Bot Owner!', color=discord.Color.dark_red())
            no_permission.set_footer(
                text=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url_as(size=512)}')
            await ctx.send(embed=no_permission)

    @todo.command()
    async def remove(self, ctx, args=None):
        todo_ids.clear()
        if ctx.message.author.id == 346952827970781185:
            datenbank = sql.connect('DatenBank.sqlite')
            cursor = datenbank.cursor()
            cursor.execute('SELECT ID FROM todo')
            results = cursor.fetchall()
            for rows in results:
                todo_ids.add(rows[0])

            if len(todo_ids) == 0:
                embed = discord.Embed(title='TODO LIST', description='Du hast noch keine TODO`S!', colour=ctx.message.author.colour)
                await ctx.send(embed=embed)
                return True
            
            if args is None:
                embed = discord.Embed(title='TODO LIST', description='Du hast keine ID angegeben!', colour=ctx.message.author.colour)
                await ctx.send(embed=embed)
                return True

            if args not in todo_ids:
                embed = discord.Embed(title='TODO LIST', description='Diese ID gibt es nicht!', colour=ctx.message.author.colour)
                await ctx.send(embed=embed)
                return True

            if args in todo_ids:
                cursor.execute('DELETE FROM todo WHERE ID =(?)', (args,))
                datenbank.commit()
                cursor.close()
                datenbank.close()

            e = discord.Embed(title='TODO LIST', description=f'Die TODO mit der ID `{args}` wurde aus deiner TODO List entfernt!', colour=ctx.message.author.colour)
            await ctx.send(embed=e)
            todo_ids.remove(args)

        else:
            no_permission = discord.Embed(
                title='No Permission', description='Du bist nicht der Bot Owner!', color=discord.Color.dark_red())
            no_permission.set_footer(
                text=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url_as(size=512)}')
            await ctx.send(embed=no_permission)

    @todo.command()
    async def show(self, ctx):
        counter = 1
        todo_ids.clear()
        todos.clear()
        if ctx.message.author.id == 346952827970781185:
            datenbank = sql.connect('DatenBank.sqlite')
            cursor = datenbank.cursor()
            cursor.execute('SELECT * FROM todo')
            results = cursor.fetchall()
            
            s = discord.Embed(title='TODO LIST', description='Deine TODO`S\n\n', colour=ctx.message.author.colour)

            for rows in results:
                if not rows[0] or not rows[1]:
                    e = discord.Embed(title='TODO LIST', description=f'Du hast noch keine TODO`S!', colour=ctx.message.author.colour)
                    await ctx.send(embed=e)
                    break

                if len(s.fields) == 25:
                    break

                todo_ids.add(rows[0])
                todos.add(rows[1])

                s.add_field(name=f'TODO {str(counter)}', value=f'TODO: `{rows[1]}`\nID: `{rows[0]}`', inline=False)
                counter += 1

            await ctx.send(embed=s)
            counter = 1

        else:
            no_permission = discord.Embed(
                title='No Permission', description='Du bist nicht der Bot Owner!', color=discord.Color.dark_red())
            no_permission.set_footer(
                text=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url_as(size=512)}')
            await ctx.send(embed=no_permission)
         

def setup(client):
    client.add_cog(TODOList(client))