import discord
from discord.ext import commands


class unicode(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def unicode(self, ctx, *, text=''):
        if ctx.message.author.id == 346952827970781185:
            await ctx.send(f'```{text}```')
        else:
            no_permission = discord.Embed(
                title='No Permission', color=discord.Color.dark_red())
            no_permission.add_field(
                name='Keine Rechte', value='Du bist nicht der Bot Owner!')
            no_permission.set_footer(
                text=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url_as(size=512)}')
            await ctx.send(embed=no_permission)


def setup(client):
    client.add_cog(unicode(client))
