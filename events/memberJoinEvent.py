import discord
from discord.ext import commands

class MemberJoinEvent(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        join = discord.utils.get(self.client.get_all_channels(), guild__name='➤ Xan Bot | Support', name='×📍eingangshalle📍×')
        user_role = member.guild.get_role(730422919112687671)

        await join.send(f'User _**{member.name}**_ ist auf unserem Discord angekommen!')
        await member.add_roles(user_role)


def setup(client):
    client.add_cog(MemberJoinEvent(client))