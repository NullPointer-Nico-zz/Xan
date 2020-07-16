import discord
from discord.ext import commands


class memberLeaveEvent(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        leave = discord.utils.get(self.client.get_all_channels(
        ), guild__name='➤ Xan Bot | Support', name='⭐eingangshalle⭐')

        if member.bot:
            await leave.send(f'Bot _**{member.name}**_ hat unseren Discord Verlassen!')
        else:
            await leave.send(f'User _**{member.name}**_ hat unseren Discord Verlassen!')


def setup(client):
    client.add_cog(memberLeaveEvent(client))
