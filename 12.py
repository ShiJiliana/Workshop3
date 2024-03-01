att = int(input('Кол-во точных передач: '))
comp = int(input('Кол-во попыток: '))
yds = int(input('Пасовые ярды: '))
td = int(input('Кол-во тачдаун-пасов: '))
lnt = int(input('Кол-во перехватов: '))

n1 = ((att/comp) - 0.3) / 0.2
n2 = ((yds/comp) - 3) / 4
n3 = (td/comp) / 0.05
n4 = (0.095 - (lnt/comp)) / 0.04
rating = (n1+n2+n3+n4) * 100 / 6

print('Рейтинг игрока составил:', round(rating, 3))