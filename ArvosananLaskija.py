arvosanojenMaara = int(input("Kuinka monen arvosanan keskiarvo lasketaan? "))
summa = 0
laskuri = 0

while laskuri < arvosanojenMaara:
    arvosana = int(input("Anna arvosana: "))
    summa += arvosana
    laskuri += 1

keskiarvo = summa / arvosanojenMaara

print("Keskiarvo:",keskiarvo)
