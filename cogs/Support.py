from codingdevil import cur_date, cur_time
import discord
from discord.ext import commands

class CD_Support(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        for channel in member.guild.text_channels:
            if channel.name == "join-leave":
                embed = discord.Embed(
                    title = ":inbox_tray: Member Joined",
                    description = f"``User`` : **{member}**\n``Display Name`` : **{member.display_name}**\n``ID`` : **{member.id}**\n``Account Creation Date`` : **{member.created_at}**",
                    color = discord.Color.green()
                )
                embed.set_thumbnail(url=member.avatar_url)
                await channel.send(embed=embed)

        if member.guild.id == 555787450765541387:
            role = discord.utils.get(member.guild.roles, name="Members")
            await member.add_roles(role)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        for channel in member.guild.text_channels:
            if channel.name == "join-leave":
                embed = discord.Embed(
                    title = ":outbox_tray: Member Left",
                    description = f"``User`` : **{member}**\n``Display Name`` : **{member.display_name}**\n``ID`` : **{member.id}**\n``Account Creation Date`` : **{member.created_at}**",
                    color = discord.Color.red()
                )
                embed.set_thumbnail(url=member.avatar_url)
                await channel.send(embed=embed)

    @commands.command()
    async def server(self, ctx, mode=None, query=None, is_private:bool=None):
        if mode == "enable" and query == "memberlog" and  is_private == None:
            guild = ctx.guild
            await guild.create_text_channel("join-leave")
            for channel in guild.text_channels:
                if channel.name == "join-leave":
                    await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        
        elif mode == "enable" and query == "memberlog" and is_private == True:
            guild = ctx.guild
            await guild.create_text_channel("join-leave")
            for channel in guild.text_channels:
                if channel.name == "join-leave":
                    await channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)

        elif mode == "disable" and query == "memberlog" and is_private == None:        
            guild = ctx.guild
            for channel in guild.text_channels:
                if channel.name == "join-leave":
                    await channel.delete()

        elif mode == None and query == None and is_private == None:
            emote = "<:error:779707707552038932>"
            embed = discord.Embed(
                title = f"{emote} Error",
                description = "``Reason`` : Missing required arguments." ,
                color = discord.Color.green()
            )
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Timestamp: {cur_time()} || {cur_date()}")
            await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def serverlist(self, ctx):
        count = 1
        await ctx.send("Server List :")
        for guild in self.client.guilds:
            await ctx.send(f"{count}) {guild}")
            count = count + 1

def setup(client):
    client.add_cog(CD_Support(client))