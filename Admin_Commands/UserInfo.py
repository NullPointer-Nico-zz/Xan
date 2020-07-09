import discord
from discord.ext import commands


class UserInfo(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        if ctx.message.author.guild_permissions.administrator:
            if not member:
                await ctx.message.delete()
                await ctx.send('**Bitte geb ein User an von den du Infos sehen willst!**')
            else:
                rollen = ''
                for role in member.roles:
                    if not role.is_default():
                        rollen += f'{role.mention} \r\n'
                await ctx.message.delete()
                userinfo = discord.Embed(title='**UserInfo**', description=f'UserInfo {member.mention}', color=discord.Color.dark_red())
                userinfo.set_thumbnail(url=member.avatar_url)
                userinfo.add_field(name='**Name**', value=f'{member.display_name}', inline=True)
                userinfo.add_field(name='**Server Join**', value=f"{member.joined_at.strftime('%d/%m/%Y, %H:%M:%S')}", inline=True)
                userinfo.add_field(name='**Discord Join**', value=f"{member.created_at.strftime('%d/%m/%Y, %H:%M:%S')}", inline=True)
                if rollen:
                    userinfo.add_field(name='**Member Roles**', value=rollen, inline=True)

                if member.bot:
                    userinfo.add_field(name='**Bot**', value='True', inline=True)
                else:
                    userinfo.add_field(name='**Bot**', value='False', inline=True)

                if member.activity:
                    userinfo.add_field(name='**Activity**', value=member.activity.name, inline=True)
                else:
                    userinfo.add_field(name='**Activity**', value='No Activity', inline=True)
                userinfo.set_footer(text=ctx.message.author, icon_url=ctx.author.avatar_url_as(size=512)) 
                await ctx.send(embed=userinfo)
        else:
            await ctx.message.delete()
            no_permission = discord.Embed(title='**No Permission**', color=discord.Color.dark_red())
            no_permission.add_field(name='Keine Rechte',
                                    value='```administrator```')
            no_permission.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url_as(size=512))
            await ctx.send(embed=no_permission)

def setup(client):
    client.add_cog(UserInfo(client))