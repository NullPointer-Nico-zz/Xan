import discord
import random
import asyncio
import datetime


from discord.ext import commands


class Game(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ssp(self, ctx):

        spieler =["schere",  "stein", "papier"]

        help = discord.Embed(title='Wähle weise xD', description='Du hast 2 minuten zeit.',
                             color=discord.Color.dark_blue())


        msg = await ctx.send(embed=help)

        com = random.choice(spieler)

        await msg.add_reaction("✊")
        await msg.add_reaction("📄")
        await msg.add_reaction("✌️")

        def check(reaction, user):
        	return user == ctx.author and str(reaction.emoji) in ["✊", "📄", "✌️"]

        while True:
        	try:
        		reaction, user = await self.client.wait_for('reaction_add', timeout=120, check=check)

        		if str(reaction.emoji) == "✊" and com == "schere":
        			help.title = "GAME OVER"
        			help.description == "YOU WIN"
        			await msg.edit(embed=help)
        			await msg.remove_reaction(reaction, user)
        			await msg.clear_reaction("✊")
        			await msg.clear_reaction("📄")
        			await msg.clear_reaction("✌️")
        			break

        		elif str(reaction.emoji) == "📄" and com == "schere":
        			help.title = "GAME OVER"
        			help.description == "YOU LOSE"
        			await msg.edit(embed=help)
        			await msg.remove_reaction(reaction, user)
        			await msg.clear_reaction("✊")
        			await msg.clear_reaction("📄")
        			await msg.clear_reaction("✌️")
        			break

        		elif str(reaction.emoji) == "✌️" and com == "schere":
        			help.title = "GAME OVER"
        			help.description = "UNENDSCHIEDEN"
        			await msg.edit(embed=help)
        			await msg.remove_reaction(reaction, user)
        			await msg.clear_reaction("✊")
        			await msg.clear_reaction("📄")
        			await msg.clear_reaction("✌️")
        			break

        		elif str(reaction.emoji) == "✊" and com == "papier":
        			help.title = "GAME OVER"
        			help.description = "YOU LOSE"
        			await msg.edit(embed=help)
        			await msg.remove_reaction(reaction, user)
        			await msg.clear_reaction("✊")
        			await msg.clear_reaction("📄")
        			await msg.clear_reaction("✌️")
        			break

        		elif str(reaction.emoji) == "📄" and com == "papier":
        			help.title == "GAME OVER"
        			help.description = "UNENDSCHIEDEN"
        			await msg.edit(embed=help)
        			await msg.remove_reaction(reaction, user)
        			await msg.clear_reaction("✊")
        			await msg.clear_reaction("📄")
        			await msg.clear_reaction("✌️")
        			break

        		elif str(reaction.emoji) == "✌️" and com == "papier":
        			help.title = "GAME OVER"
        			help.description = "YOU WIN"
        			await msg.edit(embed=help)
        			await msg.remove_reaction(reaction, user)
        			await msg.clear_reaction("✊")
        			await msg.clear_reaction("📄")
        			await msg.clear_reaction("✌️")
        			break
 
        		elif str(reaction.emoji) == "✊" and com == "stein":
        			help.title = "GAME OVER"
        			help.description = "UNENDSCHIEDEN"
        			await msg.edit(embed=help)
        			await msg.remove_reaction(reaction, user)
        			await msg.clear_reaction("✊")
        			await msg.clear_reaction("📄")
        			await msg.clear_reaction("✌️")
        			break

        		elif str(reaction.emoji) == "📄" and com == "stein":
        			help.title = "GAME OVER"
        			help.description = "YOU WIN"
        			await msg.edit(embed=help)
        			await msg.remove_reaction(reaction, user)
        			await msg.clear_reaction("✊")
        			await msg.clear_reaction("📄")
        			await msg.clear_reaction("✌️")
        			break

        		elif str(reaction.emoji) == "✌️" and com == "stein":
        			help.title = "GAME OVER"
        			help.description = "YOU LOSE"
        			await msg.edit(embed=help)
        			await msg.remove_reaction(reaction, user)
        			await msg.clear_reaction("✊")
        			await msg.clear_reaction("📄")
        			await msg.clear_reaction("✌️")
        			break

        	except asyncio.TimeoutError:
        		help.title = "GAME OVER"
        		help.description = "YOU LOSE"
        		await msg.edit(embed=help) 

def setup(client):
    client.add_cog(Game(client))
