#00000000000000000000000000000000000000- lists and dictionaries -000000000000000000000000000000000000000000000000000000

# Skapa en tom lista för namnen
#namnlista = []

# Ange antalet namn du vill lägga till i listan
#antal_namn = int(input("Ange antalet namn du vill lägga till: "))

# Använd en for-loop för att låta användaren mata in namn
#for i in range(1, antal_namn + 1):
#    namn = input("Skriv namn nummer " + str(i) + ": ")
#    namnlista.append(namn)

# Skriv ut de insamlade namnen
#print("De insamlade namnen är:")
#for namn in namnlista:
#    print(namn)

#00000000000000000000000000000000000000- lists and dictionaries "lista.pop(i)" and "lista.remove()" and "del lista[i]" -000000000000000000000000000000000000000000000000000000
    
#.pop(i) and .remove() are both methods used to manipulate lists in Python, but they have different purposes and behaviors.
#.pop(i): This method is used to remove and return the element at the specified index i from the list. It modifies the original list by removing the element at the given index and returns the removed element.

#Example:
#my_list = [1, 2, 3, 4, 5]
#removed_element = my_list.pop(2)  # Removes and returns the element at index 2 (which is 3)
#print(my_list)  # Output: [1, 2, 4, 5]
#print(removed_element)  # Output: 3
#.remove(value): This method is used to remove the first occurrence of the specified value from the list. It does not return the removed element; instead, it modifies the original list by removing the first occurrence of the specified value. If the value is not found in the list, it raises a ValueError exception.

#Example:
#my_list = [1, 2, 3, 2, 4, 5]
#my_list.remove(2)  # Removes the first occurrence of 2
#print(my_list)  # Output: [1, 3, 2, 4, 5]

#example
#my_list = [1, 2, 3, 4, 5]
#del my_list[2]  # Deletes the element at index 2 (which is 3)
#print(my_list)  # Output: [1, 2, 4, 5]
#print(my_list[2]) #observera att till skillnad 2från .pop(i) så när vi vill skriva ut värdet som hade tagits bort så visas det inte när man använder sig av "del" och i det här fallet kommer det som printas ut vara det som har index 2

#In summary:
#.pop(i) removes an element by its index and returns the removed element.
#.remove(value) removes the first occurrence of a specific value from the list and does not return the removed element.
#del lista[i] is used for deleting an element by its index and directly modifies the list.

#00000000000000000000000000000000000000- lists and dictionaries, "len(lista)" and "lista.sort()" and "lista.insert(i, "något")" -000000000000000000000000000000000000000000000000000000

#my_list = [1, 6, 2, 3, 2, 4, 5]
#my_list.sort()   #for att sortera
#my_list.insert(2, "C") # lägger till på plats nr 2
#print(my_list)
#listans_längd = len(my_list)  #len för att få längden på listan
#print(listans_längd)


#00000000000000000000000000000000000000- lists and dictionaries -000000000000000000000000000000000000000000000000000000

#Vill du sortera listan i omvänd ordning, kan du skriva reverse=True , i parenteserna.

#lista_bokstäver = ["B","D", "A", "C"]
#lista_bokstäver.sort(reverse=True)
#print(lista_bokstäver) # Visar ['D', 'C',' B', 'A']


#00000000000000000000000000000000000000- lists and dictionaries -000000000000000000000000000000000000000000000000000000
#lista = ["2","1","12","3"]
#sorterad_lista = sorted(lista)
#print(sorterad_lista)             #observera att här kommer den att betrakta listans element som strings och sortera de med utseendemässigt

#lista2 = [2, 1, 12, 3]
#sorterad_lista2 = sorted(lista2)
#print(sorterad_lista2)                  #till skillnda från förra så här är elementen i listan integer och sortering baseras på ordnigen av siffror 


#00000000000000000000000000000000000000- lists and dictionaries -000000000000000000000000000000000000000000000000000000
resultat = {"a":2, "b":3, "c":3}
#for element in resultat.keys():  #funkar
#    print(element,resultat[element])

for varjeNyckel in resultat.keys():
    print(varjeNyckel, resultat[i])


#00000000000000000000000000000000000000- lists and dictionaries -000000000000000000000000000000000000000000000000000000



#00000000000000000000000000000000000000- lists and dictionaries -000000000000000000000000000000000000000000000000000000