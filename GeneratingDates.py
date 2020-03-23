from datetime import *

dates = open("dates.txt", "w")
primary_date = date(2012, 2, 1)
while primary_date < date.today():
    #print(primary_date)
    dates.write(str(primary_date) + "T19:06:32" + '\n')
    primary_date = primary_date + timedelta(days=1)
dates.close()


