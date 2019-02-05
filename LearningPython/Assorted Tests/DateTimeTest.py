import datetime

# getting datetime
print(datetime.datetime.now())      # 2018-05-29 11:22:06.837643
print(datetime.datetime.today())    # 2018-05-29 11:22:06.837732
# print(datetime.date.now())      # AttributeError: type object 'datetime.date' has no attribute 'now'
print(datetime.date.today())        # 2018-05-29
# print(datetime.time.now())      # AttributeError: type object 'datetime.time' has no attribute 'now'
# print(datetime.time.today())    # AttributeError: type object 'datetime.time' has no attribute 'today'
print(datetime.datetime.fromtimestamp(0))   # 1970-01-01 04:00:00


# Constructing Datetime
# d = datetime.datetime(2018, 5, 0)   # ValueError: day is out of range for month
# d = datetime.datetime(2018, 2, 29)  # ValueError: day is out of range for month
d = datetime.datetime(2018, 2, 28)  # 2018-02-28 00:00:00
print(d)
d = datetime.datetime(2018, 5, 29, 0)   # 2018-05-29 00:00:00
print(d)
# d = datetime.datetime(2018, 5, 29, 24)  # ValueError: hour must be in 0..23
d = datetime.datetime(2018, 5, 29, 15, 45)  # 2018-05-29 15:45:00
print(d)
d = datetime.datetime(2018, 5, 29, 15, 45, 30)  # 2018-05-29 15:45:30
print(d)
d = datetime.datetime(2018, 5, 29, 15, 45, 30, 2500)    # 2018-05-29 15:45:30.002500
print(d)


# Constructing Date
# d = datetime.date(2018, 5, 29, 0)       # TypeError: function takes at most 3 arguments (4 given)
d = datetime.date(2018, 5, 29)      # 2018-05-29
print(d)


# Constructing Time
t = datetime.time(0, 0, 0)  # 00:00:00
print(t)
t = datetime.time(0, 0, 0, 0)   # 00:00:00
print(t)
t = datetime.time(0, 0, 0, 1)   # 00:00:00.000001
print(t)


# Comparison
d1 = datetime.date(2018, 5, 29)
d2 = datetime.date(2018, 5, 28)
d3 = datetime.date(2018, 5, 29)
print(d1 > d2)  # True
print(d1 == d3) # True


# Properties
dt = datetime.datetime.now()
print(type(dt))
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
print(dt.tzinfo)

d = dt.date()
print(type(d))
print(d.year)
print(d.month)
print(d.day)

dt = datetime.datetime.now()
t = dt.time()
print(type(t))
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)


# Time Delta
delta = datetime.timedelta(days=1, weeks=1, hours=1, minutes=1, seconds=1, milliseconds=1, microseconds=1)
print('delta =', delta)     # delta = 8 days, 1:01:01.001001

dt1 = datetime.datetime.now()
dt2 = datetime.datetime.fromtimestamp(0)
delta = dt1 - dt2
print(delta)
print(type(delta))
print(delta.days)
print(delta.seconds)
print(delta.microseconds)

d1 = datetime.date.today()
d2 = datetime.datetime.fromtimestamp(0).date()
delta = d1 - d2
print(delta)
print(type(delta))
print(delta.days)
print(delta.seconds)
print(delta.microseconds)

t1 = datetime.time(1,10, 10)    #3600 + 600 + 10 = 42§0 seconds
t2 = datetime.time(0, 0, 0)
# delta = t1 - t2                 # TypeError: unsupported operand type(s) for -: 'datetime.time' and 'datetime.time'


# STRFTIME
d = datetime.datetime.now()
print(d.strftime('%d %b %Y'))   # 29 May 2018
print(d.strftime('%H:%M:%S'))   # 14:21:55
print(d.strftime('See you on %A, %d of %B in year %Y')) # See you on Tuesday, 29 of May in year 2018


# STRPTIME
s = '29/05/2018'
d = datetime.datetime.strptime(s, '%d/%m/%Y')   # 2018-05-29 00:00:00
print(d)

s = '29/5/2018'
d = datetime.datetime.strptime(s, '%d/%m/%Y')   # 2018-05-29 00:00:00
print(d)

s = '29/05/18'
# d = datetime.datetime.strptime(s, '%d/%m/%Y')   # ValueError: time data '29/05/18' does not match format '%d/%m/%Y'

s = r'29\05\2018'
# d = datetime.datetime.strptime(s, '%d/%m/%Y')   # ValueError: time data '29\\05\\2018' does not match format '%d/%m/%Y'

s = r'29\05\2018'
d = datetime.datetime.strptime(s, '%d\%m\%Y')   # 2018-05-29 00:00:00
print(d)

