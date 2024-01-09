#1
import socket

while True:
    url_str = input('Enter a url: \n')

    if not url_str.startswith('http://'):
        url_str = 'http://' + url_str

    url_list = url_str.split('/')
    hostname = url_list[2]
        
    try:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((hostname, 80))
        cmd = ('GET ' + url_str + ' HTTP/1.0\r\n\r\n\n').encode()
        mysock.send(cmd)

        break
    except:
        print('Cannot connect to this website.\n')

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
        
#2
import socket

while True:
    url_str = input('Enter a url: \n')

    if not url_str.startswith('http://'):
        url_str = 'http://' + url_str

    url_list = url_str.split('/')
    hostname = url_list[2]
    
    
    try:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((hostname, 80))
        cmd = ('GET ' + url_str + ' HTTP/1.0\r\n\r\n\n').encode()
        mysock.send(cmd)

        break
    except:
        print('Cannot connect to this website.\n')

received = ''

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break

    received += data.decode()

    if len(received) > 3000:
        break

    print(data.decode(),end='')

mysock.close()

#3
import urllib.request, urllib.parse, urllib.error

website = input('Enter a url: ')
fhand = urllib.request.urlopen(website)

received = ''
char_dict = dict()

for line in fhand:
    linedecoded = line.decode()

    if len(received) <= 3000:     
        print(line.decode())
        received += linedecoded
    
    for char in linedecoded.strip().split():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1


charord_dict = sorted(list(char_dict.items()), key = lambda x: x[1], reverse = True)
charfreq_list = list(char_dict.values())
totalchar = sum(charfreq_list)

print(charord_dict, totalchar)

#4
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup                   #necessário instalar bs4
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
count = 0
tags = soup('p')
for tag in tags:
    print(tag)
    count += 1
    
print(count)

#5
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

data_storaged = b''
count1 = 0
count2 = 0

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    if (b'\r\n\r\n' in data) and (count1 == 0):
        count2 = 1
        print(data.decode(), end='')       
    elif (b'\r\n\r\n' in data) and (count1 > 0):
        count2 = 1
        print(data_storaged.decode(), end='')
        print(data.decode(), end='')
    elif (b'\r\n\r\n' not in data) and (count2 == 0):
        data_storaged += data
        count1 += 1
    else:
        print(data.decode(), end='')

mysock.close()
