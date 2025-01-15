a = int(input())

for _ in range(a):  
    m = int(input()) 
    n = int(input()) 
    answer = [x for x in range(1, n+1)] 
    for k in range(m): 
        for i in range(1, n): 
            answer[i] += answer[i-1]
    print(answer[-1])