s = "6musa12 5kazım"
def baslık(m):
    liste= m.split()
    
    for i in range(len(liste)):
        if liste[i][0].isalpha():
            a = liste[i].title()
            
        else:
            b = liste[i]
            
    return a +" " + b

print(baslık(s))


                                                                                                                                                                                                                                                            

