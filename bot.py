import json
import discord
from discord.ext import commands

with open("config.json") as file:
    config = json.load(file)

client = commands.Bot(command_prefix=config["prefix"], id=config["owner_id"])

# ----------- On Ready ---------------

@client.event
async def on_ready():
    print(f"{client.user} connected to discord.")

# ----- automatic message deleting -----


filtered_words = ["fuck", "chutiya"]
@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()

    await client.process_commands(msg)

# ----- clear command -----


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

# ----- command list command -----


commandlst = ["kick", "clear", "ban/unban", "mute/unmute"]


@client.command()
async def commandlist(ctx):
    p = config["prefix"]
    await ctx.send(f"Use '{p}' before the command")
    for i in commandlst:
        await ctx.send(i)


# ----- kick command -----


@client.command(aliases=['k', 'Kick', 'KICK'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    await ctx.send(member.display_name + "has been ban from the server")
    try:
        await member.send("You have been kicked from the server, Because:"+reason)
    except:
        await ctx.send("Member has their DMs closed")
    await member.kick(reason=reason)

# ----- ban command -----


@client.command(aliases=['b', 'Ban', 'BAN'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    await ctx.send(member.display_name + "has been ban from the server")
    try:
        await member.send("You have been Ban from the "+client.guilds+" server , Because:"+reason)
    except:
        await ctx.send("Member has their DMs closed")
    await member.ban(reason=reason)

# ----- unban command -----


@client.command(aliases=['ub', 'Unban', 'UNBAN'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
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


@client.command(aliases=['m', 'Mute', 'MUTE'])
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(811495106795536384)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " has been muted!")

# ----- unmute command -----


@client.command(aliases=['um', 'Unmute', 'UNMUTE'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(811495106795536384)

    await member.remove_roles(muted_role)

    await ctx.send(member.mention + " has been Unmuted!")

client.run(config["token"])
