#!/usr/bin/env python3
"""Project Euler, Problem 19."""


def leap_year(year):
    """Return True if specified year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_since(day, month, year):
    """Return the number of days from specified date since 1 Jan 1900."""
    days = 0

    # Number of days between 1 Jan 1990 and start of specified year.
    for y in range(1900, year):
        if leap_year(y):
            days += 366
        else:
            days += 365

    # Number of days between start of specified year and start of specified
    # month.
    for m in range(1, month):
        if m in (1, 3, 5, 7, 8, 10, 12):
            days += 31
        elif m == 2:
            if leap_year(year):
                days += 29
            else:
                days += 28
        else:
            days += 30

    # Number of days between start of specified month and specified day.
    days += day - 1

    return days


def day_of_week(day, month, year):
    """Return the day of the week as an integer between 1 and 7."""
    days = days_since(day, month, year)
    return (days + 2) % 7  # 1 Jan 1900 was a Monday.


if __name__ == '__main__':
    num_sundays = sum(day_of_week(day=1, month=m, year=y) == 0
                      for m in range(1, 13) for y in range(1901, 2001))
    print(num_sundays)
