import random
from datetime import date
from calendar_date import CalendarDate, is_leap_year


def test_is_leap_year():
    assert is_leap_year(1901) == False
    assert is_leap_year(1904) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(2000) == True


def day_of_week_on(day, month, year):
    date = CalendarDate(day, month, year)
    return date.day_of_week()


def test_day_of_week(day: int = 1, month: int = 1, year: int = 1900):
    assert day_of_week_on(1, 1, 1900) == 1  # Mon
    assert day_of_week_on(2, 1, 1900) == 2  # Tue
    assert day_of_week_on(3, 1, 1900) == 3  # Wed
    assert day_of_week_on(4, 1, 1900) == 4  # Thu
    assert day_of_week_on(5, 1, 1900) == 5  # Fri
    assert day_of_week_on(6, 1, 1900) == 6  # Sat
    assert day_of_week_on(7, 1, 1900) == 0  # Sun
    assert day_of_week_on(14, 1, 1900) == 0
    assert day_of_week_on(15, 1, 1900) == 1
    assert day_of_week_on(28, 1, 1900) == 0
    assert day_of_week_on(1, 2, 1900) == 4
    assert day_of_week_on(19, 2, 1900) == 1
    assert day_of_week_on(1, 3, 1900) == 4
    assert day_of_week_on(15, 4, 1900) == 0
    assert day_of_week_on(30, 5, 1900) == 3
    assert day_of_week_on(5, 8, 1900) == 0
    assert day_of_week_on(5, 8, 1901) == 1
    assert day_of_week_on(29, 2, 2000) == 2
    assert day_of_week_on(1, 3, 2000) == 3

    # random test
    for _ in range(1000):
        day = random.randint(1, 31)
        month = random.randint(1, 12)
        year = random.randint(1900, 2000)
        try:
            day_of_week = date(day, month, year).isoweekday() % 7
        except:
            continue
        assert day_of_week_on(day, month, year) == day_of_week
