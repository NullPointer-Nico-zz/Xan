import discord
from discord.ext import commands


class BanCommmand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ban(self, ctx, member: discord.Member = None, *, args=None):
        if ctx.message.author.guild_permissions.ban_members:
            if not member:
                await ctx.message.delete()
                await ctx.send(f'**Bitte gebe ein User an den du Ban willst!**')
            else:
                if member == ctx.message.guild.owner:
                    await ctx.message.delete()
                    await ctx.send(f'**Der User** _{member.display_name}_ **ist der Server Owner! Oh den kannst du Leider nicht Bannen :c!**')
                else:
                    if not member == ctx.message.author:
                        if not args:
                            await ctx.message.delete()
                            await member.ban()
                            await ctx.send(f'**User** _{member.name}#{member.discriminator}_ **wurde von** _{ctx.message.author.display_name}_ **gebannt!**')
                        else:
                            await ctx.message.delete()
                            await member.ban(reason=args)
                            await ctx.send(f'**User** _{member.name}#{member.discriminator}_ **wurde von** _{ctx.message.author.display_name}_ **gebannt wegen** ```{args}``` **!**')
                    else:
                        await ctx.message.delete()
                        await ctx.send('**oof hast du dich versucht selber zu bannen? Netter Versuch!**')
        else:
            await ctx.message.delete()
            no_permission = discord.Embed(
                title='No Permission',
                color=discord.Color.dark_red())
            no_permission.add_field(
                name='Keine Rechte',
                value='```ban members```')
            no_permission.set_footer(
                text=f'{ctx.author}',
                icon_url=f'{ctx.author.avatar_url_as(size=512)}')
            await ctx.send(embed=no_permission)


def setup(client):
    client.add_cog(BanCommmand(client))
