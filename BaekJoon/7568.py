# 덩치
num = int(input())
ans = []
answer = []

for _ in range(num):
    a = input().split() 
    a[0], a[1] = int(a[0]), int(a[1])
    ans.append((a[0], a[1])) 


for i in range(num):
    k = 1
    for j in range(num):
        if ans[i][0] < ans[j][0] and ans[i][1] < ans[j][1]:
            k += 1
    print(k, end=' ')