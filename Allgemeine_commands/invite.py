import discord

from discord.ext import commands

class InviteCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title='**Invite**', description='Bot Invite:\nhttps://discord.com/api/oauth2/authorize?client_id=716371146022322226&permissions=8&scope=bot\n\nServer Invite:https://discord.gg/vzUbh2U')
        await ctx.message.delete()
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(InviteCommand(client))