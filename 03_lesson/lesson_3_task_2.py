from smartphone import Smartphone  # Импортируем класс Smartphone из файла smartphone.py

catalog = []

catalog.append(Smartphone("Apple", "iPhone 14", "+79001234567"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79007654321"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79009876543"))
catalog.append(Smartphone("Google", "Pixel 6", "+79005432167"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79002345678"))

for smartphone in catalog:
    print(smartphone)
