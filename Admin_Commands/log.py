import discord
import datetime
import sqlite3

from discord.ext import commands


class Log(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def setlog(self, ctx, channel: discord.TextChannel = None):
        if ctx.message.author.guild_permissions.administrator:
            datenbank = sqlite3.connect('DatenBank.sqlite')
            cursor = datenbank.cursor()
            cursor.execute(
                f'SELECT channel_id FROM Logs WHERE guild_id = {ctx.guild.id}')
            result = cursor.fetchone()
            if result is None:
                db = ('INSERT INTO Logs(guild_id, channel_id) VALUES(?, ?)')
                value = (ctx.guild.id, channel.id)
                embed = discord.Embed(
                    title='**Log Settings**', description=f'Der Log Channel wurde auf **{channel.mention}** gesetzt!', color=discord.Color.dark_red())
                embed.set_footer(
                    text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif result is not None:
                db = ('UPDATE Welcomes SET channel_id = ? WHERE guild_id = ?')
                value = (channel.id, ctx.guild.id)
                embed = discord.Embed(
                    title='**Log Settings**', description=f'Der Log Channel wurde auf **{channel.mention}** geupdatet!', color=discord.Color.dark_red())
                embed.set_footer(
                    text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
                await ctx.message.delete()
                await ctx.send(embed=embed)
            cursor.execute(db, value)
            datenbank.commit()
            cursor.close()
            datenbank.close()
        else:
            await ctx.message.delete()
            no_permission = discord.Embed(
                title='**No Permission**', color=discord.Color.dark_red())
            no_permission.add_field(name='Keine Rechte',
                                    value='```administrator```')
            no_permission.set_footer(
                text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
            await ctx.send(embed=no_permission)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        db = sqlite3.connect('DatenBank.sqlite')
        cursor = db.cursor()
        cursor.execute(
            f'SELECT channel_id FROM Logs WHERE guild_id = {message.guild.id}')
        channel_id = cursor.fetchone()
        log = message.guild.get_channel(int(channel_id[0]))

        if channel_id is None:
            return
        else:
            async for entry in message.guild.audit_logs(limit=1, action=discord.AuditLogAction.message_delete):

                if len(message.content) > 1024:
                    await log.send(message.content)
                else:
                    embed = discord.Embed(title='**Message Deletet**',
                                      description=f'Author: {message.author.name}',
                                      color=discord.Color.red())
                    embed.add_field(name='Content',
                                    value=f'_{message.content}_',
                                    inline=False)
                    embed.add_field(name='Gelöscht von', value='_{0.user}_'.format(entry), inline=False)
                    embed.timestamp = datetime.datetime.utcnow()  
                    await log.send(embed=embed)


    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        db = sqlite3.connect('DatenBank.sqlite')
        cursor = db.cursor()
        cursor.execute(
            f'SELECT channel_id FROM Logs WHERE guild_id = {before.guild.id}')
        channel_id = cursor.fetchone()

        if channel_id is None:
                return
        else:
            log = before.guild.get_channel(int(channel_id[0]))
            if before.content != after.content:
                embed = discord.Embed(
                    title='**Message Edit**', description=f'Author: {before.author.name}', color=discord.Color.red())
                embed.add_field(
                    name='Before', value=f'_{before.content}_', inline=False)
                embed.add_field(
                    name='After', value=f'_{after.content}_', inline=False)
                embed.timestamp = datetime.datetime.utcnow()
                await log.send(embed=embed)


    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        db = sqlite3.connect('DatenBank.sqlite')
        cursor = db.cursor()
        cursor.execute(f'SELECT channel_id FROM Logs WHERE guild_id = {before.guild.id}')
        channel_id = cursor.fetchone()

        if channel_id is None:
            return
        else:
            log = before.guild.get_channel(int(channel_id[0]))
            if before.display_name != after.display_name:
                embed = discord.Embed(
                    title='**User Edit**', description='Username Change', color=discord.Color.red())
                embed.add_field(
                    name='Before', value=f'{before.display_name}', inline=False)
                embed.add_field(
                    name='After', value=f'{after.display_name}', inline=False)
                embed.timestamp = datetime.datetime.utcnow()
                await log.send(embed=embed)


    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        db = sqlite3.connect('DatenBank.sqlite')
        cursor = db.cursor()
        cursor.execute(f'SELECT channel_id FROM Logs WHERE guild_id = {guild.id}')
        channel_id = cursor.fetchone()

        if channel_id is None:
            return
        else:
            log = guild.get_channel(int(channel_id[0]))
            


def setup(client):
    client.add_cog(Log(client))
