import discord
from discord.ext import commands

class ClearCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, limit: int = None):
        if ctx.message.author.guild_permissions.administrator:
            if not limit:
                await ctx.message.delete()
                kein_limit = discord.Embed(title='**No Limit**', color=discord.Color.dark_orange())
                kein_limit.add_field(name='**Kein Limit**', value='Es wurde limit angegeben!')
                await ctx.send(embed=kein_limit)
            else:
                await ctx.message.delete()
                await ctx.channel.purge(limit=limit)
                chat_clear = discord.Embed(title='**Chat Clear**', color=discord.Color.green())
                chat_clear.add_field(name='**Anzahl**', value=f'{limit}')
                chat_clear.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
                await ctx.send(embed=chat_clear, delete_after=3)
        else:
            await ctx.message.delete()
            no_permission = discord.Embed(title='**No Permission**', color=discord.Color.dark_red())
            no_permission.add_field(name='Keine Rechte',
                                    value='```administrator```')
            no_permission.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
            await ctx.send(embed=no_permission)


def setup(client):
    client.add_cog(ClearCommand(client))