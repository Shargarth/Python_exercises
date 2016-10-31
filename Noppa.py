import random

def heita():
    return random.randint(1,6)

heitto = heita()

print(heitto)

while(heitto  < 6):
    heitto = heita()
    print(heitto)
