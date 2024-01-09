#1
#resposta: printa 5; associa 5 à variável x; printa 6, pois x+1=6

#2    
prompt = input("What's your name?\n")   

print(f"Hello, {prompt}! Welcome!")

#3
hours = float(input("How many hours have you worked?\n"))

payrate = float(input("What's your payment rate per hour?\n"))

payment = round(hours*payrate, 2)

print(f"You're going to receive ${payment}")

#4
width = 17

height = 12.0

if width//2 == 8 and width/2.0 == 8.5 and height/3 == 4.0:
    print("A última expressão é um erro com certeza e você acertou as outras")
else:
    print("Errrrôôu")

#5
celstemp = float(input("Temperature in Celsius: \n"))

fahrtemp = celstemp*1.8 + 32

print(f"The temperature, in Fahrenheit, is {fahrtemp}")



