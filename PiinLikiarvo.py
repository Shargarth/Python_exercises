# A on yksikkoympyrä, eli sen keskipiste on origo ja sen säde on 1
#Ympärille piirretään pienin mahdollinen neliö B, joka peittää ympyrän
#Nurkkapisteet tällöin (-1,-1), (1,1), (-1,1), (1,-1)
#Jos neliön sisälle arvotaan pisteitä suuri määrä, osuu niistä ympyrän sisälle
#likimain niin suuri osa kuin ympyrän pinta-ala on neliön pinta-alasta eli pii*r^2 / 4
#Tämä sievenee muotoon pii / 4 koska r = 1

#Arvotaan neliön B sisälle suuri määrä pisteitä, esimerkiksi miljoona
#Olkoon N tämä pisteiden kokonaismäärä

#Jokaisesta neliön sisään arvotusta pisteestä katsotaan onko se ympyrän sisällä.
#Olkoon n pisteiden määrä ympyrän sisällä

# Pätee n / N ~~ pii / 4 jolloin pii = 4n / N

# Kysy käyttäjältä arvottavien pisteiden lukumäärä, jolla lasketaan piin likiarvo
#Jokaisesta arvotusta pisteestä on helppo katsoa, onko se ympyrän sisällä: testataan onko x^2 + y^2 < 1

import numpy

pisteidenMaara = int(input("Anna arvottavien pisteiden määrä kokonaislukuna: "))
pisteetYmpyranSisalla = 0

laskuri = 0

while(laskuri < pisteidenMaara):
    xPiste = numpy.random.uniform(0,1)
    yPiste = numpy.random.uniform(0,1)
    laskuri += 1


    if(pow(xPiste,2) + pow(yPiste,2) < 1.0):
        pisteetYmpyranSisalla += 1


piinLikiarvo = 4.0 * pisteetYmpyranSisalla / float(pisteidenMaara)


print("Piin likiarvo:",piinLikiarvo)
