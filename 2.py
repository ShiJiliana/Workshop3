number = int(input('Напишите число от 1 до 86400: '))
hours = number // (60**2)
#Вспомогательная переменая. Остаток секунд недостающих до часа.
p = number % (60**2)
min = p // 60
sec = p % 60
print(hours, ':', min, ':', sec)