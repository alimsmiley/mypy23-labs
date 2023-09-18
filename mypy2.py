""" x = 15
print(x)
print(1001)
print("Det var lite siffror, detta är en sträng")
djur = 'katt'
a = djur
b = 'djur'
print(b, x-10, b, "Hi this is Alim!") """
# Everything between """" counts as comment, for single line comment we use # and everything after it in the same line will be counted as a comment 
# skriver ut [0, 1, 2, 3] 4 anger antalet tal
print(list(range(4)))
# skriver ut [1, 2, 3] 1 anger första talet, 4 övre gräns
print(list(range(1,4)))
# skriver ut [1, 3] 1 anger första talet, 4 övre gräns, 2 steget mellan
print(list(range(1,4,2)))

def beräkna_styckpris(antal=50, bakgrundsfärg="blå", form="fyrkantig"):
  if form != "fyrkantig":
  styckpris = 60
  else:
  styckpris = 40
 
  if bakgrundsfärg != "vit":
  styckpris += 3
 
  if antal >= 100:
  styckpris = styckpris * 0.80

  return styckpris
  