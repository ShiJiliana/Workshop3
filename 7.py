# по карте расстояние = диагонали прямоугольника 500*600м
'''
import math
width = 500
long = 600
s = int(math.sqrt(width**2 + long**2))
print(s, 'метр')'''

# 7 - 2 вариант (начало сквера находится примерно на середине квадрата сетки)
import math
width = 450
long = 600
s = int(math.sqrt(width**2 + long**2))
print(s, 'метров')