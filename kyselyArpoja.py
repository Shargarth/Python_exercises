from random import randint

koneenLuku = randint(1,10)

kayttajanArvaus = int(input("Arvaa luku 1 - 10 välillä: "))

while not kayttajanArvaus == koneenLuku:
    if koneenLuku < kayttajanArvaus:
        print("Liian suuri \n")
    else:
        print("Liian pieni\n")

    kayttajanArvaus = int(input("Arvaa luku: "))
print("Oikein!")