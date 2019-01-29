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

# 1.10 -2
a = int(input())
b = ''
if a % 400 == 0:
    b = 'Високосный'
elif a % 4 == 0 and a % 100 !=0:
    b = 'Високосный'
else:
    b = 'Обычный'
print(b)
