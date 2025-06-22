import math

def square(side):
    return math.ceil(side * side) # Вычисляем площадь квадрата и округляем результат вверх

side = 8  # Выберите длину стороны квадрата
area_result = square(side)

print(f"Площадь квадрата со стороной {side}: {area_result}")