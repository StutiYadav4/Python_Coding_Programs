import datetime

def day_of_the_week(day, month, year):
    date_obj = datetime.date(year, month, day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date_obj.weekday()]


print(day_of_the_week(3, 6, 2023))
print(day_of_the_week(4, 6, 2024))
print(day_of_the_week(1, 1, 2000))
print(day_of_the_week(25, 12, 2022))
