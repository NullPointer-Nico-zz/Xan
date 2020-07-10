import discord
from discord.ext import commands
import datetime as d
import platform
import psutil

from Bot import start_time
from Secrets import BOT_VERSION


class BotInfoCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def botinfo(self, ctx):
        # ramusage, cpuusage, usw.
        ram = psutil.virtual_memory()
        cpu = psutil.cpu_percent(interval=1)

        # uptime
        now = d.datetime.utcnow()
        delta = now - start_time
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        if days:
            time_format = 'Tage: **{d}**\nStunden: **{h}**\nMinuten: **{m}**\nSekunden: **{s}**'
        else:
            time_format = 'Stunden: **{h}**\nMinuten: **{m}**\nSekunden: **{s}**'
        uptime_stamp = time_format.format(
            d=days, h=hours, m=minutes, s=seconds)

        await ctx.message.delete()
        bot_info = discord.Embed(title='**Bot Info**', description='Infos über den Bot',
                                 color=discord.Color.dark_gold())
        bot_info.add_field(
            name='**Name**', value=f'{self.client.user.name}', inline=True)
        bot_info.add_field(name='**Bot Version**',
                           value=BOT_VERSION, inline=True)
        bot_info.add_field(name='**Erstellungs Datum**',
                           value=f'{self.client.user.created_at}', inline=True)
        bot_info.add_field(
            name='**API**', value='Discord.py\nhttps://discordpy.readthedocs.io/en/latest/', inline=True)
        bot_info.add_field(name='**API Version**',
                           value=f'{discord.__version__}', inline=True)
        bot_info.add_field(name='**OS/Plattform**',
                           value=f'{platform.system()}', inline=True)
        bot_info.add_field(name='**Invite**',
                           value='https://discord.com/api/oauth2/authorize?client_id=716371146022322226&permissions=8&scope=bot',
                           inline=True)
        bot_info.add_field(name='**Uptime seit Restart**',
                           value=f'{uptime_stamp}', inline=True)
        bot_info.add_field(
            name='**Bot owner**', value=f'Zockyyyy || Nico#7468\nhttps://dsc.bio/zockyyyy', inline=True)
        bot_info.add_field(name='**RAM Usage in %**',
                           value=f'{str(ram[2])}%', inline=True)
        bot_info.add_field(name='**CPU Usage in %**',
                           value=f'{str(cpu)}%', inline=True)
        bot_info.set_footer(
            text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
        await ctx.send(embed=bot_info)


def setup(client):
    client.add_cog(BotInfoCommand(client))
