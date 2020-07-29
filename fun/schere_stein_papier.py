import discord
import random
import datetime


from discord.ext import commands


class Game(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ssp(self, ctx, args=None):

        computer = ["schere", "stein", "papier"]
        spieler =["schere",  "stein", "papier"]

        help = discord.Embed(title='**Schere Stein Papier**',
                             color=discord.Color.dark_blue())
        help.add_field(name='**How to Play**',
                   value='Wähle was aus\n\nBeispiel.\n```ssp stein/schere/papier```')
        help.set_footer(text="ACHTUNG! stein/schere/papier klein schreiben! ACHTUNG!")


        if args == None:

            await ctx.send(embed=help)

        if args not in spieler:

            await ctx.send(embed=help)

        else:

            result = random.choice(computer)

            you_win = discord.Embed(title='**Game Result**',color=discord.Color.dark_gold())
            you_win.set_author(name=ctx.message.author.name)
            you_win.add_field(name='**You Win**', value=f'You: {args}\nXan: {result}')
            you_win.timestamp = datetime.datetime.utcnow()

            you_lose = discord.Embed(title='**Game Result**',color=discord.Color.dark_gold())
            you_lose.set_author(name=ctx.message.author.name)
            you_lose.add_field(name='**You Lose**', value=f'You: {args}\nXan: {result}')
            you_lose.timestamp = datetime.datetime.utcnow()

            unendschieden = discord.Embed(title='**Game Result**',color=discord.Color.dark_gold())
            unendschieden.set_author(name=ctx.message.author.name)
            unendschieden.add_field(name='**Unentschieden**', value=f'You: {args}\nXan: {result}')
            unendschieden.timestamp = datetime.datetime.utcnow()

            if args == "schere" and result == "stein":
                
                #you lose    
                await ctx.send(embed=you_lose)
                return True

            elif args == "schere" and result == "schere":

                #unendschieden
                await ctx.send(embed=unendschieden)
                return True

            elif args == "schere" and result == "papier":

                #you win
                await ctx.send(embed=you_win)
                return True

            elif args == "stein" and result == "papier":

                #you lose
                await ctx.send(embed=you_lose)
                return True

            elif args == "stein" and result == "schere":

                #you win
                await ctx.send(embed=you_win)
                return True

            elif args == "stein" and result == "stein":

                #unendschieden
                await ctx.send(embed=unendschieden)
                return True

            elif args == "papier" and result == "papier":

                #unendschieden
                await ctx.send(embed=unendschieden)
                return True

            elif args == "papier" and result == "schere":

                #you lose
                await ctx.send(embed=you_lose)
                return True

            elif args == "papier" and result == "stein":

                #you win
                await ctx.send(embed=you_win)
                return True


def setup(client):
    client.add_cog(Game(client))
