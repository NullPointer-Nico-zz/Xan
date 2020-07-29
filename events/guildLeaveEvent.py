import discord
import sqlite3

from discord.ext import commands


class GuildLeaveEvent(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        datenbank = sqlite3.connect('DatenBank.sqlite')
        cursor = datenbank.cursor()
        
        cursor.execute(f'DELETE FROM Prefixe WHERE guild_id = {guild.id}')

        datenbank.commit()
        cursor.close()
        datenbank.close()


def setup(client):
    client.add_cog(GuildLeaveEvent(client))
