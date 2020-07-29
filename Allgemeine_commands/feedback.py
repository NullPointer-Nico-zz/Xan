import discord
import asyncio
from datetime import datetime

from discord.ext import commands

class FeedBack(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["fd"])
    @commands.cooldown(1, 7200, commands.BucketType.user)
    async def feedback(self, ctx, *, args=None):
        if args is None:
            await ctx.send(f"{ctx.message.author.mention} bitte geb ein Feedback zum Bot.")
        elif len(args) < 100:
            await ctx.send(f"{ctx.message.author.mention} dein Feedback muss mindestens 100 Zeiche lang sein. Länge des Feedbacks {len(args)} Zeichen.")
        elif len(args) > 2048:
            await ctx,send(f"{ctx.message.author.mention} dein Feedback darf nur 2048 Zeichen lang sein. Länge des Feedbacks {len(args)} Zeichen.")
        else:
            embed = discord.Embed(title="**Feedback**", color=discord.Color.green())
            embed.add_field(name='Nachricht', value=args, inline=False)
            embed.set_footer(text=f"{ctx.message.author.name} | {ctx.guild.name}", icon_url=ctx.guild.icon_url_as(size=512))

            msg = await ctx.send(embed=embed)
            await asyncio.sleep(3)
            await msg.delete()
            await ctx.send(f"{ctx.message.author.mention} dein Feedback wurde gesendet!")

            for guild in self.client.guilds:
                if guild.name == "➤ Xan Bot | Support":
                    for channel in guild.text_channels:
                        if channel.id == 738067878552535054:
                            await channel.send(embed=embed)

    @feedback.error
    async def feedback_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):

            cooldown = datetime.fromtimestamp(int(error.retry_after)).strftime("%I:%M:%S")

            await ctx.send(f"Du hast ein Cooldown von _**{cooldown}m**_ !")


def setup(client):
    client.add_cog(FeedBack(client))