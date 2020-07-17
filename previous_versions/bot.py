import discord
from discord.ext import commands
from datetime import date

bot = commands.Bot(command_prefix= '.')
amr_num = 10
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

bot.amr_active = False
def generate_amr():
    amr_num = 1
    if bot.amr_active:
        return
    today = str(date.today())
    x = today.split('-')
    y = str(amr_num)
    if amr_num < 100:
        y = "0" + y
    elif amr_num < 10:
        y = "00" + y
    amr_num += 1
    result = f"{y}-{x[2]}{x[1]}{x[0][:-2]}"
    return result



@bot.command()
async def amr(ctx):
    await ctx.send(generate_amr())
   ## await ctx.send(".amr [airframe_type] [requested_operation] [base]")




bot.run('NzI3NTg2NDA0NTM1ODk0MDU2.XwEbjA.3Iiqwq6ZLUS9sytWY7xwF3hEc3c')