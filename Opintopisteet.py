opintopisteet = int(input("Anna opintopisteesi: "))

if(opintopisteet < 45):
    print("Kela ja opet ei tykkää")
elif opintopisteet >= 45 and opintopisteet < 55:
    print("Opet ei tykkää")
else:
    print("Onnittelut ensimmäisestä opiskeluvuodestasi")