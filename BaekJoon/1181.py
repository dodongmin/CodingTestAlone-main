num = int(input())

engl = []

for i in range(num):
    lista = input()
    engl.append((lista, len(lista)))
    
engl = list(set(engl)) 
engl.sort(key=lambda x: (x[1], x[0]))

for m,n in engl:
    print(m)