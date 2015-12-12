#!/usr/bin/env python3
"""Project Euler, Problem 19

Brute force solution.
"""
def is_leap_year(year):
    """Return true if 'year' is a leap year.
    """
    return year % 4 == 0 and not (year % 100 == 0 and not year % 400 == 0)

def days_since(day, month, year):
    """Return the number of days since 1 Jan 1900.
    """
    days = 0

    # number of days between 1 Jan 1990 and start of 'year'.
    for y in range(1900, year):
        if is_leap_year(y):
            days += 366
        else:
            days += 365

    # number of days between start between start of 'year' and start of
    # 'month'.
    for m in range(1, month):
        if m in range(1, 8, 2) or m in range(8, 13, 2):
            days += 31
        elif m == 2:
            if is_leap_year(year):
                days += 29
            else:
                days += 28
        else:
            days += 30

    # number of days between start of month and 'day'
    days += day - 1

    return days

def day_of_week(day, month, year):
    """Return the day of the week as an integer between 1 and 7.
    """
    days = days_since(day, month, year)
    # 1 Jan 1900 was a Monday.
    return (days + 1) % 7

def main():
    """Print the number of Sundays that fell on the first of the month during
    the twentieth century.
    """
    number_of_sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if day_of_week(1, month, year) == 0:
                number_of_sundays += 1

    print(number_of_sundays)


if __name__ == "__main__":
    main()
