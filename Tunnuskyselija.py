oikeaTunnus = "python"
oikeaSalasana = "rules"


kayttajanTunnus = input("Anna käyttäjätunnus: ")
kayttajanSalasana = input("Anna salasana: ")
yritykset = 1

while yritykset < 5:
    if kayttajanSalasana == oikeaSalasana and kayttajanTunnus == kayttajanTunnus:
        print("Tervetuloa!")
        break;
    yritykset += 1
    kayttajanTunnus = input("Anna käyttäjätunnus: ")
    kayttajanSalasana = input("Anna salasana: ")

if yritykset == 5:
    print("Pääsy evätty!")