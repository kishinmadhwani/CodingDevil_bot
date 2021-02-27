import random
import discord

def randomcolor():
    colors = [
        discord.Color.red(),
        discord.Color.green(),
        discord.Color.gold(),
        discord.Color.blue(),
        discord.Color.blurple(),
        discord.Color.greyple(),
        discord.Color.purple(),
        discord.Color.orange(),
        discord.Color.teal(),
        discord.Color.dark_gold(),
        discord.Color.dark_magenta(),
        discord.Color.dark_teal(),
        discord.Color.magenta(),
        ]

    return random.choice(colors)
