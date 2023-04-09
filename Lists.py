N = int(input())
liste = []
for i in range(N):
    command = input().split()
    if command[0]=="insert":
        liste.insert(int(command[1]),int(command[2]))
    elif command[0]=="print":
        print(liste)
    elif command[0]=="append":
        liste.append(int(command[1]))
    elif command[0] == "pop":
        liste.pop()
    elif command[0]=="sort":
        liste.sort()
    elif command[0] == "reverse":
        liste.reverse()
    else:
        if int(command[1]) in liste:
            liste.remove(int(command[1]))
        else:
            pass
