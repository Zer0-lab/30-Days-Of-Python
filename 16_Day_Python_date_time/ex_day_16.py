from datetime import datetime, date

now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(day)
print(month)
print(year)
print(hour)
print(minute)
print(timestamp)

print(now.strftime("%m/%d/%Y, %H:%M:%S"))

today = date(year=2019, month=12, day=5)
print(today.strftime("%d %B %y")) # 5 December 19

dif_bet_now_newyear = date(year=2027, month=1, day=1) - now.date()
print(dif_bet_now_newyear)

dif_bet_date_now = now.date() - date(year=1970, month=1, day=1)
print(dif_bet_date_now)

