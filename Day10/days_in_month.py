
def is_leap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return True

def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    leap_year = is_leap(year)
    if leap_year and month == 2:
        return 29
    return month_days[month-1]

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
days = days_in_month(year=year,month=month)
print(f"Total days in {month} month of year {year} are {days} days.")
