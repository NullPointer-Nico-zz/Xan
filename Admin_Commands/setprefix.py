import discord
import json

from discord.ext import commands


class SetPrefix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def setprefix(self, ctx, prefix=None):
        if ctx.message.author.guild_permissions.administrator:
            if not prefix:
                await ctx.message.delete()
                await ctx.send('**Bitte geb ein neuen Prefix an!**')
            else:
                await ctx.message.delete()
                with open('prefixes.json', 'r') as f:
                    prefixes = json.load(f)

                prefixes[str(ctx.guild.id)] = prefix

                with open('prefixes.json', 'w') as f:
                    json.dump(prefixes, f, indent=4)

                await ctx.send(f'**Prefix wurde zu** ```{prefix}``` **geändert!**')
        else:
            await ctx.message.delete()
            no_permission = discord.Embed(
                title='**No Permission**', color=discord.Color.dark_red())
            no_permission.add_field(name='Keine Rechte',
                                    value='```administrator```')
            no_permission.set_footer(
                text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
            await ctx.send(embed=no_permission)


def setup(client):
    client.add_cog(SetPrefix(client))
