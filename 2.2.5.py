import datetime
YY, mm, dd = 2016, 4, 20
#YY, mm, dd = int(input().strip())
#days = int(input())
days = 14
data = datetime.datetime(year = YY, month = mm, day = dd) + datetime.timedelta(days)
print(data)
print(data.year, data.month, data.day)