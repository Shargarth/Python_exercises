laskuri = 0
luvut = []

print("Anna kymmenen lukua, tulostan niistä suurimman ja pienimmän")
while laskuri < 10:
    luku = float(input("Anna luku: "))
    luvut.append(luku)
    laskuri += 1

luvut.sort()

print("Pienin:", luvut[0], "Suurin:", luvut[len(luvut) -1] )