import discord
import asyncio

from discord.ext import commands
import commandcounter


class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True, case_insensitive=True)
    async def help(self, ctx):
        # help commands categorys
        help_commands_category = discord.Embed(title='**Help**', description=f'Settings | Help', color=discord.Color.dark_blue())
        help_commands_category.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url_as(size=512))
        help_commands_category.set_thumbnail(url='https://i.ibb.co/5Bt2bM9/Neon-Photo-Editor-20200706-144711323.jpg')
        help_commands_category.add_field(name='**Kategorien**', value='**-----------------------------------------------**')
        help_commands_category.add_field(name='**All**', value=f'```» {len(commandcounter.alle_commands)} Commands```', inline=False)
        help_commands_category.add_field(name='**Everyone**', value=f'```» {len(commandcounter.Allegemeine_commands)} Commands```', inline=False)
        help_commands_category.add_field(name='**Fun**', value=f'```» {len(commandcounter.fun_commands)} Commands```')
        help_commands_category.add_field(name='**Moderation**', value=f'```» {len(commandcounter.mod_commands)} Commands```', inline=False)
        help_commands_category.add_field(name='**Administrator**', value=f'```» {len(commandcounter.Admin_Commands)} Commands```', inline=False)
        help_commands_category.add_field(name='**Owner**', value=f'```» {len(commandcounter.owner_commands)} Commands```', inline=False)
        help_commands_category.set_footer(text=f'Command angefordert von {ctx.message.author.name}')

        await ctx.message.delete()
        await ctx.send(embed=help_commands_category)

    @help.command()
    async def fun(self, ctx):
        help_commands_fun = discord.Embed(title='**Help Fun**', description=f'Settings | Help', color=discord.Color.dark_blue())
        help_commands_fun.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url_as(size=512))
        help_commands_fun.set_thumbnail(url='https://i.ibb.co/5Bt2bM9/Neon-Photo-Editor-20200706-144711323.jpg')
        help_commands_fun.add_field(name='**Cat**', value='_usage: cat_', inline=False)
        help_commands_fun.add_field(name='**Dog**', value='_usage: dog_', inline=False)
        help_commands_fun.set_footer(text='<> = Nötig | [] = Nicht Nötig')

        await ctx.message.delete()
        await ctx.send(embed=help_commands_fun)

    @help.command()
    async def all(self, ctx):
        # alle commands
        help_commands_all = discord.Embed(title='**Help All**', description='Settings | Help', color=discord.Color.dark_blue())
        help_commands_all.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url_as(size=512))
        help_commands_all.set_thumbnail(url='https://i.ibb.co/5Bt2bM9/Neon-Photo-Editor-20200706-144711323.jpg')
        help_commands_all.add_field(name='**Botinfo**', value=f'_usage: {self.client.get_prefix}botinfo_', inline=False)
        help_commands_all.add_field(name='**Help**', value='_usage: help <category>_', inline=False)
        help_commands_all.add_field(name='**Ping**', value='_usage: ping_', inline=False)
        help_commands_all.add_field(name='**Cat**', value='_usage: cat_', inline=False)
        help_commands_all.add_field(name='**Dog**', value='_usage: dog_', inline=False)
        help_commands_all.add_field(name='**Ban**', value='_usage: ban <member> [grund]_', inline=False)
        help_commands_all.add_field(name='**Kick**', value='_usage: kick <member> [grund]_', inline=False)
        help_commands_all.add_field(name='**Unban**', value='_usage: unban <member>_', inline=False)
        help_commands_all.add_field(name='**Mute**', value='_usage: mute <member> [grund]_', inline=False)
        help_commands_all.add_field(name='**Unmute**', value='_usage: unmute <member>_', inline=False)
        help_commands_all.add_field(name='**Broadcast**', value='_usage: br <text>_', inline=False)
        help_commands_all.add_field(name='**Clear**', value='_usage: clear <zahl>_', inline=False)
        help_commands_all.add_field(name='**Nickname**', value='_usage: nick <member> <nickname>_', inline=False)
        help_commands_all.add_field(name='**Setprefix**', value='_usage: setprefix <prefix>_', inline=False)
        help_commands_all.add_field(name='**Userinfo**', value='_usage: userinfo <member>_', inline=False)
        help_commands_all.add_field(name='**Stop**', value='_usage: stop_', inline=False)
        help_commands_all.add_field(name='**Unicode**', value='_usage: unicode <emoji>_', inline=False)
        help_commands_all.set_footer(text='<> = Nötig | [] = Nicht Nötig')

        await ctx.message.delete()
        await ctx.send(embed=help_commands_all)

    @help.command()
    async def everyone(self, ctx):
        # commands für alle
        help_command_for_all = discord.Embed(title='**Help Everyone**', description='Settings | Help', color=discord.Color.dark_blue())
        help_command_for_all.set_thumbnail(url='https://i.ibb.co/5Bt2bM9/Neon-Photo-Editor-20200706-144711323.jpg')
        help_command_for_all.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url_as(size=512))
        help_command_for_all.add_field(name='**Botinfo**', value='_usage: botinfo_', inline=False)
        help_command_for_all.add_field(name='**Help**', value='_usage: help <category>_', inline=False)
        help_command_for_all.add_field(name='**Ping**', value='_usage: ping_', inline=False)
        help_command_for_all.set_footer(text='<> = Nötig | [] = Nicht Nötig')

        await ctx.message.delete()
        await ctx.send(embed=help_command_for_all)

    @help.command()
    async def moderation(self, ctx):
        # moderations commands
        help_command_mod = discord.Embed(title='**Help Moderation**', description='Setting | Help', color=discord.Color.dark_blue())
        help_command_mod.set_thumbnail(url='https://i.ibb.co/5Bt2bM9/Neon-Photo-Editor-20200706-144711323.jpg')
        help_command_mod.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url_as(size=512))
        help_command_mod.add_field(name='**Ban**', value='_usage: ban <member> [Grund]_', inline=False)
        help_command_mod.add_field(name='**Kick**', value='_usage: kick <member> [Grund]_', inline=False)
        help_command_mod.add_field(name='**Unban**', value='_usage: unban <member>_', inline=False)
        help_command_mod.add_field(name='**Mute**', value='_usage: mute <member> [grund]_', inline=False)
        help_command_mod.add_field(name='**Unmute**', value='_usage: unmute <member>_', inline=False)
        help_command_mod.set_footer(text='<> = Nötig | [] = Nicht Nötig')

        await ctx.message.delete()
        await ctx.send(embed=help_command_mod)

    @help.command()
    async def administrator(self, ctx):
        # adminstrator commands
        adminstrator = discord.Embed(title='**Help Administrator**', description='Settings | Help', color=discord.Color.dark_blue())
        adminstrator.set_thumbnail(url='https://i.ibb.co/5Bt2bM9/Neon-Photo-Editor-20200706-144711323.jpg')
        adminstrator.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url_as(size=512))
        adminstrator.add_field(name='**Broadcast**', value='_usage: br <text>_', inline=False)
        adminstrator.add_field(name='**Clear**', value='_usage: clear <zahl>_', inline=False)
        adminstrator.add_field(name='**Nickname**', value='_usage: nick <member> <nickname>_', inline=False)
        adminstrator.add_field(name='**Setprefix**', value='_usage: setprefix <prefix>_', inline=False)
        adminstrator.add_field(name='**Userinfo**', value='_usage: userinfo <member>_', inline=False)
        adminstrator.set_footer(text='<> = Nötig | [] = Nicht Nötig')

        await ctx.message.delete()
        await ctx.send(embed=adminstrator)

    @help.command()
    async def owner(self, ctx):
        # owner commands
        owner = discord.Embed(title='**Help Owner**', description='Settings | Help', color=discord.Color.dark_blue())
        owner.set_thumbnail(url='https://i.ibb.co/5Bt2bM9/Neon-Photo-Editor-20200706-144711323.jpg')
        owner.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url_as(size=512))
        owner.add_field(name='**Stop**', value='_usage: stop_', inline=False)
        owner.add_field(name='**Unicode**', value='_usage: unicode <emoji>_', inline=False)
        owner.set_footer(text='<> = Nötig | [] = Nicht Nötig')

        await ctx.message.delete()
        await ctx.send(embed=owner)

    
        

def setup(client):
    client.add_cog(HelpCommand(client))