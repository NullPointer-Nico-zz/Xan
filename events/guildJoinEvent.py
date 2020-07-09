import discord
import json

from discord.ext import commands

class GuildJoinEvent(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = 'x!'

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

def setup(client):
    client.add_cog(GuildJoinEvent(client))