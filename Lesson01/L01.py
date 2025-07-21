# №2
#
# a = int(input())
# hours = a // 3600 % 24
# minutes = a // 60 % 60
# seconds = a % 60
# print(hours, minutes, seconds)

# №3
#
# a = int(input())
# b = str(a)
# print(int(b) + int(b * 2) + int(b * 3))

# №6

a = int(input())
b = int(input())
k = 1
while a < b:
    a = a * 0.1 + a
    k += 1
print(k)