import json
import discord
import time
from discord.ext import commands
from datetime import date, timedelta


with open("setup/Bot_config.json") as file:
    config = json.load(file)

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=config["prefix"], id=config["id"])
client.remove_command("help")

# ----------- functions ---------------

def ping():
    p = f"{round(client.latency)*100}ms"
    return p

def cur_time():
    t = time.localtime()
    n = time.strftime("%I:%H:%S %p",t)
    return n

def cur_date():
    today = date.today()
    return today

def cur_activity(name,mode):
    if mode == "watching":
        watching = discord.ActivityType.watching
        activity = discord.Activity(name=name, type=watching)
        return activity

    elif mode == "playing":
        playing = discord.ActivityType.playing
        activity = discord.Activity(name=name, type=playing)
        return activity

def cur_guilds():
    i = len(client.guilds)
    return i

def version():
    v = config["version"]
    return v
    
# ----------- Login ---------------

@client.event
async def on_ready():
    me = await client.fetch_user(config["id"])
    print(f"Logged in at {cur_time()}")
    await me.send(f"``` Client Booted || No Error \n Time: {cur_time()} \n Date: {cur_date()}```")
    await client.change_presence(activity=cur_activity(f"{cur_guilds()} Guilds","watching"))

# ------------- Cogs ---------------

intial_extensions = [
                        "cogs.Basic",
                        "cogs.Support",
                        "cogs.Error",
                        "cogs.Mod",
                    ]

for extension in intial_extensions:
    client.load_extension(extension)
    print(f"Loaded: {extension}")

# -------- Manual Cog Control ----------
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        cog = f"cog.{extension}"
        client.load_extension(extension)
        await ctx.send(f"Loaded Cog: {extension}")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        cog = f"cog.{extension}"
        client.unload_extension(extension)
        await ctx.send(f"Unloaded Cog: {extension}")
    except Exception as e:
        await ctx.send(f"Error: {e}")


client.run(config["token"])