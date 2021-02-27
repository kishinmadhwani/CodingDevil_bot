import discord
from discord.ext import commands
from codingdevil import cur_date, cur_time

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    # ----- kick command -----

    @commands.command(aliases=['k', 'Kick', 'KICK'])
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx, member: discord.Member, *, reason="No reason provided"):
        await ctx.send(member.display_name + "has been ban from the server")
        try:
            await member.send("You have been kicked from the server, Because:"+reason)
        except:
            await ctx.send("Member has their DMs closed")
        await member.kick(reason=reason)

    # ----- ban command -----

    @commands.command(aliases=['b', 'Ban', 'BAN'])
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx, member: discord.Member, *, reason="No reason provided"):
        await ctx.send(member.display_name + " has been ban from the server")
        try:
            await member.send(f"You have been Ban from the {ctx.guild.name} server , Because:"+reason)
        except:
            await ctx.send("Member has their DMs closed")
        await member.ban(reason=reason)

    # ----- unban command -----


    @commands.command(aliases=['ub', 'Unban', 'UNBAN'])
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx, *, member):
        banned_user = ctx.guild.bans()
        member_name, member_disc = member.split('#')

        for banned_entry in banned_user:
            user = banned_entry.user

            if(user.name, user.discriminator) == (member_name, member_disc):

                await ctx.guild.unban(user)
                await ctx.send(member_name + " has been Unbanned!")
                return

        await ctx.send(member+" was not found")

    # ----- mute command -----

    @commands.command(aliases=['m', 'Mute', 'MUTE'])
    @commands.has_permissions(kick_members=True)
    async def mute(ctx, member: discord.Member):
        muted_role = ctx.guild.get_role(811495106795536384)

        await member.add_roles(muted_role)

        await ctx.send(member.mention + " has been muted!")

    # ----- unmute command -----

    @commands.command(aliases=['um', 'Unmute', 'UNMUTE'])
    @commands.has_permissions(kick_members=True)
    async def unmute(ctx, member: discord.Member):
        muted_role = ctx.guild.get_role(811495106795536384)

        await member.remove_roles(muted_role)

        await ctx.send(member.mention + " has been Unmuted!")

    # ----- clear command -----

    @commands.command(aliases=['c'])
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount=2):
        await ctx.channel.purge(limit=amount)



def setup(client):
    client.add_cog(Moderation(client))