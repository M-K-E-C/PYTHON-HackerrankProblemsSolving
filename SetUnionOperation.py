m = int(input())
a = input()
n = int(input())
b = input()

set1 = set(a.split())
set2 = set(b.split())

set3 = set1.union(set2)

print(len(set3))
