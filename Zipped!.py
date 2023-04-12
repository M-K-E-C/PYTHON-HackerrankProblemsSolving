s = input().split()
x = int(s[1])
liste = []
for i in range(x):
    s = list(map(float,input().split()))
    liste.append(s)
for i in zip(*liste):
    print(sum(i)/len(i))
