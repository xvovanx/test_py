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

# # 2.1 -1
# i = 1
# s = 0
# while i != 0:
#     i = int(input())
#     s = s + i
# print(s)

# # 2.1 -2
# a = int(input())
# b = int(input())
# if a >= b:
#     i = a
# else:
#     i = b
# while (i % a == 0 and i % b != 0) or (i % a != 0 and i % b == 0) or (i % a != 0 and i % b != 0):
#     i = i + 1
# print(i)

# # 2.2 -1
# a = True
# s = ''
# while a != False:
#     b = int(input())
#     if b > 100:
#         break
#     if b > 11:
#         s = s + '\n' + str(b)
# print(s)

# # 2.3 -1
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for g in range (c,d+1):
#     print('\t'+str(g),end='')
# print(end='\n')
# for i in range (a,b+1):
#     print(str(i)+'\t',end='')
#     for j in range (c,d+1):
#         print(str(i*j),end='\t')
#     print(end='\n')

# # 2.3 -2
# a = int(input())
# b = int(input())
# s = 0
# kol = 0
# for g in range(a, b+1):
#     if g % 3 == 0:
#         s = s + g
#         kol = kol + 1
# print(s/kol)
#
# # 2.4 -1
# s = input()
# dl = len(s)
# GS = 0
# for i in s:
#     if i in ('G', 'g', 'C', 'c'):
#         GS = GS + 1
# pr = GS/dl * 100
# print(pr)

# # 2.4 -2
# s = 'aaaabbсaa'
# #s = input()
# n = 0
# kod = ''
# sum = 0
# for i in s:
#     if s[n] == s[n+1]:
#        sum = sum + 1
#     else:
#         sum = 0
#         kod = i + kod + str(sum)
# print(kod)
#
# # 2.4 -3
# s = input()
# sp = []
# n = 0
# n1 = 0
# n2 = 0
# sp = s.split()
# ls = len(sp)
# if ls == 1:
#     print(sp[0])
# else:
#     for i in sp:
#         sum = 0
#         n1 = n - 1
#         n2 = n + 1
#         if n2 == ls:
#             sum = int(sp[n1]) + int(sp[0])
#         else:
#             sum = int(sp[n1]) + int(sp[n2])
#         n += 1
#         print(sum, end=' ')

# # 2.4 -4
# s = input()
# sp = []
# sp_new = []
# n = 0
# sp = s.split()
# sp.sort()
# for i in range(1, len(sp)):
#     if sp[i] == sp[i-1]:
#         sp_new.append(sp[i])
#
# sp_new = list(set(sp_new))
# sp_new.sort()
#
# print (' '.join(sp_new))

# # 2.6 -1
# sum = 0
# s = 0
# sum_kvad = 0
# while 0 == 0:
#     s = int(input())
#     sum = s + sum
#     sum_kvad = s ** 2 + sum_kvad
#     if sum == 0:
#         break
# print (sum_kvad)

# # 2.6 -2
# n = int(input())
# sp_new = []
# for i in range (1, n + 1):
#     for k in range (0, i):
#         sp_new.append(i)
#
# print (' '.join(map(str, sp_new[:n])))

# # 2.6 -3
# sl = input()
# s = int(input())
# n = 0
# slp =sl.split()
# slp_s = []
# for i in slp:
#     if s == int(slp[n]):
#         slp_s.append(n)
#     n +=1
# if not slp_s:
#     print ('Отсутствует')
# else:
#     print (' '.join(map(str, slp_s)))

# # 2.6 -4
# n = ''
# m = []
# while True:
#     n = str(input())
#     if n == 'end':
#         break
#     m.append([int(s) for s in n.split()])
# li, lj = len(m), len(m[0])
# new = [[sum([m[i-1][j], m[(i+1)%li][j], m[i][j-1], m[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]
#
# for i in range (li):
#     for j in range (lj):
#         print(new[i][j], end =' ')
#     print()

# 2.6 -5


# # 3.1 -1
# def f(x):
#     if x > 2:
#         return (x - 2) ** 2 + 1
#     elif x <= -2:
#         return 1 - (x + 2) ** 2
#     else:
#         return -x/2
# print (f(1))

# # 3.1 -2
# def modify_list(l):
#     lst = []
#     n = 0
#     for i in l:
#         if i % 2 == 0:
#             lst.append(int(i/2))
#         n += 1
#     l.clear()
#     l[:] = lst
#     return l
# print (modify_list([1, 3, 5, 7]))

# # 3.2 -1
# d = {}
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#     elif key * 2 in d:
#         d[key * 2].append(value)
#     else:
#         d[key * 2] = [value]
# update_dictionary(d, 0, '-5')
# print (d)
# update_dictionary(d, 1, '-1')
# print (d)
# update_dictionary(d, 2, '-2')
# print (d)
# update_dictionary(d, 3, '-3')
# print (d)

# # 3.2 -2
# s = []
# d = {}
# t = str(input())
# for i in t.split():
#     i = i.lower()
#     s.append(i)
#
# s.sort()
# for j in s:
#     if j in d:
#         sum = sum + 1
#         d[j] = (sum)
#     else:
#         sum = 1
#         d[j] = (sum)
#
# for x, y in d.items():
#     print (x, y)

# # 3.2 -3
# def f(x): #для теста функция
#     x = x + 1
#     return x
#
# dict = {}
# list = []
# n = int(input())
# for i in range(0, n):
#     x = int(input())
#     if x in dict:
#         list.append(dict[x])
#     else:
#         dict[x] = f(x)
#         list.append(dict[x])
# print ('\n'.join(map(str, list)))

# # 3.4 -1
# strfull = ''
# n = 0
# with open ('dataset_3363_2.txt', 'r') as ftxt:
#     str1 = ftxt.readline()
#     for i in str1:
#         if i.isalpha():
#            strfull = strfull + i
#         elif i.isdigit():
#             if str1[n+1].isdigit():
#                 num = i
#                 num = num + str1[n+1]
#                 for j in range (1, int(num)):
#                     strfull = strfull + str1[n-1]
#             if str1[n-1].isalpha() and str1[n+1].isalpha():
#                 num = i
#                 for k in range (1, int(num)):
#                     strfull = strfull + str1[n-1]
#         n += 1
#     print (strfull)
#     print (str1)

# 3.4 -2
# strfull = ''
# sum = 0
# str1 = ''
# with open ('dataset_3363_3.txt', 'r') as ftxt:
#     for striped_line in ftxt.readlines():
#         str1 = str1 + striped_line
#     s = []
#     d = {}
#     for i in str1.split():
#         i = i.lower()
#         s.append(i)
#     s.sort()
#     for j in s:
#         if j in d:
#             sum = sum + 1
#             d[j] = (sum)
#         else:
#             sum = 1
#             d[j] = (sum)
#
#     mode = max(d, key=d.get)
#     if mode in d:
#         print (mode, d[mode])
#     print (s)
#     print (d)

# # 3.4 -3
# stritog = []
# sum = 0
# sh = 0
# math = 0
# fiz = 0
# rus = 0
# str1 = []
# s = []
# with open ('dataset_3363_4.txt', 'r') as ftxt:
#     for striped_line in ftxt.readlines():
#         str1.append(striped_line.strip('\n'))
#     for i in str1:
#         n = []
#         for j in i.split(';'):
#             n.append(j)
#         s.append(n)
#     for sr_o in s:
#         m = round(((int(sr_o[1]) + int(sr_o[2]) + int(sr_o[3]))/3),9)
#         sh += 1
#         math = math + int(sr_o[1])
#         fiz = fiz + int(sr_o[2])
#         rus = rus + int(sr_o[3])
#         stritog.append(m)
#         print (m)
#     print (round(math/sh,9), round(fiz/sh,9), round(rus/sh,9))

# # 3.5 -1
# import math
# r = float(input())
# p = 2 * math.pi * r
# print (p)

# # 3.5 -2
# import sys
# print(*sys.argv[1:])

# # 3.6 -1
# import requests
# str1 = ''
# lines = 0
# with open('dataset_3378_2.txt', 'r') as ftxt:
#     for striped_line in ftxt.readlines():
#         str1 = striped_line
# r = requests.get(str1.strip('\n'))
# for i in r.text:
#     if i == '\n':
#         lines += 1
# print(lines)

# # 3.6 -2
# import requests
# str1 = ''
# lines = 0
# with open('dataset_3378_3.txt', 'r') as ftxt:
#     for striped_line in ftxt.readlines():
#         str1 = striped_line
# r = requests.get(str1.strip('\n'))
# file = r.text
# while file[:2] != 'We':
#     b = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + file)
#     file = b.text
#     print(file)
# print(file)

# 3.7 -2



## 3.7 -2
# d_dict = {}
# l_dict = {}
# dl_dict = {}
# ld_dict = {}
# result_code_str = []
# result_code = []
# d = input()
# l = input()
# code_str = input()
# code = input()
# n = 1
# for i in d:
#     d_dict[i] = n
#     n +=1
# n = 1
# for j in l:
#     l_dict[j] = n
#     n +=1
# dl_dict = dict(zip(d_dict, l_dict))
# ld_dict = dict(zip(l_dict, d_dict))
# for i_code in code_str:
#     if i_code in dl_dict:
#         result_code_str.append(dl_dict.get(i_code))
# for j_code in code:
#     if j_code in ld_dict:
#         result_code.append(ld_dict.get(j_code))
#
# print(*result_code_str, sep='')
# print(*result_code, sep='')


# # 3.7 -3
# d_dict = {}
# l_dict = {}
# result = []
#
# d = int(input())
# for i in range(1, d+1):
#     d_str = input()
#     d_dict[d_str.lower()] = (i)
#
# l = int(input())
# for j in range(1, l+1):
#     l_str = input()
#     for u in l_str.split():
#         l_dict[u.lower()] = (j)
#
# for key in l_dict:
#     if key not in d_dict:
#         result.append(key)
# print('\n'.join(result))

# # 3.7 -5
# # не сделал обопботку Пустого класса '-'
# str1 = []
# str2 = []
# lines = 0
# with open('dataset_3380_5.txt', 'r') as ftxt:
#     for striped_line in ftxt.readlines():
#         str1.append(striped_line.strip('\n').split('\t'))
# print(str1)
# rost = 0
# ch = 0
# sred = 0
# d = {}
# for str_line in str1:
#     if int(str_line[0]) not in d:
#        d[int(str_line[0])] = list()
#        d[int(str_line[0])].append(int(str_line[2]))
#        d[int(str_line[0])].append(1)
#     else:
#        d[int(str_line[0])][0] = d[int(str_line[0])][0] + int(str_line[2])
#        d[int(str_line[0])][1] = d[int(str_line[0])][1] + 1
# for key in sorted(d.keys()):
#     print(key, d[key])
# print('_____')
# for key in sorted(d.keys()):
#     d[key] = d[key][0]/d[key][1]
#     print(key, d[key])