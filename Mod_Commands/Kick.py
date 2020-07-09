import discord
from discord.ext import commands


class KickCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member: discord.Member = None, *, args=None):
        if ctx.message.author.guild_permissions.kick_members:
            if not member:
                await ctx.message.delete()
                await ctx.send(f'**Bitte gebe ein User an den du Kicken willst!**')
            else:
                if member == ctx.message.guild.owner:
                    await ctx.message.delete()
                    await ctx.send(f'**Der User** _{member.display_name}_ **ist der Server Owner! Oh den kannst du Leider nicht Kicken :c!**')
                else:
                    if not member == ctx.message.author:
                        if not args:
                            await ctx.message.delete()
                            await member.kick(reason=args)
                            await ctx.send(f'**User** _{member.display_name}_ **wurde von** _{ctx.message.author.display_name}_ **gekickt!**')
                        else:
                            await ctx.message.delete()
                            await member.kick(reason=args)
                            await ctx.send(f'**User** _{member.display_name}_ **wurde von** _{ctx.message.author.display_name}_ **gekickt wegen** ```{args}``` **!**')
                    else:
                        await ctx.send('**oof hast du versucht dich selbst zu Kicken? Netter Versuch!**')
        else:
            await ctx.message.delete()
            no_permission = discord.Embed(title='No Permission', color=discord.Color.dark_red())
            no_permission.add_field(name='Keine Rechte', value='```kick members```')
            no_permission.set_footer(text=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url_as(size=512)}')
            await ctx.send(embed=no_permission)

def setup(client):
    client.add_cog(KickCommand(client))
