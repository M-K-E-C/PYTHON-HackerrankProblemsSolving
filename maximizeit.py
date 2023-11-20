l = input().split()
k = int(l[0])
m = int(l[1])
max_list = []
for i in range(k):
    liste = input().split()
    liste2 = map(int,liste)
    max_list.append(max(liste2))

total = 0
for i in max_list:
    total+=i*i
    
result = total%m
print(total)
print(result)
    

