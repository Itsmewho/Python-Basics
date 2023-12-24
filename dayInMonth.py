# get user input with day and year.
# check the input
# def days_in_month():
# month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# check days in month Check for leap year for Februari.

year = int(input("Please enter an year:\n"))  # Enter a year
month = int(input("Please enter an month:\n"))  # Enter a month


def check_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True
    else:
        return False


check_leap(year)


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and check_leap(year):
        return 29
    else:
        return month_days[month - 1]


days = days_in_month(year, month)

print(f"The year of {year} and the {month} has {days} in it")
