m = int(input())
a = input()
n = int(input())
b = input()

set1 = set(a.split())
set2 = set(b.split())

x = set1.difference(set2)
y = set2.difference(set1)

l = []
for i in x:
    l.append(int(i))
    
for j in y:
    l.append(int(j))


l.sort()

for i in l:
    print(i)

