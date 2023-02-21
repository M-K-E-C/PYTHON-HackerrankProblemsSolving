l = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([score,name])
        
l.sort()

nl = []

for i in range(len(l)):
    if l[i][0] != l[0][0]:
        nl.append(l[i])


nl1 = []

for i in range(len(nl)):
    if nl[i][0] == nl[0][0]:
        nl1.append(nl[i][1])
nl1.sort()

for i in nl1:
    print(i)
    
    

