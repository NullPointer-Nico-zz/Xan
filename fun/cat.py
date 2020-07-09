import discord
import asyncio
import aiohttp

from discord.ext import commands

class Cat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as s:
            async with s.get('http://aws.random.cat/meow') as r:
                if r.status == 200:
                    js = await r.json()
                    random_cat = discord.Embed(title='**Random Cat**', description=f'Hier **{ctx.author.name}** ein Bild von einer Katze!', color=discord.Color.dark_orange())
                    random_cat.set_image(url=js['file'])
                    random_cat.set_footer(text='Powered by http://aws.random.cat')
                    await ctx.message.delete()
                    await ctx.send(embed=random_cat)
                else:
                    random_cat_error = discord.Embed(title='**Random Cat Error**', description='**http://aws.random.cat konnte nicht erreicht werden!**', color=discord.Color.dark_red())
                    await ctx.message.delete()
                    await ctx.send(embed=random_cat_error)

def setup(client):
    client.add_cog(Cat(client))