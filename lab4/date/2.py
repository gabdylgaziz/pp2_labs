import datetime

x = datetime.datetime.now()
print('yesterday: ',x.year,'.', x.month,'.',x.day - 1, sep='')
print('today: ',x.year,'.', x.month,'.',x.day, sep='')
print('tomorrow: ',x.year,'.', x.month,'.',x.day + 1, sep='')