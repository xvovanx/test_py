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

# 1.12 -6
a = int(input())
if a == 0:
    print(str(a) + ' программистов')
elif a == 1:
    print(str(a) + ' программист')
elif a == 2:
    print(str(a) + ' программиста')
elif a == 3:
    print(str(a) + ' программиста')
elif a == 4:
    print(str(a) + ' программиста')
elif a == 5:
    print(str(a) + ' программистов')
elif a == 6:
    print(str(a) + ' программистов')
elif a == 7:
    print(str(a) + ' программистов')
elif a == 8:
    print(str(a) + ' программистов')
elif a == 9:
    print(str(a) + ' программистов')
else:
    if a // 10 > 10 and (a // 10) % 10 == 1 and a % 10 ==1:
        print(str(a) + ' программистов')
    elif a // 10 > 10 and a % 10 == 1:
        print(str(a) + ' программист')
    elif a // 10 > 10 and a % 10 > 1:
        print(str(a) + ' программистов')
    elif a // 10 <= 1:
        print(str(a) + ' программистов')
    elif a // 10 > 1 and a % 10 == 0:
        print(str(a) + ' программистов')
    elif a // 10 > 1 and a % 10 == 1:
        print(str(a) + ' программист')
    elif a // 10 > 1 and ((a % 10 > 1) and (a % 10 < 5)):
        print(str(a) + ' программиста')
    elif a // 10 > 1 and a % 10 >= 5:
        print(str(a) + ' программистов')

    a10 = a // 10
    a11 = (a // 10) // 10
    a1 = a % 10
    print(a10, a11, a1)









