import discord
from discord.ext import commands
import random


class BroadCastCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def br(self, ctx, *, args=None):
        if not ctx.author.guild_permissions.administrator:
            await ctx.message.delete()
            no_permission = discord.Embed(title='**No Permission**', color=discord.Color.dark_red())
            no_permission.add_field(name='Keine Rechte',
                                    value='```administrator```!')
            no_permission.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
            await ctx.send(embed=no_permission)
        else:
            if not args:
                no_args = discord.Embed(title='**Nix angegeben**', color=discord.Color.dark_red())
                no_args.add_field(name='Kein Text Angegeben', value='Du hast nix angegeben!', inline=True)
                await ctx.message.delete()
                await ctx.send(embed=no_args)
            else:
                broadcast = discord.Embed(title='**Wichtig**', color=random.randint(0, 0xffffff))
                broadcast.add_field(name='Nachricht', value=args)
                broadcast.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
                await ctx.message.delete()
                await ctx.send(embed=broadcast)


def setup(client):
    client.add_cog(BroadCastCommand(client))
