import discord
from discord.ext import commands
from datetime import datetime
from pytz import timezone


class amr(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active = False
        self.num = 1

    def isPilot(ctx):
        role = discord.utils.get(ctx.guild.roles, name="Pilot")
        if not role in ctx.author.roles:
            return False
        else:
            return True

    def gen_amr_num(self):
        now = datetime.now(timezone('GMT'))
        amr_d = now.strftime("%d%m%y")
        result = str(self.num) + '-' + amr_d

        while len(result) != 10:
            result = "0" + result
        self.num += 1
        return result

    def check_args(self, ctx, *args):
        if len(args) != 7:
            await ctx
            return True
        else:
            return False

    @commands.command()
    async def print_active(self, ctx, *args):
        if (self.check_args(ctx, args)):


        inp = str(args)
        inputs = [x.strip() for x in inp.split(",")]
        result = "AMR#: {}\nPilot Name: {}\nPilot Callsign: {}\nPilot Information: {}\nRequested Operation: {}\nEstimated Duration: {}\nReason: {}\nAircraft: {}\nBase: {}".format(
            self.gen_amr_num(), ctx.author.mention, inputs[0], inputs[1], inputs[2], inputs[3], inputs[4],
            inputs[5], inputs[6])
        await ctx.send(result)

    ## @commands.Cog.listener()
    ##async def on_message(self, ctx):
    ## time.sleep(5)
    ## await ctx.channel.purge()

    @commands.Cog.listener()
    async def on_ready(self):
        print("I'm ready")

def setup(bot):
    bot.add_cog(amr(bot))
