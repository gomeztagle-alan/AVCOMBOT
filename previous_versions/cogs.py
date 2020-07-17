class amr(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._current_num = 1
        self._request_active = False
        self._requests = {}

    def generate_amr_num(self):
        now = datetime.now(timezone('GMT'))
        amr_d = now.strftime("%d%m%y")
        result = str(self._current_num) + '-' + amr_d
        while len(result) != 10:
            result = "0" + result
        self._current_num += 1
        return result
    # AMR  #:
    # Pilot
    # name:
    # Pilot
    # callsign:
    # Pilot
    # information:
    # Requested
    # Operation:
    # Estimated
    # Duration:
    # Reason:
    # Aircraft:
    # Departure
    # Base:

class request:



