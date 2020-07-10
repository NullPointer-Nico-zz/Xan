import discord
from discord.ext import commands


class NickName(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nick(self, ctx, member: discord.Member = None, *, args=None):
        if ctx.message.author.guild_permissions.administrator:
            if not member:
                await ctx.message.delete()
                await ctx.send('**Bitte geb ein Member an von denn du den NickName ändern willst!**')
            else:
                if member == ctx.message.guild.owner:
                    await ctx.send(f'**Oh der User {member} ist ja der Server Owner. Von ihn kann ich leider nicht den NickName ändern :c**')
                else:
                    if not args:
                        await ctx.message.delete()
                        await member.edit(nick=member.name)
                        await ctx.send(f'**Nickname von User** _{member}_ **wurde zu** _{member.name}_ **geändert!**')
                    else:
                        await ctx.message.delete()
                        await member.edit(nick=args)
                        await ctx.send(f'**Nickname von User** _{member}_ **wurde zu** _{args}_ **geändert!**')
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
    client.add_cog(NickName(client))
