nimet = []
for x in range(0,3):
    nimi = input("Anna ryhmäläisen nimi: ")
    nimet.append(nimi)

for nimi in nimet:
    print(nimi)

lopettanut = input("Kuka lopetti kurssin? ")

if lopettanut in nimet:
    nimet.remove(lopettanut)

uusiRyhmalainen = input("Anna uusi ryhmäläinen: ")
nimet.append(uusiRyhmalainen)


toisenRyhmanNimet = ["Timo", "Hannu", "Timi"]

for nimi in toisenRyhmanNimet:
    nimet.append(nimi)



for nimi in nimet:
    print(nimi)