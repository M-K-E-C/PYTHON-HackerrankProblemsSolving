ogeA = input()
n = int(input())
setA = set(ogeA.split())
sayac = 0
for i in range(n):
    s = input()
    
    if setA.issuperset(set(s.split())):
        sayac+=1
    
if sayac ==n :
    print(True)
else:
    print(False)
