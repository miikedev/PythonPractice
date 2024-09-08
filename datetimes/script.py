from datetime import datetime

birthday = datetime(1997,9,5,4,20,30)

print(birthday)

print(birthday.year, birthday.month, birthday.day)

print(birthday.hour, birthday.minute, birthday.second)

print(birthday.weekday())

diff = datetime(1997,9,5) - datetime(2006,5,9)

print(diff)

parse_date = datetime.strptime('Jan 1, 2006','%b %d, %Y')

print(parse_date)

parse_date_new = datetime.strftime(datetime.now(),'%b %d, %Y')

print(parse_date_new)