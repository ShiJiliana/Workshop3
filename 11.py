import math
a = int(input())
a2 = a**2
b = int(input())
b2 = b**2
c = int(input())
c2 = c**2

cos_a = (-a2 + b2 + c2) / (2 * b * c)
angle_a = math.degrees(math.acos(cos_a))

cos_b = (-b2 + a2 + c2) / (2 * a * c)
angle_b = math.degrees(math.acos(cos_b))

cos_c = (-c2 + b2 + a2) / (2 * b * a)
angle_c = math.degrees(math.acos(cos_c))

print(round(angle_a), round(angle_b), round(angle_c))