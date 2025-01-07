# 2309 일곱난쟁이
num = []
for i in range(9):
    num.append(int(input()))

for j in range(8):
    for k in range(j+1, 9):
        if (sum(num) - num[j] - num[k]) == 100:
            findx, findy = j, k
            break

if findx > findy:
    del num[findx]
    del num[findy]
else:
    del num[findy]
    del num[findx]

num.sort()

for n in num:
    print(n)