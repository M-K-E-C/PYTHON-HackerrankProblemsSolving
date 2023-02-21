# sayilar = [1,3,5,7,9,12,19,21]
# sayac = 0
# deger = 0
# while sayac<len(sayilar):
#     print(sayilar[deger])
#     sayac+=1
#     deger+=1

bas = int(input("lütfen başlangıç değerini giriniz: "))
bitis = int(input("lütfen bitiş değerini  giriniz: "))

i = bas
while i < bitis:
    i+=1
    if i % 2 == 1:
        print(i)

    # if bas % 2 == 1:
    #     print(f"girdiğinis {bas} sayısı ile {bitis} sayısı arasındaki tek sayılar: ",bas+2)
    #     bas+=2
    #
    # elif bas % 2==0:
    #     print(f"girdiğinis {bas} sayısı ile {bitis} sayısı arasındaki tek sayılar : ",bas+1)
    #     bas+=1

# x=100
# while x>0:
#     print(x)
#     x-=1



