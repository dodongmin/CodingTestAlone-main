# 나이순 정렬
j = int(input())

num = []

for i in range(j):
    line = input().split() 
    line[0] = int(line[0])
    num.append((line[0], line[1], i)) 

num.sort(key=lambda x: (x[0], x[2]))

for k,m,n in num:
    print(k,m)