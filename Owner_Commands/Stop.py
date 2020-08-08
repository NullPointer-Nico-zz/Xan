import discord
from discord.ext import commands


class StopCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def stop(self, ctx):
        if ctx.message.author.id == 346952827970781185:
            await ctx.message.delete()
            await ctx.send('**Bot wird gestoppt!**')
            await self.client.close()
        else:
            no_permission = discord.Embed(
                title='No Permission', color=discord.Color.dark_red())
            no_permission.add_field(
                name='Keine Rechte', value='Du bist nicht der Bot Owner!')
            no_permission.set_footer(
                text=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url_as(size=512)}')
            await ctx.send(embed=no_permission)


def setup(client):
    client.add_cog(StopCommand(client))
