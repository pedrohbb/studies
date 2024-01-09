#1
words_dict = {}
fhand = open(input('Enter a file name: '))

for line in fhand:
    words_line = line.split()
    for i in range(len(words_line)):
        words_dict[words_line[i]] = 0



#2
days_dict = {}
fhand = open(input('Enter a file name: '))

for line in fhand:
    if line.startswith('From'):
        words_line = line.split()
        if len(words_line) >=3:
            if (words_line[2] in days_dict):
                days_dict[words_line[2]] += 1
            else:
                days_dict[words_line[2]] = 1

print(days_dict)

#3
mails_dict = {}
fhand = open(input('Enter a file name: '))

for line in fhand:
    if line.startswith('From'):
        words_line = line.split()
        if len(words_line) >=3:
            if (words_line[1] in mails_dict):
                mails_dict[words_line[1]] += 1
            else:
                mails_dict[words_line[1]] = 1
                
print(mails_dict)

#4
mails_dict = {}
fhand = open(input('Enter a file name: '))

for line in fhand:
    if line.startswith('From'):
        words_line = line.split()
        if len(words_line) >=3:
            if (words_line[1] in mails_dict):
                mails_dict[words_line[1]] += 1
            else:
                mails_dict[words_line[1]] = 1

mails_list = list(mails_dict.keys())
countmails_list = list(mails_dict.values())
maximum = max(countmails_list)
users_max = []

for keysz in mails_list:
    if mails_dict[keysz] == maximum:
        users_max += [keysz]

print(f"Who has the most messages ({maximum}): ")

for j in range(len(users_max)):
    print(users_max[j])

#5
domains_dict = {}
fhand = open(input('Enter the file name: '))

for line in fhand:
    if line.startswith('From'):
        words_line = line.split()              
        
        if len(words_line) >= 3:
            at_index = words_line[1].index('@')
            domain_line = words_line[1][at_index:]
            
            if domain_line in domains_dict:
                domains_dict[domain_line] += 1

            else:
                domains_dict[domain_line] = 1

print(domains_dict)
        

                


