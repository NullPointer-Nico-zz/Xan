import discord

from discord.ext import commands
from Bot import trans
from Bot import getPrefix

class ClearCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, limit: int = None):
        if not ctx.message.author.guild_permissions.administrator:
            no_permission = discord.Embed(
                title=trans(ctx.message, 'Dazu hast du keine Berechtigung!'), 
                description=f'{trans(ctx.message, "Sie haben nicht die folgende Berechtigung")}:\n`Administrator`', 
                color=discord.Color.dark_red())
            no_permission.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
            await ctx.send(embed=no_permission)
            return True

        if not limit:
            kein_limit = discord.Embed(
                title=trans(ctx.message, 'Keine Begrenzung'), description=f'`Usage: {getPrefix(ctx.message)}clear <int>`', color=discord.Color.dark_orange())
            await ctx.send(embed=kein_limit)
            return True

        await ctx.channel.purge(limit=limit)

        chat_clear = discord.Embed(
            title='Chat Clear', 
            description=f'{trans(ctx.message, f"`{limit}` Es wurde Nachrichten gelöscht")}', 
            color=discord.Color.green())
        chat_clear.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))

        await ctx.send(embed=chat_clear, delete_after=3)

def setup(client):
    client.add_cog(ClearCommand(client))
