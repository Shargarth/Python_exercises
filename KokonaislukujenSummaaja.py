print("Ohjelmassa annetaan kokonaislukuja kunnes niiden summa on >= 10: ")

kayttajanLuku = int(input("Anna kokonaisluku: "))
summa = kayttajanLuku
while summa < 10:
    kayttajanLuku = int(input("Anna kokonaisluku: "))
    summa += kayttajanLuku


print("Summa:", summa)