x, y, n = map(int, input('Введите стоимость латте в рублях '
                         'с копейками и кол-во заказов: ').split())
x *= n
y *= n
k = y % 100
r = y // 100 + x
print(r, 'руб.', k, 'коп.')