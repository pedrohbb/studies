#1
hours = float(input("How many hours have you worked?\n"))

rate = float(input("How much you're paid for hour?\n"))

if hours > 40:
    rate = rate * 1.4
    paym = hours * rate
    print(f"Your payment is ${paym}")
else:
    paym = hours * rate
    print(f"Your payment is ${paym}")

#2
try:
    hours = float(input("How many hours have you worked?\n"))

    rate = float(input("How much you're paid for hour?\n"))

    if hours > 40:
        rate = rate * 1.4
        paym = hours * rate
        print(f"Your payment is ${paym}")
    else:
        paym = hours * rate
        print(f"Your payment is ${paym}")
except:
    print("Error! Please enter a numeric input")


#3
score = float(input("Enter score: \n"))
if 0 <= score and 1 >= score:
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
else:
    print("Bad score!")

    