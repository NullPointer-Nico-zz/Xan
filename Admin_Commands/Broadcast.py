from sqlite3.dbapi2 import PARSE_COLNAMES
import discord
import random

from discord.ext import commands
from Bot import trans

class BroadCastCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def br(self, ctx, *, args=None):
        if not ctx.author.guild_permissions.administrator:
            no_permission = discord.Embed(
                title=trans(ctx.message, 'Dazu hast du keine Berechtigung!'), 
                description=f'{trans(ctx.message, "Sie haben nicht die folgende Berechtigung")}:\n`Administrator`', 
                color=discord.Color.dark_red())
            no_permission.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
            await ctx.send(embed=no_permission)
            return True
        
        if not args:
            no_args = discord.Embed(title=trans(ctx.message, "Keine Nachricht angegeben"), color=discord.Color.dark_red())
            await ctx.send(embed=no_args)
            return True

        broadcast = discord.Embed(title=trans(ctx.message, "Wichtige Nachricht"), description=f'`{args}`', color=random.randint(0, 0xffffff))
        broadcast.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
        await ctx.send(embed=broadcast)


def setup(client):
    client.add_cog(BroadCastCommand(client))
