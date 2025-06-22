def is_year_leap(year):
    return year % 4 == 0

year = 1990  # Выберите любой год
is_leap = is_year_leap(year)

print(f"ГОД {year}: {is_leap}")
