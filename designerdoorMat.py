s = "11 33"
string =".|."
s2 = "WELCOME"
a = s.split()
n=int(a[0])
m=int(a[1])

for i in range(1,n,2):
    print((i*string).center(m,"-"))
print(s2.center(m,"-"))

for i in range(n-2,0,-2):
    print((i*string).center(m,"-"))

