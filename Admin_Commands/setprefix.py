import discord
import sqlite3

from discord.ext import commands


class SetPrefix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def setprefix(self, ctx, p=None):
        if ctx.message.author.guild_permissions.administrator:
            if not p:
                await ctx.message.delete()
                await ctx.send('**Bitte geb ein neuen Prefix an!**')
            else:
                await ctx.message.delete()
                db = sqlite3.connect('DatenBank.sqlite')
                cursor = db.cursor()
                cursor.execute(
                    f'SELECT prefix FROM Prefixe WHERE guild_id = {ctx.guild.id}')
                result = cursor.fetchone()

                if result is None:
                    prefix = (
                        'INSERT INTO Prefixe(guild_id, prefix) VALUES(?, ?)')
                    value = (ctx.guild.id, p)
                else:
                    prefix = (
                        'UPDATE Prefixe SET prefix = ? WHERE guild_id = ?')
                    value = (p, ctx.guild.id)

                cursor.execute(prefix, value)
                db.commit()
                cursor.close()
                db.close()
                await ctx.send(f'**Prefix wurde zu** ```{p}``` **geändert!**')
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
