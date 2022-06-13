def calculate_month_and_day_in_year(year, number_of_day, leap=False):
    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

    month = 0
    while number_of_day > 0:
        if month == 1 and leap is True:
            number_of_day = number_of_day - (days[month] + 1)
        else:
            number_of_day = number_of_day - days[month]
        month += 1
        if number_of_day == 0:
            break

    if leap is True and number_of_day == 0:
        day_of_month = days[month - 1] + 1 + number_of_day
    else:
        day_of_month = days[month - 1] + number_of_day

    return year, month, day_of_month


def calculate_number_of_day(month, day, leap=False):
    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

    if month > 2 and leap is True:
        day += 1

    month -= 1
    while month > 0:
        day = day + days[month - 1]
        month -= 1
    return day


def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def calculate_number_of_day_in_year(year, month, day):
    if is_leap_year(year):
        return calculate_number_of_day(month, day, leap=True), 365 + 1
    else:
        return calculate_number_of_day(month, day), 365


def calculate_date(year, month, day, time_shift):
    print(year, month, day, time_shift)


    number_of_day_in_year, days_in_year = calculate_number_of_day_in_year(year, month, day)

    delta = number_of_day_in_year + time_shift - days_in_year
    year_shift = 0
    while delta > 0:
        year_shift += 1
        time_shift = delta
        number_of_day_in_year, days_in_year = calculate_number_of_day_in_year(year + year_shift, 1, 1)
        delta = number_of_day_in_year + time_shift - days_in_year

    if is_leap_year(year + year_shift):
        if year_shift < 1:
            y, m, d = calculate_month_and_day_in_year(year + year_shift, number_of_day_in_year + time_shift,
                                                      is_leap_year(year + year_shift))
        else:
            y, m, d = calculate_month_and_day_in_year(year + year_shift, number_of_day_in_year + time_shift-1,
                                                      is_leap_year(year + year_shift))
    else:
        y, m, d = calculate_month_and_day_in_year(year + year_shift, number_of_day_in_year + time_shift, is_leap_year(year + year_shift))

    print(y, m, d, '\n')

    return y, m, d


if __name__ == '__main__':
    calculate_date(2020, 2, 28, 1)
    calculate_date(2020, 2, 28, 2)
    calculate_date(2020, 2, 28, 3)

    calculate_date(2022, 12, 31, 1)
    calculate_date(2022, 12, 31, 2)
    calculate_date(2022, 12, 31, 3)
    calculate_date(2022, 12, 31, 30)
    calculate_date(2022, 12, 31, 31)
    calculate_date(2022, 12, 31, 32)

    calculate_date(2022, 12, 31, 364)
    calculate_date(2022, 12, 31, 365)
    calculate_date(2022, 12, 31, 366)

    calculate_date(2022, 12, 21, 1)

    calculate_date(2008, 1, 10, 10)
    calculate_date(2020, 6, 29, 8)
