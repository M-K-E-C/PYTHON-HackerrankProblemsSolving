m = int(input())
a = input()
n = int(input())
b = input()

set1 = set(a.split())
set2 = set(b.split())

set3 = set1.symmetric_difference(set2)

print(len(set3))
