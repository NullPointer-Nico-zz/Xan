import discord
from discord.ext import commands

user = set([])

class LiveCounter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def counter(self, ctx):
        await ctx.send('User werden gezählt...')

def setup(client):
    client.add_cog(LiveCounter(client))