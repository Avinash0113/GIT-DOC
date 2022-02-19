import datetime
import pytz



#d = datetime.date(2021,12,31) # O/P: 2021-12-31 , we need to give as same as line-3 pattern  of (year,month,day)
#d = datetime.date(31,12,2021) # ValueError: day is out of range for month
#d = datetime.date(2021,07,31) # SyntaxError: leading zeros in decimal integer literals are not permitted;\n
 # in line-5 in month/day place we can't give the zero       # use an 0o prefix for octal integers
#d = datetime.date(12,31,2021) # ValueError: month must be in 1..12

#print(d)

#tday = datetime.date.today() # O/P: 2021-12-31 by using this inbuilt command we get current date
#print(tday)

# tday = datetime.date.today()
# print(tday.year)  # O/P: 2021    if we use variable.year in print() we get current year

# tday=datetime.date.today()
# print(tday.month)  # O/P: 12    if we use variable.month in print() we get current month

# tday=datetime.date.today()
# print(tday.day)  # O/P: 31    if we use variable.day in print() we get current day


# tday=datetime.date.today()
# print(tday.weekday())  # O/P: 4, monday 0 sunday 6
# print(tday.isoweekday()) # O/P: 5, monday 1 sunday 7


# tday=datetime.date.today()
# tdelta=datetime.timedelta(days=7)
# print(tday+tdelta)  # O/P: 2022-01-07  , we get the date from now after 7 days


# tday=datetime.date.today()
# tdelta=datetime.timedelta(days=7)  #  here in timedelta we can give the days=(whatever we want)
# print(tday-tdelta)  # O/P: 2021-12-24  , we get the date before a week from now


# tday=datetime.date.today()
# tdelta=datetime.timedelta(days=10)  # here iam showing that we can take the days as our wish
# print(tday+tdelta)  # O/P: 2021-12-24  , we get the date before a week from now


# tday=datetime.date.today()
# tdelta=datetime.timedelta(days=7)
# bday=datetime.date(2022,7,19)
# till_bday=bday-tday
# print(till_bday) # o/p: 200 days, 0:00:00 , we get the number of days from today till next coming birthday date
# print(till_bday.days)  # o/p: 200 , we get simpy as 200 by using (.days)in print statement
# print(till_bday.total_seconds())  # o/p: 17280000.0 ,we get the total seconds from toadys date to coming birthday date


# t =datetime.time(6,30,25,20000) # o/p: 06:30:25.020000
# print(t)
#
# t =datetime.time(6,30,25,20000)
# print(t.hour)  # o/p: 6 , we get hour
# print(t.minute) # o/p: 30 , we get minute
# print(t.second)  # o/p: 25 , we get second
# print(t.microsecond)  # o/p: 20000 , we get microsecond

#
# dt = datetime.datetime(2021,12,31,9,45,30,50000)  # o/p: 2021-12-31 09:45:30.050000
# print(dt)


# dt = datetime.datetime(2021,12,31,9,45,30,50000)  # o/p: 2021-12-31
# print(dt.date())

#
# dt = datetime.datetime(2021,12,31,9,45,30,50000)  # # o/p: 09:45:30.050000
# print(dt.time())


# dt=datetime.datetime(2021,12,31,9,30,45,200000)
# tdelta=datetime.timedelta(days=7)  # o/p: 2022-01-07 09:30:45.200000 ,  we get the date after 7 days
# print(dt+tdelta)

#
# dt=datetime.datetime(2021,12,31,9,30,45,200000)
# tdelta=datetime.timedelta(hours=12)  # o/p: 2021-12-31 21:30:45.200000 ,  we get the date after 7 days
# print(dt+tdelta)



# dt=datetime.datetime(2021,12,31,9,30,45,200000) #  here the format will be like: (year,month,day,hour,minute,second,microsecond)
# tdelta=datetime.timedelta(hours=12,days=10)  # o/p: 2022-01-10 21:30:45.200000 ,  we get the date& time after 7 days
# print(dt+tdelta)


# dt_today=datetime.datetime.today()
# dt_now=datetime.datetime.now()
# dt_utcnow=datetime.datetime.utcnow()
# print(dt_today) # o/p: 2021-12-31 17:54:57.786869
# print(dt_now) # o/p: 2021-12-31 17:54:57.786869
# print(dt_utcnow)  # o/p: 2021-12-31 12:24:57.786869



# timezone





