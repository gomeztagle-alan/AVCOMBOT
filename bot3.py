import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('NzI3NTg2NDA0NTM1ODk0MDU2.XwEbjA.3Iiqwq6ZLUS9sytWY7xwF3hEc3c')