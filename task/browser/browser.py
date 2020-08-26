import os
import sys
from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore

import requests
# write your code here
my_stack = deque()
my_stack.append(None)
my_stack.append(None)
directory = sys.argv[1]
if not os.path.exists(directory):
    os.mkdir(directory)


def run_stuff():
    working_url = url
    if url.find('https://') == -1:
        working_url = 'https://' + url
    r = requests.get(working_url)
    if r:
        soup = BeautifulSoup(r.content, 'html.parser')
        x = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li'])
        hh = ''
        for i in x:
            if i.script:
                i.script.extract()
            z = ''
            if i.a:
                z += Fore.BLUE + i.text
            else:
                z += i.text
            hh += z

        print(hh)

        with open(f'{directory}/{url}.txt', 'w') as b:
            b.write(hh)
    else:
        print('error')


while True:
    url = input()
    if url == 'exit':
        exit()
    elif url == 'back':
        url = my_stack[1]
        run_stuff()
    elif url.find('.') == -1:
        if os.path.isfile(f'{directory}/{url}.txt'):
            with open(f'{directory}/{url}.txt', 'r') as f:
                print(f.read())
        else:
            print('error')
    else:
        run_stuff()
    my_stack.appendleft(url)
