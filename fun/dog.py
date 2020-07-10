import discord
import aiohttp

from discord.ext import commands


class dog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as s:
            async with s.get('https://dog.ceo/api/breeds/image/random') as r:
                if r.status == 200:
                    js = await r.json()
                    random_dog = discord.Embed(
                        title='**Random Dog**', description=f'Hier **{ctx.author.name}** ein Bild von einem Hund!', color=discord.Color.dark_orange())
                    random_dog.set_image(url=js['message'])
                    random_dog.set_footer(text='Powered by https://dog.ceo/')
                    await ctx.message.delete()
                    await ctx.send(embed=random_dog)
                else:
                    random_dog_error = discord.Embed(
                        title='**Random Dog Error**', description='**https://dog.ceo/ konnte nicht erricht werden!**', color=discord.Color.dark_red())
                    await ctx.message.delete()
                    await ctx.send(embed=random_dog_error)


def setup(client):
    client.add_cog(dog(client))
