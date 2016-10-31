def parittomienKarsija(alkuperainenLista):
    uusiLista = alkuperainenLista[:]

    for x in uusiLista:
        if not x % 2  == 0:
            uusiLista.remove(x)
    return uusiLista

alkuperainenLista = [1,2,3,4,5,6,7,8]

uusiLista = parittomienKarsija(alkuperainenLista)

print(alkuperainenLista)
print(uusiLista)


