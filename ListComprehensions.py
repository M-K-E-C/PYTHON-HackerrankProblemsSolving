i = int(input())
j = int(input())
k = int(input())
n = int(input())
l=[]

for i in range(i+1):
    
    for j in range(j+1):
        
        for k in range(k+1):
            l.append([i,j,k])
            
l1 = []

for i in l:
    if sum(i)!=n:
        l1.append(i)
        
print(l1)
        
