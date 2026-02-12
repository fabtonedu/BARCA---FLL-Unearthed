from pybricks.hubs import PrimeHub

# Hub inicializálása
hub = PrimeHub()

# Akku feszültség lekérése millivoltban
battery_mv = hub.battery.voltage()

print(battery_mv)

# Feltételezett teljes akku feszültség (Spike Prime esetén kb. 9500 mV)
full_battery_mv = 8400

# Átalakítás százalékra
battery_percent = (battery_mv / full_battery_mv) * 100
battery_percent = int(battery_percent)  # egész számra kerekítés

# Kiírás a terminálra
print("Hub töltöttségi szintje:", battery_percent, "%")
