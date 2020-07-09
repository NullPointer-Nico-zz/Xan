import discord

from discord.ext import commands

class MuteCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mute(self, ctx, member: discord.Member = None, *, args=None):
        mute_role = discord.utils.get(ctx.guild.roles, name='Mute')
        if ctx.message.author.guild_permissions.manage_messages:
            if not member:
                await ctx.message.delete()
                await ctx.send('**Bitte geb ein User an den du muten willst!**')
                return
            
            if member == ctx.message.guild.owner:
                await ctx.message.delete()
                await ctx.send(f'_{member.name}_ **ist der Server Owner! Den kann ich nicht Muten!**')
                return

            if member == ctx.message.author:
                await ctx.message.delete()
                await ctx.send(f'_{ctx.message.author.mention}_ **Hast du greade versucht dich selber zu muten? War woll nix!**')
                return

            if not args:
                await ctx.message.delete()
                await member.add_roles(mute_role)
                await ctx.send(f'**User** _{member.name}_ **wurde von** _{ctx.message.author.name}_ **gemuted!**')
            else:
                await ctx.message.delete()
                await member.add_roles(mute_role)
                await ctx.send(f'**User** _{member.name}_ **wurde von** _{ctx.message.author.name}_ **gemuted wegen** ```{args}``` **!**')
        else:
            await ctx.message.delete()
            no_permission = discord.Embed(title='No Permission', color=discord.Color.dark_red())
            no_permission.add_field(name='Keine Rechte', value='```manage messages```')
            no_permission.set_footer(text=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url_as(size=512)}')
            await ctx.send(embed=no_permission)


def setup(client):
    client.add_cog(MuteCommand(client))