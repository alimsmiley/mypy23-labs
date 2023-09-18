
#functions: 
def my_name(first_name, last_name): #functions start with "def" then name of your function and parentesese with the arguments inside and finishing with ":",inside the parenteses are caled arguments and you can have as many arguments as you want, and you seperate each argument with a comma as you see here
   # """This function reads your full name and prints it with a welcome message"""
    print(f"{first_name} {last_name}, Nice to meet you!") #to get the values of a variable from a funcion after you call the function, and printing it, you can use this method where python reads the code and prints the value assigned to a variable, and abserve the qutation marks and how we write different arguments of funcion in cyúrly braces
    #you could also use + for fomating the message inside print but using f"string is more modern and readable
    
# my_name("ALim", "Esmaili") #the function above will not be executed as long as you don't call it, and when you call the function it will go through the function and do as you have instructed, in other words calling a function is to telling your code that you can now work and do your job.

###################################################################################################### 1
def greet(name):
    message = "Hello " + name + " " + "nice to meet you!"
    return message
#name = input("Please enter your name: ")
#print(greet(name))
##fråga: varför visat inte coden greet meddelandet (jag vet att man kan lägga in greet i print och sedan köra men varför händer det inget utan )
###################################################################################################### 2

#if you dont know how many parameters you will need for a function, just add a * before the name of that general parameter inside the parenteses, like the example below
def models_of_cars_owned(*cars):
    print("Beside the other car models " + cars[3] + " is my favorite!") #In Python, list and tuple indexing is zero-based, which means that the first element is at index 0, the second element is at index 1, and so on. When you access cars[4], you are actually retrieving the fifth element (index 4) from the cars tuple.
    
#models_of_cars_owned("Ferari", "Lamborgini", "Cadilac", "Porsche", "Mercedes_GLS") #don't forget to use the quotation marks while naming different argumnets, as you see here inside the parenteses
####################################################################################

def my_children(first_name, last_name, age):
    
    print(first_name, last_name, age, " Good Job!")
    

#my_children(last_name="Esmaili", first_name="Mila", age="5")

################################333
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

#my_function(name="Alice", age=30, city="New York")  # kwargs is a dictionary
#####################################################################3333

#default parameter valu: wi can give the function parameter a default value that when we call the function, if anything is given then the function uses it otherwise if the call is empty for example the the function will use the defualt value given inside the function, as you can see in the example below
def country_of_origin(country = "Sweden"):
    print("I am originally from " + country + "!")
#country_of_origin("USA")
#country_of_origin()
#################################################33333

#return values in functions: if you want to return a value to the function for getting printed after doing as the function structure the you can use the return value. Return takes an argument and passes it to function then the function does its job and returns the final result to function as it was called 
def your_total_tax(income):
    return 0.3 * income
#observe that you could also add "income=60000" and put "income" instead of "60000" below inside the call
tax = your_total_tax(60000)
#print("your total tax would be: ", tax)
 ####################################################

#age = int(input("Please enter your age: "))
#print(f"You are {age} years old!")
#print("du är " + str(age) + " år gammal!")
#print("du är ", age, " år gammal!")
#############################################################
name = "alim"
name2 = "alim"
#print(name>=name2) #this will print "True"
#############################
#if sats
#temperature = int(input("Please enter current temperature: "))
#if temperature > 25:  #dont forget colon after if as you see here
    #print("DAMN son, it's hot as hell!") #glöm inte att efter if satsen det som skrivs ska vara indenterad(tab eller 4 space =avståndet)
#else: #dont forget colon as you see here
    #print ("Shit, it's fucking cold!")


#################################################################
#age = int(input("Hur gammal är du?: ")) #obs, här om vi inte hade skrivit "int" då borde vi omvandla 18 nedan till string "str(18)" men nu när vi har int så går det att jämföra med ett integer
#if age < 18: #obs att i if-satser får vi endast jämföra samma data typer och här har vi två olika, string till vänster och integer till höger. för att fixa det så kan vi omvadla integer till string genom t.ex här: str(18)
# print("Tyvärr, du är för ung för att komma in!")
#else:
# print("Välkommen in!")
####################################################
#and/or in if sats

x = 0
MITTEN = -17

if x <= MITTEN:
 print("f", end = " ")
 print("g", end = " ")
else:
 print("h", end = " ")
print("i")

##########################3
#testa f string i input sats










































































































































































































