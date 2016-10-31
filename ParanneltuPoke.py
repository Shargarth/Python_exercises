ika = int(input("Anna ikäsi: "))

if ika >= 18 and ika < 20:
    paperit = input("Onko papereita k/e")
    if paperit == 'k' or paperit == 'K':
        print("Tervetuloa!")
    else:
        print("Mene kotiin kasvmaan")

if ika >= 20:
    print("Tervetuloa!")
elif ika < 18:
    print("Mene kotiin kasvamaan!")