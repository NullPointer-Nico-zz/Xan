import discord
from discord.ext import commands


class setupCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def setup(self, ctx, *, args=None):
        if ctx.message.author.guild_permissions.administrator:
            if not args:
                await ctx.message.delete()
                setup_help = discord.Embed(
                    title='**Setup Help**', description='Setup Commands', color=discord.Color.purple())
                setup_help.add_field(name='**setup start**',
                                     value='Starte das setup!', inline=True)
                setup_help.add_field(
                    name='**setup remove**', value='Lösche alles von setup!', inline=True)
                setup_help.set_footer(
                    text=ctx.message.author, icon_url=f'{ctx.author.avatar_url_as(size=512)}')
                await ctx.send(embed=setup_help)
            elif args == 'START'.lower():
                await ctx.message.delete()
                if not any(category.name == 'Xan' for category in ctx.guild.categories):
                    cate = await discord.Guild.create_category(self=ctx.guild, name='Xan')
                    await ctx.send('**Category wurde erstellt!**')
                    if not any(channel.name == 'xan-log' for channel in ctx.guild.text_channels):
                        await discord.Guild.create_text_channel(self=ctx.guild, name='Xan Log', category=cate)
                        await ctx.send('**Log wurde erstellt!**')
                        if not any(role.name == 'Mute' for role in ctx.guild.roles):
                            mute_role = await discord.Guild.create_role(self=ctx.guild, name='Mute',
                                                                        permissions=discord.Permissions(
                                                                            add_reactions=True, change_nickname=True,
                                                                            connect=True, create_instant_invite=True,
                                                                            read_messages=True, speak=True,
                                                                            view_channel=True),
                                                                        color=discord.Color.dark_grey())
                            for channles in ctx.guild.channels:
                                await channles.set_permissions(mute_role, send_messages=False)
                            await ctx.send('**Mute Role erstellt!**')

                            for log in ctx.guild.channels:
                                if log.name == 'xan-log':
                                    await channles.set_permissions(discord.Role.is_default, read_messages=False)
                                    await channles.set_permissions(ctx.guild.owner, read_messages=True)
                                    await channles.set_permissions(ctx.guild.owner, send_messages=True)
                                    await log.send('**Log wird bald verfügbar sein!**')
                else:
                    await ctx.send('**Setup wurde schonma ausgeführt!**')
            elif args == 'REMOVE'.lower():
                await ctx.message.delete()
                role = discord.utils.get(ctx.guild.roles, name='Mute')
                log = discord.utils.get(
                    ctx.guild.text_channels, name='xan-log')
                category = discord.utils.get(ctx.guild.categories, name='Xan')
                if role:
                    await role.delete()
                    await ctx.send('**Mute Role wurde entfernt!**')
                else:
                    await ctx.send('**Mute Role gibt es nicht!**')

                if log:
                    await log.delete()
                    await ctx.send('**Log wurde entfernt!**')
                else:
                    await ctx.send('**Log gibt es nicht!**')

                if category:
                    await category.delete()
                    await ctx.send('**Category wurde entfernt!**')
                else:
                    await ctx.send('**Category gibt es nicht!**')
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
    client.add_cog(setupCommand(client))
