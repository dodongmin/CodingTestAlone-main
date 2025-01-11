# 나무 조각
num = list(map(int, input().split()))
a= 0

for _ in range(4):
    for i in range(4):
        if num[i] > num[i+1]:
            a = num[i]
            num[i] = num[i+1]
            num[i+1] = a
            print(" ".join(map(str, num)))