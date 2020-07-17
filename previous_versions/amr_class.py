import discord
from discord.ext import commands
from pytz import timezone
from datetime import datetime

current_num = 1
class amr:
    def __init__(self, pilot, callsign, information, operation, duration, reason, aircraft, base):
        self.pilot = pilot
        self.callsign = callsign
        self.information = information
        self.operation = operation
        self.duration = duration
        self.reason = reason
        self.aircraft = aircraft
        self.base = base

    def generate_amr_num(self):
        global current_num
        now = datetime.now(timezone('GMT'))
        amr_d = now.strftime("%d%m%y")
        result = str(current_num) + '-' + amr_d

        while len(result) != 10:
            result = "0" + result
        current_num += 1
        return result

    def make_string(self):
        #TO-DO: Set up and test result statement
        result = "AMR#: {}\nPilot Name: {}\nPilot Callsign: {}\nPilot Information: {}\nRequested Operation: {}\nEstimated Duration: {}\nReason: {}\nAircraft: {}\nBase: {}".format(self.generate_amr_num(), self.pilot, self.callsign, self.information, self.operation, self.duration, self.reason, self.aircraft, self.base)
        return result

