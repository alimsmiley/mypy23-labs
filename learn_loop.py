#for x in range(6):  #(for loop): it reapeates the process for a predetermind number of times (here 6 times)
#    print("Hello")

#oooooooooooooooooooooooooooooooooooooooooooo -While_slinga- oooooooooooooooooooooooooooooooooooooo000000000
#x=0
#while x<6:          #same result as above but in this example using while looks a bit more complicated, so depending on the problem we can choose for-loop or while-loop
#    print("hej! ")
#    x = x + 1   #or x += 1

#oooooooooooooooooooooooooooooooooooooooooooo -Ändra Listan- oooooooooooooooooooooooooooooooooooooooooooooooo

#lista_mat = ["gurka", "tomat", "pasta", "bröd", "mjölk"]
#lista_mat[3] = "köt"            #skriv namn på listan och indexnummer inom square brackets för att ändra värdet av det som står i listan med den nya
#lista_mat.append("ost")         #.append("något") lägger till det som står i parentesen sist i listan 
#lista_mat.remove("mjölk")       #.remove("något") tar bort element i listan som står i parentesen
#print(lista_mat)

#oooooooooooooooooooooooooooooooooooooooooooo -While_slinga och lista- oooooooooooooooooooooooooooooooooooooo

#lista_mat = ["gurka", "tomat", "pasta", "bröd", "mjölk"]
#ista_mat[3] = "köt"            #skriv namn på listan och indexnummer inom square brackets för att ändra värdet av det som står i listan med den nya
#lista_mat.append("ost")         #.append("något") lägger till det som står i parentesen sist i listan 
#lista_mat.remove("mjölk")       #.remove("något") tar bort element i listan som står i parentesen

#x = 0               #while loopen börjar från startvärden som vi anger här och sedan med avseende på det vi skriver i ( x += 2) fortsätter och gör samma sak, så i det här fallet den börjar från den första element i listan och printar den sedan hoppar två steg i listan och printar osv
#while x<6:
#    print(lista_mat[x])
#    x += 2


#oooooooooooooooooooooooooooooooooooooooooooo -For_slinga och lista- oooooooooooooooooooooooooooooooooooooo0000

#namnlista = ["David", "Kim", "Julia"]
#for namn in namnlista:                  #efter "for" måste vi skriva namnet som vi vill kalla varje element i listan, och sedan efter in skriver vi namnet på den listan vi menar
#    print(namn)

#oooooooooooooooooooooooooooooooooooooooooooo - for-slinga -ooooooooooooooooooooooooooooooooooooooooooooooooooo

#namelist = 3*[None]
#agelist = 3*[None]
#for i in range(3):
# namelist[i] = input("Name of person number " + str(i+1) + ": ")
# agelist[i] = input("Age of person number " + str(i+1) + ": ")

#namelist.append("Alim")
#agelist.append("23")

#for i in range(len(namelist)):                                   #len() beräknar längden av en lista eller tuple osv. och när vi inte vet vad längden /antal elemnet i en lista är eller blir efter att vi har lagt till eller tagit bort element från listan så är det smart att använda len() för att låta programmet räkna range av element i listan 
#    print("Name: " + namelist[i] + ", Age: " + agelist[i])       #och på så sätt kan vi skriva ut namn och ålder vidan sidan av varandra ocbservera att vi använder fo-loop för att skriva ut resultat på rader efter varandra och att få python gå igenom coden som vi vill

#oooooooooooooooooooooooooooooooooooooooooooo - for-slinga -ooooooooooooooooooooooooooooooooooooooooooooooooooo

#veckodagar = ["mån", "tis", "ons", "tor", "fre", "lör", "sön"]
#for d in [1, 2, 3]:             #observera att [1, 2, 3] är indexnummer för elemetn i listan, detta betyder för element 1(som är "tis"), element2 (som är "ons") och element 3 (som är "tors")
#  print(veckodagar[xxx])        
                                #t.ex om vi vill att coden ska printa ut ons, tor, fre då måste det stå d+1 istället för xxx

#oooooooooooooooooooooooooooooooooooooooooooo - for-slinga -ooooooooooooooooooooooooooooooooooooooooooooooooooo

#Skriver ut en multiplikationstabell från 1 till 11.
#for i in range(1, 12):
#  for j in range (1,12):
#    print (i*j, end = "  ")
#  print()
###

#Första exemplet, med fel
#lista1 = []
#for i in range(1,6):
#  print("Multiplikationstabell för " + str(i) + ":", end=" ")
#  for j in range(1,6):
#    produkt = i*j 
#    lista1.append(produkt)
#  for resultat in lista1:
#    print(resultat, end=" ")
#  print()

#print("\n")
#Andra exemplet, som fungerar som det ska
#for i in range(1,6):
#  print("Multiplikationstabell för " + str(i) + ":", end=" ")
#  lista2 = []
#  for j in range(1,6):
#    produkt = i*j 
#    lista2.append(produkt)
#  for resultat in lista2:
#    print(resultat, end=" ")
#  print()
#oooooooooooooooooooooooooooooooooooooooooooo - for-slinga -ooooooooooooooooooooooooooooooooooooooooooooooooooo

#for i in range(1, 5):
#    for j in range (1,3):
#        print (i+j, end = " ")
#    print()
#print("6 7")

#oooooooooooooooooooooooooooooooooooooooooooo - While-loop -ooooooooooooooooooooooooooooooooooooooooooooooooooo
# example: Vi vill skriva ut "x" exakt 5 gånger. Vilken/vilka av följande program gör det?

#metod1
#i = 0
#while i < 5:
#    print("x")
#    i += 1
#metod2    
#i = 1
#while i <= 5:
#    print("x")
#    i += 1
#metod3
#i = 0
#while i != 5:   #Ditt kodexempel är en enkel while-loop i Python som kommer att köra tills värdet på variabeln i blir lika med 5.
#    print("x")
#    i += 1
#oooooooooooooooooooooooooooooooooooooooooooo - While-loop (continue) -ooooooooooooooooooooooooooooooooooooooooooooooooooo

#i = 0
#while i < 6:
#  i += 1
#  if i == 3:           # Note that number 3 is missing in the result, so when you use continue. the condition in if doesnt print as you can see it when you run this programm
#    continue
#  print(i)

#oooooooooooooooooooooooooooooooooooooooooooo - XXXX -ooooooooooooooooooooooooooooooooooooooooooooooooooo

#tal = 100
#while True:
#    if tal > 50:
#        tal -= 10
#        print(tal)
#        continue
#    print("Tal är nu", tal, ".")
#    svar = input("Vil du fortsätta? (j/n)")
 
#    if svar == "n":
#        break
#    else:
#        tal = 100
 
#print("Tack och hej!")


#oooooooooooooooooooooooooooooooooooooooooooo - XXXX -ooooooooooooooooooooooooooooooooooooooooooooooooooo

#while True: 
#     stoppa = input("Vill du stoppa? Skriv ja: ") 
#     if stoppa == "ja": 
#         break
#primtal = 45*[]
#b = 0
#while b < 41:
#    print(primtal[b], end = " ")
#    b += 1

i = 3
while i < 8:
    print("a", end = " ")
    if i > 5:
        print("b", end = " ")
    i += 1