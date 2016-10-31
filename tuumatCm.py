tuumaSentteina = 2.54

kayttajanArvo = float(input("Anna tuumat, muunnan senttimetreiksi. Jos arvo on negatiivinen, ohjelma loppuu: "))

while  not kayttajanArvo < 0:
    print(kayttajanArvo * tuumaSentteina)

    kayttajanArvo = float(input("Anna tuumat: "))
