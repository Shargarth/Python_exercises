def gallonatLitroiksi(gallonat):
    return gallonat * 3.78541178

print("Anna gallonat, muunnan ne litroiksi")

gallonat = float(input("Anna gallonat: "))
while gallonat >= 0:
    gallonatLitroiksi(gallonat)
    print(gallonatLitroiksi(gallonat))
    gallonat = float(input("Anna gallonat: "))