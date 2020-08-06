import discord
import asyncio
import sqlite3

from discord.ext import commands
import commandcounter

class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):

        # Seiten anzahl
        pages = 6

        # Cur Pages
        cur_page = 1

        # Haupt Embed
        h = discord.Embed(title='**Help**', description=f'Page **{cur_page}/{pages}**\n⏪ Geh zur ersten Seite\n◀️ Gehe ein Seite zurück\n▶️ Gehe zur nächsten Seite\n⏩ Gehe zur letzen Seite\n\nDieser Help Command gilt nur für dich!', color=discord.Color.dark_blue())
        h.set_thumbnail(url='https://i.ibb.co/5Bt2bM9/Neon-Photo-Editor-20200706-144711323.jpg')

        # Fun Commands
        help_commands_fun = discord.Embed(
                    title='**Help Fun**', description=f'Page **{cur_page}/{pages}**', color=discord.Color.dark_blue())
        help_commands_fun.set_author(
                    name=ctx.author.name, icon_url=ctx.author.avatar_url_as(size=512))
        help_commands_fun.set_thumbnail(
                    url='https://i.ibb.co/5Bt2bM9/Neon-Photo-Editor-20200706-144711323.jpg')
        help_commands_fun.add_field(
                    name='**Cat**', value=f'_usage: cat_', inline=False)
        help_commands_fun.add_field(
                    name='**Dog**', value='_usage: dog_', inline=False)
        help_commands_fun.add_field(
                    name='**Schere Stein Papier**', value='_usage: ssp <schere/stein/papier>_', inline=False)
        help_commands_fun.set_footer(text='<> = Nötig | [] = Nicht Nötig')


        # Commands for all
        help_command_for_all = discord.Embed(
                    title='**Help Everyone**', description=f'Page **{cur_page}/{pages}**', color=discord.Color.dark_blue())
        help_command_for_all.set_thumbnail(
                    url='https://i.ibb.co/5Bt2bM9/Neon-Photo-Editor-20200706-144711323.jpg')
        help_command_for_all.set_author(
                    name=ctx.author.name, icon_url=ctx.author.avatar_url_as(size=512))
        help_command_for_all.add_field(
                    name='**Botinfo**', value='_usage: botinfo_', inline=False)
        help_command_for_all.add_field(
                    name='**Help**', value='_usage: help <category>_', inline=False)
        help_command_for_all.add_field(
                    name='**Ping**', value='_usage: ping_', inline=False)
        help_command_for_all.add_field(name='**Feedback**', value='_usage: feedback <nachricht> | fd <nachricht>_')
        help_command_for_all.set_footer(text='<> = Nötig | [] = Nicht Nötig')


        # Mod Commands
        help_command_mod = discord.Embed(
                    title='**Help Moderation**', description=f'Page **{cur_page}/{pages}**', color=discord.Color.dark_blue())
        help_command_mod.set_thumbnail(
                    url='https://i.ibb.co/5Bt2bM9/Neon-Photo-Editor-20200706-144711323.jpg')
        help_command_mod.set_author(
                    name=ctx.author.name, icon_url=ctx.author.avatar_url_as(size=512))
        help_command_mod.add_field(
                    name='**Ban**', value='_usage: ban <member> [Grund]_', inline=False)
        help_command_mod.add_field(
                    name='**Kick**', value='_usage: kick <member> [Grund]_', inline=False)
        help_command_mod.add_field(
                    name='**Unban**', value='_usage: unban <member>_', inline=False)
        help_command_mod.add_field(
                    name='**Mute**', value='_usage: mute <member> [grund]_', inline=False)
        help_command_mod.add_field(
                    name='**Unmute**', value='_usage: unmute <member>_', inline=False)
        help_command_mod.set_footer(text='<> = Nötig | [] = Nicht Nötig')


        # Admin Commands
        adminstrator = discord.Embed(
                    title='**Help Administrator**', description=f'Page **{cur_page}/{pages}**', color=discord.Color.dark_blue())
        adminstrator.set_thumbnail(
                    url='https://i.ibb.co/5Bt2bM9/Neon-Photo-Editor-20200706-144711323.jpg')
        adminstrator.set_author(name=ctx.author.name,
                                        icon_url=ctx.author.avatar_url_as(size=512))
        adminstrator.add_field(name='**Broadcast**',
                                    value='_usage: br <text>_', inline=False)
        adminstrator.add_field(
                    name='**Clear**', value='_usage: clear <zahl>_', inline=False)
        adminstrator.add_field(
                    name='**Nickname**', value='_usage: nick <member> <nickname>_', inline=False)
        adminstrator.add_field(
                    name='**Setprefix**', value='_usage: setprefix <prefix>_', inline=False)
        adminstrator.add_field(
                    name='**Userinfo**', value='_usage: userinfo <member>_', inline=False)
        adminstrator.add_field(name='**Welcome Settigns**', value='_usage: welcome help_', inline=False)
        adminstrator.add_field(name='**Log**#', value='_usage: setlog <channel>_', inline=False)
        adminstrator.add_field(name='**Leave Settigns**', value='_usage: leave help_', inline=False)
        adminstrator.set_footer(text='<> = Nötig | [] = Nicht Nötig')


        # Owner Commands
        owner = discord.Embed(
                    title='**Help Owner**', description=f'Page **{cur_page}/{pages}**', color=discord.Color.dark_blue())
        owner.set_thumbnail(
                    url='https://i.ibb.co/5Bt2bM9/Neon-Photo-Editor-20200706-144711323.jpg')
        owner.set_author(name=ctx.author.name,
                                icon_url=ctx.author.avatar_url_as(size=512))
        owner.add_field(name='**Stop**', value='_usage: stop_', inline=False)
        owner.add_field(name='**Unicode**',
                                value='_usage: unicode <emoji>_', inline=False)
        owner.set_footer(text='<> = Nötig | [] = Nicht Nötig')

        # Contet des Help Commands
        Content = [h, help_command_for_all, help_commands_fun, help_command_mod, adminstrator, owner]
        
        # Erstellt msg varibale
        msg = await ctx.send(embed=Content[cur_page-1])

        # addet Reactions
        await msg.add_reaction('⏪')
        await msg.add_reaction('◀️')
        await msg.add_reaction('▶️')
        await msg.add_reaction('⏩')

        # Check für Reaction
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["⏪", "◀️", "▶️", "⏩"]

        while True:
            try:
                await ctx.message.delete()
                reaction, user = await self.client.wait_for('reaction_add', timeout=120, check=check)

                if str(reaction.emoji) == '▶️' and cur_page != pages:
                    cur_page += 1

                    # Updatet die Embeds
                    help_command_for_all.description = f'Page **{cur_page}/{pages}**'
                    help_command_mod.description = f'Page **{cur_page}/{pages}**'
                    help_commands_fun.description = f'Page **{cur_page}/{pages}**'
                    adminstrator.description = f'Page **{cur_page}/{pages}**'
                    owner.description = f'Page **{cur_page}/{pages}**'
                    h.description = f'Page **{cur_page}/{pages}**\n⏪ Geh zur ersten Seite\n◀️ Gehe ein Seite zurück\n▶️ Gehe zur nächsten Seite\n⏩ Gehe zur letzen Seite\n\nDieser Help Command gilt nur für dich!'

                    await msg.edit(embed=Content[cur_page-1])
                    await msg.remove_reaction(reaction, user)

                elif str(reaction.emoji) == '◀️' and cur_page > 1:
                    cur_page -= 1

                    # Updatet die Embeds
                    help_command_for_all.description = f'Page **{cur_page}/{pages}**'
                    help_command_mod.description = f'Page **{cur_page}/{pages}**'
                    help_commands_fun.description = f'Page **{cur_page}/{pages}**'
                    adminstrator.description = f'Page **{cur_page}/{pages}**'
                    owner.description = f'Page **{cur_page}/{pages}**'
                    h.description = f'Page **{cur_page}/{pages}**\n⏪ Geh zur ersten Seite\n◀️ Gehe ein Seite zurück\n▶️ Gehe zur nächsten Seite\n⏩ Gehe zur letzen Seite\n\nDieser Help Command gilt nur für dich!'

                    await msg.edit(embed=Content[cur_page-1])
                    await msg.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "⏪":

                    if cur_page == 1:
                        return
                    elif cur_page == 2:
                        cur_page -= 1

                        # Updatet die Embeds
                        help_command_for_all.description = f'Page **{cur_page}/{pages}**'
                        help_command_mod.description = f'Page **{cur_page}/{pages}**'
                        help_commands_fun.description = f'Page **{cur_page}/{pages}**'
                        adminstrator.description = f'Page **{cur_page}/{pages}**'
                        owner.description = f'Page **{cur_page}/{pages}**'
                        h.description = f'Page **{cur_page}/{pages}**\n⏪ Geh zur ersten Seite\n◀️ Gehe ein Seite zurück\n▶️ Gehe zur nächsten Seite\n⏩ Gehe zur letzen Seite\n\nDieser Help Command gilt nur für dich!'

                        await msg.edit(embed=Content[cur_page-1])
                        await msg.remove_reaction(reaction, user)

                    elif cur_page == 3:
                        cur_page -= 2

                        # Updatet die Embeds
                        help_command_for_all.description = f'Page **{cur_page}/{pages}**'
                        help_command_mod.description = f'Page **{cur_page}/{pages}**'
                        help_commands_fun.description = f'Page **{cur_page}/{pages}**'
                        adminstrator.description = f'Page **{cur_page}/{pages}**'
                        owner.description = f'Page **{cur_page}/{pages}**'
                        h.description = f'Page **{cur_page}/{pages}**\n⏪ Geh zur ersten Seite\n◀️ Gehe ein Seite zurück\n▶️ Gehe zur nächsten Seite\n⏩ Gehe zur letzen Seite\n\nDieser Help Command gilt nur für dich!'

                        await msg.edit(embed=Content[cur_page-1])
                        await msg.remove_reaction(reaction, user)

                    elif cur_page == 4:
                        cur_page -= 3

                        # Updatet die Embeds
                        help_command_for_all.description = f'Page **{cur_page}/{pages}**'
                        help_command_mod.description = f'Page **{cur_page}/{pages}**'
                        help_commands_fun.description = f'Page **{cur_page}/{pages}**'
                        adminstrator.description = f'Page **{cur_page}/{pages}**'
                        owner.description = f'Page **{cur_page}/{pages}**'
                        h.description = f'Page **{cur_page}/{pages}**\n⏪ Geh zur ersten Seite\n◀️ Gehe ein Seite zurück\n▶️ Gehe zur nächsten Seite\n⏩ Gehe zur letzen Seite\n\nDieser Help Command gilt nur für dich!'

                        await msg.edit(embed=Content[cur_page-1])
                        await msg.remove_reaction(reaction, user)

                    elif cur_page == 5:
                        cur_page -= 4

                        # Updatet die Embeds
                        help_command_for_all.description = f'Page **{cur_page}/{pages}**'
                        help_command_mod.description = f'Page **{cur_page}/{pages}**'
                        help_commands_fun.description = f'Page **{cur_page}/{pages}**'
                        adminstrator.description = f'Page **{cur_page}/{pages}**'
                        owner.description = f'Page **{cur_page}/{pages}**'
                        h.description = f'Page **{cur_page}/{pages}**\n⏪ Geh zur ersten Seite\n◀️ Gehe ein Seite zurück\n▶️ Gehe zur nächsten Seite\n⏩ Gehe zur letzen Seite\n\nDieser Help Command gilt nur für dich!'

                        await msg.edit(embed=Content[cur_page-1])
                        await msg.remove_reaction(reaction, user)

                    elif cur_page == 6:
                        cur_page -= 5

                        # Updatet die Embeds
                        help_command_for_all.description = f'Page **{cur_page}/{pages}**'
                        help_command_mod.description = f'Page **{cur_page}/{pages}**'
                        help_commands_fun.description = f'Page **{cur_page}/{pages}**'
                        adminstrator.description = f'Page **{cur_page}/{pages}**'
                        owner.description = f'Page **{cur_page}/{pages}**'
                        h.description = f'Page **{cur_page}/{pages}**\n⏪ Geh zur ersten Seite\n◀️ Gehe ein Seite zurück\n▶️ Gehe zur nächsten Seite\n⏩ Gehe zur letzen Seite\n\nDieser Help Command gilt nur für dich!'

                        await msg.edit(embed=Content[cur_page-1])
                        await msg.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "⏩":

                    if cur_page == 6:
                        return
                    elif cur_page == 5:
                        cur_page += 1

                        cur_page -= 4

                        # Updatet die Embeds
                        help_command_for_all.description = f'Page **{cur_page}/{pages}**'
                        help_command_mod.description = f'Page **{cur_page}/{pages}**'
                        help_commands_fun.description = f'Page **{cur_page}/{pages}**'
                        adminstrator.description = f'Page **{cur_page}/{pages}**'
                        owner.description = f'Page **{cur_page}/{pages}**'
                        h.description = f'Page **{cur_page}/{pages}**\n⏪ Geh zur ersten Seite\n◀️ Gehe ein Seite zurück\n▶️ Gehe zur nächsten Seite\n⏩ Gehe zur letzen Seite\n\nDieser Help Command gilt nur für dich!'

                        await msg.edit(embed=Content[cur_page-1])
                        await msg.remove_reaction(reaction, user)

                    elif cur_page == 4:
                        cur_page += 2

                        # Updatet die Embeds
                        help_command_for_all.description = f'Page **{cur_page}/{pages}**'
                        help_command_mod.description = f'Page **{cur_page}/{pages}**'
                        help_commands_fun.description = f'Page **{cur_page}/{pages}**'
                        adminstrator.description = f'Page **{cur_page}/{pages}**'
                        owner.description = f'Page **{cur_page}/{pages}**'
                        h.description = f'Page **{cur_page}/{pages}**\n⏪ Geh zur ersten Seite\n◀️ Gehe ein Seite zurück\n▶️ Gehe zur nächsten Seite\n⏩ Gehe zur letzen Seite\n\nDieser Help Command gilt nur für dich!'

                        await msg.edit(embed=Content[cur_page-1])
                        await msg.remove_reaction(reaction, user)

                    elif cur_page == 3:
                        cur_page += 3

                        # Updatet die Embeds
                        help_command_for_all.description = f'Page **{cur_page}/{pages}**'
                        help_command_mod.description = f'Page **{cur_page}/{pages}**'
                        help_commands_fun.description = f'Page **{cur_page}/{pages}**'
                        adminstrator.description = f'Page **{cur_page}/{pages}**'
                        owner.description = f'Page **{cur_page}/{pages}**'
                        h.description = f'Page **{cur_page}/{pages}**\n⏪ Geh zur ersten Seite\n◀️ Gehe ein Seite zurück\n▶️ Gehe zur nächsten Seite\n⏩ Gehe zur letzen Seite\n\nDieser Help Command gilt nur für dich!'

                        await msg.edit(embed=Content[cur_page-1])
                        await msg.remove_reaction(reaction, user)

                    elif cur_page == 2:
                        cur_page += 4

                        # Updatet die Embeds
                        help_command_for_all.description = f'Page **{cur_page}/{pages}**'
                        help_command_mod.description = f'Page **{cur_page}/{pages}**'
                        help_commands_fun.description = f'Page **{cur_page}/{pages}**'
                        adminstrator.description = f'Page **{cur_page}/{pages}**'
                        owner.description = f'Page **{cur_page}/{pages}**'
                        h.description = f'Page **{cur_page}/{pages}**\n⏪ Geh zur ersten Seite\n◀️ Gehe ein Seite zurück\n▶️ Gehe zur nächsten Seite\n⏩ Gehe zur letzen Seite\n\nDieser Help Command gilt nur für dich!'

                        await msg.edit(embed=Content[cur_page-1])
                        await msg.remove_reaction(reaction, user)

                    elif cur_page == 1:
                        cur_page += 5

                        # Updatet die Embeds
                        help_command_for_all.description = f'Page **{cur_page}/{pages}**'
                        help_command_mod.description = f'Page **{cur_page}/{pages}**'
                        help_commands_fun.description = f'Page **{cur_page}/{pages}**'
                        adminstrator.description = f'Page **{cur_page}/{pages}**'
                        owner.description = f'Page **{cur_page}/{pages}**'
                        h.description = f'Page **{cur_page}/{pages}**\n⏪ Geh zur ersten Seite\n◀️ Gehe ein Seite zurück\n▶️ Gehe zur nächsten Seite\n⏩ Gehe zur letzen Seite\n\nDieser Help Command gilt nur für dich!'

                        await msg.edit(embed=Content[cur_page-1])
                        await msg.remove_reaction(reaction, user)

                else:
                    await msg.remove_reaction(reaction, user)

            except asyncio.TimeoutError:
                await msg.delete()
                break




def setup(client):
    client.add_cog(HelpCommand(client))
