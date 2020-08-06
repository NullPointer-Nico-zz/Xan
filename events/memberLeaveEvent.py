import discord
import sqlite3

from discord.ext import commands


class memberLeaveEvent(commands.Cog):
    def __init__(self, client):
        self.client = client

   
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        datenbank = sqlite3.connect('DatenBank.sqlite')
        cursor = datenbank.cursor()
        cursor.execute(
            f'SELECT channel_id FROM Leaves WHERE guild_id = {member.guild.id}')
        result = cursor.fetchone()
        members = len(list(member.guild.members))
        guild = member.guild

        if result is None:
            return
        else:
            cursor.execute(
                f'SELECT message FROM Leaves WHERE guild_id = {member.guild.id}')
            result1 = cursor.fetchone()
            channel = self.client.get_channel(id=int(result[0]))

            embed = discord.Embed(
                title='**Leave**', description=f'**{members}** User!', color=discord.Color.dark_red())
            embed.set_image(url=member.avatar_url)
            embed.add_field(name=member.name, value=f'_{result1[0]}_')
            embed.timestamp = datetime.datetime.utcnow()
            await channel.send(embed=embed)

    @commands.group(invoke_without_command=True, case_insensitive=True)
    async def leave(self, ctx):
        if ctx.message.author.guild_permissions.administrator:
            await ctx.message.delete()
            embed = discord.Embed(title='**Leave Settings**',
                                  description='Bitte geb **leave help** ein um alle befehle zu sehen!', color=discord.Color.dark_green())
            embed.set_footer(
                text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
            await ctx.send(embed=embed)
        else:
            await ctx.message.delete()
            no_permission = discord.Embed(
                title='**No Permission**', color=discord.Color.dark_red())
            no_permission.add_field(name='Keine Rechte',
                                    value='```administrator```')
            no_permission.set_footer(
                text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
            await ctx.send(embed=no_permission)

    @leave.command()
    async def help(self, ctx):
        if ctx.message.author.guild_permissions.administrator:
            await ctx.message.delete()
            embed = discord.Embed(
                title='**Leave Settings**', color=discord.Color.dark_green())
            embed.add_field(name='setchannel',
                            value='```leave setchannel <channel>```')
            embed.add_field(name='setmessage',
                            value='```leave setmessage <message>```')
            embed.set_footer(
                text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
            await ctx.send(embed=embed)
        else:
            await ctx.message.delete()
            no_permission = discord.Embed(
                title='**No Permission**', color=discord.Color.dark_red())
            no_permission.add_field(name='Keine Rechte',
                                    value='```administrator```')
            no_permission.set_footer(
                text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
            await ctx.send(embed=no_permission)

    @leave.command()
    async def setchannel(self, ctx, channel: discord.TextChannel = None):
        if ctx.message.author.guild_permissions.administrator:
            datenbank = sqlite3.connect('DatenBank.sqlite')
            cursor = datenbank.cursor()
            cursor.execute(
                f'SELECT channel_id FROM Leaves WHERE guild_id = {ctx.guild.id}')
            result = cursor.fetchone()
            if result is None:
                db = ('INSERT INTO Leaves(guild_id, channel_id) VALUES(?, ?)')
                value = (ctx.guild.id, channel.id)
                embed = discord.Embed(
                    title='**Leave Settings**', description=f'Der Leave Channel wurde auf **{channel.mention}** gesetzt!', color=discord.Color.dark_red())
                embed.set_footer(
                    text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif result is not None:
                db = ('UPDATE Leaves SET channel_id = ? WHERE guild_id = ?')
                value = (channel.id, ctx.guild.id)
                embed = discord.Embed(
                    title='**Leave Settings**', description=f'Der Leaves Channel wurde auf **{channel.mention}** geupdatet!', color=discord.Color.dark_red())
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

    @leave.command()
    async def setmessage(self, ctx, *, text=None):
        if ctx.message.author.guild_permissions.administrator:
            datenbank = sqlite3.connect('DatenBank.sqlite')
            cursor = datenbank.cursor()
            cursor.execute(
                f'SELECT message FROM Leaves WHERE guild_id = {ctx.guild.id}')
            result = cursor.fetchone()

            if result is None:
                db = ('INSERT INTO Leaves(guild_id, message) VALUES(?, ?)')
                value = (ctx.guild.id, text)
                embed = discord.Embed(
                    title='**Leave Settings**', description=f'Die Leave Message wurde auf **{text}** gesetzt!', color=discord.Color.dark_red())
                embed.set_footer(
                    text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
                await ctx.message.delete()
                await ctx.send(embed=embed)
            elif result is not None:
                db = ('UPDATE Leaves SET message = ? WHERE guild_id = ?')
                value = (text, ctx.guild.id)
                embed = discord.Embed(
                    title='**Leave Settings**', description=f'Die leave Message wurde auf **{text}** geupdatet!', color=discord.Color.dark_red())
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


def setup(client):
    client.add_cog(memberLeaveEvent(client))
