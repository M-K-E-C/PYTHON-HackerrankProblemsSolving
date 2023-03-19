t = int(input())
for i in range(t):
    sA = int(input())
    ogeA = input()
    setA = set(ogeA.split())
    sB = int(input())
    ogeB = input()
    setB = set(ogeB.split())
   
    if setA.issubset(setB):
        print(True)
    else: 
        print(False)
