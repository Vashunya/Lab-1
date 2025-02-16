from datetime import datetime, timedelta

#1
current_date = datetime.today()
new_date = current_date - timedelta(days=5)
print(new_date.strftime("%Y-%m-%d"))

#2
today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("yesterday:", yesterday.strftime("%Y-%m-%d"))
print("today:", today.strftime("%Y-%m-%d"))
print("tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#3
now = datetime.now()
without_microseconds = now.replace(microsecond=0)
print(now)
print(without_microseconds)

#4
date1 = datetime(2024, 2, 10, 12, 30, 0)
date2 = datetime(2024, 2, 14, 15, 45, 30)
diff_seconds = abs((date2 - date1).total_seconds())
print(diff_seconds)

