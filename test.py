# # 1.8 -1
# x = int(input())
# print(x % (60 * 24) // 60)
# print(x%60)
#
# # 1.8 -2
# x = int(input())
# h = int(input())
# m = int(input())
# c = h * 60 + m + x
# print(c % (60 * 24) // 60)
# print(c % 60)
#

# 1.10 -1
# a = int(input())
# b = int(input())
# h = int(input())
# if h > b:
#     print('Пересып')
# elif h < a:
#     print('Недосып')
# else:
#     print('Это нормально')

# # 1.10 -2
# a = int(input())
# b = ''
# if a % 400 == 0:
#     b = 'Високосный'
# elif a % 4 == 0 and a % 100 !=0:
#     b = 'Високосный'
# else:
#     b = 'Обычный'
# print(b)

# # 1.12 -1
# import math
# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c)/2
# S = math.sqrt(p * (p - a) * (p - b) * (p - c))
# print(S)

# # 1.12 -2
# a = int(input())
# if (a > -15 and a <= 12) or (a > 14 and a < 17) or (a >= 19):
#     print('True')
# else:
#     print('False')

# # 1.12 -3
# a = float(input())
# b = float(input())
# c = input()
# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '/':
#     if b == 0:
#         print('Деление на 0!')
#     else:
#         print(a / b)
# elif c == '*':
#     print(a * b)
# elif c == 'mod':
#     if b == 0:
#         print('Деление на 0!')
#     else:
#         print(a % b)
# elif c == 'pow':
#         print(a ** b)
# elif c == 'div':
#     if b == 0:
#         print('Деление на 0!')
#     else:
#         print(a // b)

# # 1.12 -4
# import math
# x = input()
# if x == 'треугольник':
#     a = float(input())
#     b = float(input())
#     c = float(input())
#     p = (a + b + c)/2
#     print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
# elif x == 'прямоугольник':
#     a = float(input())
#     b = float(input())
#     print(a * b)
# elif x == 'круг':
#     r = float(input())
#     print(3.14 * r**2)

# # 1.12 -5
# a = int(input())
# b = int(input())
# c = int(input())
# max = 0
# min = 0
# ost = 0
# if a >= b and b <= c:
#     if a >= c:
#         max = a
#         min = b
#         ost = c
#     else:
#         max = c
#         min = b
#         ost = a
# elif (a >= b) and b >= c:
#     max = a
#     min = c
#     ost = b
# elif b >= a and (a <= c):
#     if b >= c:
#         max = b
#         min = a
#         ost = c
#     else:
#         max = c
#         min = a
#         ost = b
# elif (b >= a) and a >= c:
#     max = b
#     min = c
#     ost = a
# print(max)
# print(min)
# print(ost)

# # 1.12 -6
# a = int(input())
# if a < 0:
#     print('Ошибка, введите положительное число')
# elif a % 10 == 1 and tp % 100 != 11:
#     print(a, 'программист')
# elif a % 10 >= 2 and a % 10 <= 4 and (a % 100 < 10 or a % 100 > 20):
#     print(a, 'программиста')
# else:
#     print(a, 'программистов')

# # 1.12 -7
# a = input()
# sum1 = 0
# sum2 = 0
# sum1 = int(a[0]) + int(a[1]) + int(a[2])
# sum2 = int(a[3]) + int(a[4]) + int(a[5])
# if sum1 == sum2:
#     print('Счастливый')
# else:
#     print('Обычный')

# 2.1 -1
i = 1
s = 0
while i != 0:
    i = int(input())
    s = s + i
print(s)

# 2.1 -2

