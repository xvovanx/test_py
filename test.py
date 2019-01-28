# 1.8 -1
x = int(input())

print(x % (60 * 24) // 60)
print(x%60)

# 1.8 -2
x = int(input())
h = int(input())
m = int(input())
c = h * 60 + m + x
print(c % (60 * 24) // 60)
print(c % 60)
