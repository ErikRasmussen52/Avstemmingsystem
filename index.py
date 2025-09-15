import random
# Liste med partier
partier = ["FRP", "AP", "Høyre", "SV", "Venstre", "SP", "KRF", "MDG", "Rødt", "Annet"]

# Viser hvilke partier man kan stemme på
def startValg()
    print("Du kan stemme på disse partiene:")
    for parti in partier:
        print(parti)

    print("Skriv 'slutt valg' når du er ferdig.")

startValg()

    
rndm = round(random.uniform(1, 100), 1)

partierliste ={
    "FRP": 23.8, "AP": 28.0, "Høyre": 14.6, "SV": 5.6, "Venstre": 3.7, "SP": 5.6, "KRF": 4.2, "MDG": 4.7, "Rødt": 5.3, "Annet": 4.5,
}
            
if partierliste["FRP"]




""""
#Lager en ordbok for å lagre stemmer
stemmer = {}
for parti in partier:
    stemmer[parti] = 0

# Leser inn stemmer
while True:
    valg = input("Skriv navnet på partiet du vil stemme på: ")

    if valg.lower() == "slutt valg": # stopper programmet
        break
    elif valg in stemmer:             # parti på listen
        stemmer[valg] += 1
        print("Du stemte på:", valg)
    else:
        print("Ugyldig parti, prøv igjen.")

# Viser resultat
print("Resultat:")
totalt_stemmer = sum(stemmer.values())

for parti, antall in stemmer.items():
    if totalt_stemmer > 0:
        prosent = (antall / totalt_stemmer) * 100
    else:
        prosent = 0
    print(f"{parti} : {antall} stemmer ({prosent:.2f}%)")

# Finner partiet som vant
if totalt_stemmer > 0: 
    vinner = max(stemmer, key=stemmer.get)
    print("Vinneren av valget ble:", vinner)
else:
    print("Ingen stemmer ble avgitt.")

"""