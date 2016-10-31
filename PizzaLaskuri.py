import math
#Halkaisija on senteissa, hinta euroissa
def hintaLaskuri(halkaisija, hinta):
    pizzanPintaAla = math.pi * halkaisija ** 2
    hintaPerNelioCm = hinta / pizzanPintaAla
    return  hintaPerNelioCm

ekanHalkaisija = float(input("Ensimmäisen pizzan halkaisija: "))
ekanHinta = float(input("Ensimmäisen pizzan hinta: "))
ekanPizzanHintaPerNelioCm = hintaLaskuri(ekanHinta, ekanHalkaisija)

tokanHalkaisija = float(input("Toisen pizzan halkaisija: "))
tokanHinta = float(input("Toisen pizzan hinta: "))
tokanPizzanHintaPerNelioCm = hintaLaskuri(tokanHalkaisija, tokanHinta)


if(ekanPizzanHintaPerNelioCm < tokanPizzanHintaPerNelioCm):
    print("Ensimmäinen pizza on edullisempi ")
elif (tokanPizzanHintaPerNelioCm < ekanPizzanHintaPerNelioCm):
    print("Toinen pizza on edullisempi")
else:
    print("Pizzat ovat saman hintaisia")