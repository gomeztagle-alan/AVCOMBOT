import discord
from datetime import datetime
from pytz import timezone
from discord.ext import commands

bot = commands.Bot(command_prefix=".")

current_num = 1

def generate_amr_num():
    global current_num
    now = datetime.now(timezone('GMT'))
    amr_d = now.strftime("%d%m%y")
    result = str(current_num) + '-'+ amr_d

    while len(result) != 10:
        result = "0" + result
    current_num += 1
    return result
@bot.event
async def on_ready():
    print("Bot2 is ready")

amr_active = False
@bot.command()
async def request_amr(ctx):
    global amr_active
    if amr_active:
        return
    amr_active = True
    role = discord.utils.get(ctx.guild.roles, name="Pilot")
    if not role in ctx.author.roles:
        await ctx.send(f"Must be a qualifed Pilot to send AMRs, {ctx.author.mention}")
        amr_active = False
        return
    await ctx.send("What aircraft type?")

    msg = await bot.wait_for('message', check=lambda msg: msg.author == ctx.author, timeout=10)
    if not msg:
        await ctx.send("Request timed out")
        amr_active = False
        return
    amr_active = False
    await ctx.send(f"AMR #:{generate_amr_num()}\nPilot:{ctx.author.mention}\nAircraft Type:{msg.content}")
bot.run('NzI3NTg2NDA0NTM1ODk0MDU2.XwEbjA.3Iiqwq6ZLUS9sytWY7xwF3hEc3c')


