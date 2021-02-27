import discord
from discord.ext import commands
from codingdevil import cur_date, cur_time

class Error(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        emote = "<:error:779707707552038932>"
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title = f"{emote}  Error",
                description = f"``Reason :`` **{error}**",
                color = discord.Colour.green()
            )
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title = f"{emote}  Error",
                description = "``Reason :`` **A Bad Argument was passed. Try Again.**",
                color = discord.Color.green()
            )
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed)

        if isinstance(error, commands.NotOwner):
            embed = discord.Embed(
                title = f"{emote}  Error",
                description = "``Reason :`` **You need to be the Bot Owner for this command**",
                color = discord.Color.green()
            )
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Error(client))