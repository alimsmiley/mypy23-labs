def meny(): 
  """En funktion som skriver ut en meny och frågar användaren om inmatning"""
  print("Meny\n1. Skriv ut en text.\n2. Mata in en text.\n3. Avsluta.") 
  text = "Det var en gång" 
  val = input("Vad vill du göra?\n")
  while val != "3": 
    if val == "1": 
      print(text) 
    elif val == "2": 
      text = input("Varsågod och mata in din text: \n")
    else:
      print("Felaktigt val! Välj en siffra mellan 1 och 3.")
      #När någon matat in fel kan hen ha glömt bor valen.
      #Kan du lägga till kod så de presenteras igen?
    val = input("Vad vill du göra?\n")

meny()