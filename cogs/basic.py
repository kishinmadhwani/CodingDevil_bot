import discord
from discord.ext import commands
from codingdevil import cur_date, cur_time

class CD_basic(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # ----- whois command -----


@client.command(aliases=['Whois', 'info', 'user'])
@commands.has_permissions(kick_members=True)
async def whois(self,ctx, member: discord.Member):
    embed = discord.Embed(title = member.display_name , discription = member.mention ,color = discord.Color.dark_grey())
    embed.add_field(name = "ID",value = member.id,inline=True)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

# ----- poll command -----


@client.command(aliases = ["pl"])
async def poll(self,ctx,*,msg):
    channel = ctx.channel
    try:
        main_heading,op = msg.split(",")
        op1,op2 = op.split("or")
        txt = f"React with 1️⃣ for {op1} or 2️⃣ for {op2}"
    except:
        await channel.send("Correct Syntax: txt,[choice1] or [choice2]")
        return

    embed = discord.Embed(title= main_heading,description= txt,colour = discord.Color.red())
    message_ = await channel.send(embed=embed)
    await message_.add_reaction("1️⃣")
    await message_.add_reaction("2️⃣")
    await ctx.message.delete()

# ------- Bot Latency -----------

@client.command()
async def ping(ctx):
    await ctx.send(f"**Ping: {round(client.latency*100)}ms**")


def setup(client):
    client.add_cog(CD_basic(client))