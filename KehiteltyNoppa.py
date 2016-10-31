import random

def heita(tahkojenMaara):
    return random.randint(1,tahkojenMaara)

tahkojenMaara = int(input("Kuinka monta tahkoa nopassa on? "))
heitto = heita(tahkojenMaara)

print(heitto)

while(heitto  < tahkojenMaara):
    heitto = heita(tahkojenMaara)
    print(heitto)
