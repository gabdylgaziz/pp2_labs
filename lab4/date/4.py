import datetime

d1 = datetime.datetime(2022,2,26,23,59,59)
d2 = datetime.datetime(2022,2,25,23,59,59)

print((d1-d2).total_seconds())