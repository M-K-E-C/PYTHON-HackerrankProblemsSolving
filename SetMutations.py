sA = int(input())
setA = set(map(int,input().split()))
sN = int(input())
def Operations():
    global result
    s = input().split()
    setN = set(map(int,input().split()))
    o1= s[0]
    if s[0] == "update":
        setA.update(setN)
    elif s[0] == "intersection_update":
        setA.intersection_update(setN)
    elif s[0] == "difference_update":
        setA.difference_update(setN)
    elif s[0] == "symmetric_difference_update":
        setA.symmetric_difference_update(setN)
    result = sum(setA)
    return result
for i in range(sN):
    Operations()
print(result)
    
