import datetime

def time_delta(t1, t2):
    tarih = datetime.datetime.strptime(t1,"%a %d %b %Y %X %z")
    tarih2 = datetime.datetime.strptime(t2,"%a %d %b %Y %X %z")
    sonuc = tarih-tarih2

    saniye = sonuc.total_seconds()
    return saniye

t = int(input())

for t_itr in range(t):
    t1 = input()

    t2 = input()

    delta = time_delta(t1, t2)

    print(int(delta))
