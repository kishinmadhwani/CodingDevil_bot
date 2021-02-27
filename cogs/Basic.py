import discord
from discord.ext import commands
from codingdevil import cur_date, cur_time, ping
from utility.colors import randomcolor

class CD_basic(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # ----- whois command -----


    @commands.command(aliases=['Whois', 'info', 'user'])
    @commands.has_permissions(kick_members=True)
    async def whois(self,ctx, member: discord.Member):
        embed = discord.Embed(title = member.display_name , discription = member.mention ,color = discord.Color.dark_grey())
        embed.add_field(name = "ID",value = member.id,inline=True)
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    # ----- poll command -----


    @commands.command(aliases = ["pl"])
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

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"**Ping: {ping()}**")

    # ------------ Time Pass ----------------

    @commands.command()
    async def fuck(self, ctx, member:discord.Member=None):
        img = "https://cdn.discordapp.com/attachments/599577010099978241/815210404418551808/images.png"
        embed = discord.Embed(
            title = f"Suck my Dick {member.display_name}",
            description = member.mention,
            color = randomcolor()
        )
        embed.set_image(url=img)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(CD_basic(client))