#övning 2, förbättra följande code
"""
barn_pris = 10
vuxen_pris = 20

antal_biljetter = input("Hur många biljetter vil du köpa? ")
antalBiljetter = int(antal_biljetter)

antal_vuxen = input("Hur många av de biljetterna är för en vuxen? ")
antalVuxen = int(antal_vuxen)

antal_barn = antalBiljetter - antalVuxen

total_pris = antal_barn*barn_pris + antalVuxen*vuxen_pris

print("Du ska betala:")
print(total_pris)
"""
###################################
BARN_PRIS = 10
VUXEN_PRIS = 20

antal_biljetter = input("Hur många biljetter vil du köpa? ")
antalBiljetter = int(antal_biljetter)

antal_vuxen = input("Hur många av de biljetterna är för en vuxen? ")
antalVuxen = int(antal_vuxen)

antal_barn = antalBiljetter - antalVuxen

total_pris = antal_barn*BARN_PRIS + antalVuxen*VUXEN_PRIS

print(f"Du ska betala {total_pris}") #här skrev vi om inuti print satsen till f string för att minimera upprepning och enklare att hantera olika datatyper då vi har f-string

