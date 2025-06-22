def month_to_season(month):
    seasons = [
        "Зима",  # Декабрь (12), Январь (1), Февраль (2)
        "Весна",  # Март (3), Апрель (4), Май (5)
        "Лето",   # Июнь (6), Июль (7), Август (8)
        "Осень"   # Сентябрь (9), Октябрь (10), Ноябрь (11)
    ]
    
    if month < 1 or month > 12:
        return "Некорректный номер месяца"
    
    # Определяем индекс сезона
    if month in [12, 1, 2]:
        return seasons[0]  # Зима
    elif month in [3, 4, 5]:
        return seasons[1]  # Весна
    elif month in [6, 7, 8]:
        return seasons[2]  # Лето
    else:
        return seasons[3]  # Осень

# Пример использования функции
month_number = 5  # Номер месяца
season = month_to_season(month_number)
print(f"Месяц {month_number}: {season}")
