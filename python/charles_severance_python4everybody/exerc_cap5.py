#1
total = 0
Count = 0
average = 0
nullstep = 'Notdone'
number_str = 'Notdone'

while number_str != 'done':
    try: 
        number = float(number_str)
        total = total + number
        Count = Count + 1    
        average = total/Count
    except:
        if number_str is nullstep:
            pass
        else:
            print("\nBad data!")
    number_str = input("\nEnter a number: \n")
    print(id(number_str))
    print(id(nullstep))

average_trunc = round(average, 2)

print(f"There is a total of {Count} numbers, their sum is {total} and {average_trunc} as average ")

#1 - 2a solução
total = 0
Count = -1
average = 0
number_str = 0

while number_str != 'done':
    try: 
        number = float(number_str)
        total = total + number
        Count = Count + 1
        if Count > 0:    
            average = total/Count
    except:
            print("\nBad data!")
    number_str = input("\nEnter a number: \n")

average_trunc = round(average, 2)

print(f"There is a total of {Count} numbers, their sum is {total} and {average_trunc} as average ")

#1 - 3a solução
total = 0
Count = 0
average = 0

while True:
    number_str = input("\nEnter a number: \n")
  
    if number_str == 'done':
        break
    else:
        try: 
            number = float(number_str)
            total = total + number
            Count = Count + 1
            average = total/Count
        except:
                print("\nBad data!")
    
average_trunc = round(average, 2)

print(f"There is a total of {Count} numbers, their sum is {total} and {average_trunc} as average ")

#2
number_str = 0
max_number = 0
min_number = 0
count = 0
total = 0

while number_str != 'done':
    try: 
        number = float(number_str)
        total = total + number
        if count <= 1:
            max_number = number 
            min_number = number
        else:
            if number - max_number >= 0:
                max_number = number
            if number - min_number <= 0:
                min_number = number
        count = count + 1      
    except:
       print("\nBad data!")
    number_str = input("\nEnter a number or 'done' to end the program: \n")

print(f"The sum of all numbers is {total}, the minimum is {min_number}")

#2 - solução alternativa
total = 0
Count = 0
average = 0

while True:
    number_str = input("\nEnter a number: \n")
  
    if number_str == 'done':
        break
    else:
        try: 
            number = float(number_str)
            total = total + number
            Count = Count + 1
            average = total/Count
        except:
                print("\nBad data!")



