#1
import random

for _ in range(10):
    x = random.random()
    print(x)

#2
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
#resposta: NameEror, pois, de fato, a função repeat_lyrics() não estava definida ainda

#3
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
repeat_lyrics()
#resposta: Não há erro nesta situação, pois a função repeat_lyrics() não é chamada antes da definição da variável print_lyrics
#não dá erro, mas é estranho. afinal, pq definir uma função senão a partir do 1o momento em que usá-la? soa abstrato, mas talvez
#seja irrelevante para uma boa prática - aliás, n consigo afirmar se é boa ou má prática

#4
#resposta: b)

#5
#resposta: d)

#6
hours = float(input("How many hours have you worked?\n"))

rate = float(input("How much you're paid for hour?\n"))

def computepay(x1,x2):
    if hours > 40:
        x1 = x1 * 1.4
        paym = x1 * x2
        return paym
    else:
        paym = x1 * x2
        return paym

print(f"Your payment is ${computepay(hours,rate)}")

#7
def computegrade(x):
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")

score = float(input("Enter score: \n"))

if 0 <= score and 1 >= score:
        computegrade(score)
else:
    print("Bad score!")

