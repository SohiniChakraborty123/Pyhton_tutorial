# datetime module is one of the module in python.
# it is build in module that work date as well as time
# it can be catogarized into 6 main classes
# date
#time
# datetime
# timedelta


from datetime import date
my_date=date(1999,6,30)
print("My birthday is",my_date)

# get the current date
from datetime import date
today=date.today()
print("Today date is",today)

# get the current year, month,date

from datetime import date
today_date=date.today()# date object of current date
print("Current year",today_date.year)
print("Current month :",today_date.month)
print("current day",today_date.day)

# get the date from timestamp

from datetime import datetime
date_time= datetime.fromtimestamp(1889898988)
print(date_time)

# get hours minute and second
from datetime import time
Time=time(11,34,56)
print("hour",Time.hour)
print("minute",Time.minute)
print("second",Time.second)


# Get current date and time
from datetime import datetime
today=datetime.now()# calling now function
print("Current date and time is",today)

# Convert python date into string:
from datetime import datetime as dt
now=dt.now()
string=dt.isoformat(now)
print(string)
print(type(string))