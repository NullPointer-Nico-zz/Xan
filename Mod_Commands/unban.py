import discord
from discord.ext import commands


class unbanCommand(commands.Cog):
    def __int__(self, client):
        self.client = client

    @commands.command()
    async def unban(self, ctx, *, member=None):
        if ctx.message.author.guild_permissions.ban_members:
            if not member:
                await ctx.message.delete()
                await ctx.send('**Bitte geb ein User an den du entbannen willst!**')
            else:
                await ctx.message.delete()
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split('#')

                for ban_entry in banned_users:
                    user = ban_entry.user

                    if(user.name, user.discriminator) == (member_name, member_discriminator):
                        await ctx.guild.unban(user)
                        await ctx.send(f'**Der User** ```{user.name}#{user.discriminator}``` **wurde entbannt von** _{ctx.message.author.display_name}_ **entbannt!**')
                        return

        else:
            await ctx.message.delete()
            no_permission = discord.Embed(title='No Permission', color=discord.Color.dark_red())
            no_permission.add_field(name='Keine Rechte', value='```ban members```')
            no_permission.set_footer(text=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url_as(size=512)}')
            await ctx.send(embed=no_permission)


def setup(client):
    client.add_cog(unbanCommand(client))
