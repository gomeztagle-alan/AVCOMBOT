import datetime
import pytz

unaware = datetime.datetime(2011, 8, 15, 8, 15, 12, 0)
aware = datetime.datetime(2011, 8, 15, 8, 15, 12, 0, pytz.UTC)

print(unaware.strftime("%d%H"))

now_aware = pytz.utc.localize(unaware)
print(now_aware.strftime("%d%H"))
print(aware == now_aware)


d = datetime.datetime.now()
timezone = pytz.timezone("America/Los_Angeles")
d_aware = timezone.localize(d)

gmt = timezone('GMT')
print("Time in GMT:", datetime.now(gmt))