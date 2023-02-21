from decimal import Decimal
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    
query_name = input()
l = student_marks[query_name]
average = Decimal(sum(l)/len(l))
print(round(average,2))
