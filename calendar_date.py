def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0


class CalendarDate():
    def __init__(self, day: int = 1, month: int = 1, year: int = 1900):
        if year < 1900:
            raise ValueError(
                'can only compute for dates starting from 01/Jan/1900')
        if day < 0 or day > 31 or month < 0 or month > 12:
            raise ValueError('invalid date')
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f'{self.day}/{self.month}/{self.year}'

    def _days_elapsed_from_01Jan1900(self) -> int:
        days_elapsed = 0
        (day, month, year) = (self.day, self.month, self.year)

        while year > 1900:
            if is_leap_year(year - 1):
                days_elapsed += 366
            else:
                days_elapsed += 365
            year -= 1

        while month > 1:
            last_month = month - 1   # no need to consider Jan as month > 1
            if last_month in [1, 3, 5, 7, 8, 10]:
                days_elapsed += 31
            elif last_month in [4, 6, 9, 11]:
                days_elapsed += 30
            elif last_month == 2:
                if is_leap_year(self.year):
                    days_elapsed += 29
                else:
                    days_elapsed += 28

            month -= 1

        days_elapsed += day - 1

        return days_elapsed

    def day_of_week(self) -> int:
        return (self._days_elapsed_from_01Jan1900() + 1) % 7
