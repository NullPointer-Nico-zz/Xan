import discord
import sqlite3

from discord.ext import commands


class GuildJoinEvent(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        datenbank = sqlite3.connect('DatenBank.sqlite')
        cursor = datenbank.cursor()
        cursor.execute(
            f'SELECT prefix FROM Prefixe WHERE guild_id = {guild.id}')
        result = cursor.fetchone()

        if result is None:
            prefix = cursor.execute('INSERT INTO Prefixe (guild_id, prefix) VALUES (?, ?)', (guild.id, "$"))
        
        datenbank.commit()


        cursor.execute(f'SELECT lang FROM lang WHERE guild_id = {guild.id}')
        result = cursor.fetchone()

        if result is None:
            lang = cursor.execute('INSERT INTO lang(guild_id, lang) VALUES(?, ?)', (guild.id, "en"))

        datenbank.commit()
        cursor.close()
        datenbank.close()


def setup(client):
    client.add_cog(GuildJoinEvent(client))
