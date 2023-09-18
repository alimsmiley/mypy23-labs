import felhantering  # Importera felhanteringsmodulen

# Funktion för att beräkna den aritmetiska summan
def aritmetisk_summa(a, d, n):
    aritmetisk_summa_värde = n * (2 * a + (n - 1) * d) / 2
    return aritmetisk_summa_värde

# Funktion för att beräkna den geometriska summan
def geometrisk_summa(g_1, q, n):
    geometrisk_summa_värde = g_1 * (1 - q**n) / (1 - q)
    return geometrisk_summa_värde

# Läs in data för den aritmetiska summan med felhantering
a = felhantering.läs_in_float("Data för den aritmetiska summan:\na_1: ")
d = felhantering.läs_in_float("d: ")

# Läs in data för den geometriska summan med felhantering
print("\nData för den geometriska summan:")
g_1 = felhantering.läs_in_float("g_1: ")
q = felhantering.läs_in_float("q: ")

# Läs in antal termer i summorna med felhantering
n = felhantering.läs_in_heltal("Antal termer i summorna:\nn: ")

# Beräkna den aritmetiska summan
aritmetiskt_resultat = aritmetisk_summa(a, d, n)

# Beräkna den geometriska summan
geometriskt_resultat = geometrisk_summa(g_1, q, n)

# Jämför och skriv ut resultatet
if aritmetiskt_resultat is not None and geometriskt_resultat is not None:
    if aritmetiskt_resultat > geometriskt_resultat:
        print("Den aritmetiska summan är störst.")
    elif geometriskt_resultat > aritmetiskt_resultat:
        print("Den geometriska summan är störst.")
    else:
        print("Den aritmetiska och geometriska summan är lika stora.")
