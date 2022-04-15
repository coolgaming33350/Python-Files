import time
import random

import os.path
isvalidchoice = 'false'
print('DO NOT USE IDLE TO RUN THIS!! IT WILL NOT SAVE PASSWORDS!')
temppwd = ''
def checkExistence():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()

def appendNew():
    file = open("info.txt", 'a')

    print()
    print()

    userName = input("Please enter the user name: ")
    password = input("Please enter the password here: ")
    website = input("Please enter the website address here: ")

    print()
    print()

    usrnm = "UserName: " + userName + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close
    print(time.thread_time_ns())

def readPasswords():
    file = open('info.txt', 'r')
    content = file.read()
    file.close()
    print(content)
    print(time.thread_time_ns())

def generatePasswords():
    one = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&',
    '*', '(', ')', '-', '+', '_', '=', '<', '>', '`', '~', '[', ']')
    two = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&',
    '*', '(', ')', '-', '+', '_', '=', '<', '>', '`', '~', '[', ']')
    three = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&',
    '*', '(', ')', '-', '+', '_', '=', '<', '>', '`', '~', '[', ']')
    number4 = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&',
    '*', '(', ')', '-', '+', '_', '=', '<', '>', '`', '~', '[', ']')
    five = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&',
    '*', '(', ')', '-', '+', '_', '=', '<', '>', '`', '~', '[', ']')
    six = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&',
    '*', '(', ')', '-', '+', '_', '=', '<', '>', '`', '~', '[', ']')
    seven = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&',
    '*', '(', ')', '-', '+', '_', '=', '<', '>', '`', '~', '[', ']')
    eight = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&',
    '*', '(', ')', '-', '+', '_', '=', '<', '>', '`', '~', '[', ']')
    nine = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&',
    '*', '(', ')', '-', '+', '_', '=', '<', '>', '`', '~', '[', ']')
    ten = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&',
    '*', '(', ')', '-', '+', '_', '=', '<', '>', '`', '~', '[', ']')
    eleven = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&',
    '*', '(', ')', '-', '+', '_', '=', '<', '>', '`', '~', '[', ']')
    twelve = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&',
    '*', '(', ')', '-', '+', '_', '=', '<', '>', '`', '~', '[', ']')
    num1 = random.randrange(0, 80)
    num2 = random.randrange(0, 80)
    num3 = random.randrange(0, 80)
    num4 = random.randrange(0, 80)
    num5 = random.randrange(0, 80)
    num6 = random.randrange(0, 80)
    num7 = random.randrange(0, 80)
    num8 = random.randrange(0, 80)
    num9 = random.randrange(0, 80)
    num10 = random.randrange(0, 80)
    num11 = random.randrange(0, 80)
    num12 = random.randrange(0, 80)
    # this part was annoying cuz of stupid tuple issues, otherwise it would be in one variable.
    temppwd = (one[num1] + two[num2])
    temppwd2 = (temppwd + three[num3])
    temppwd3 = (temppwd2 + number4[num4])
    temppwd4 = (temppwd3 + five[num5])
    temppwd5 = (temppwd4 + six[num6])
    temppwd6 = (temppwd5 + seven[num7])
    temppwd7 = (temppwd6 + eight[num8])
    temppwd8 = (temppwd7 + nine[num9])
    temppwd9 = (temppwd8 + ten[num10])
    temppwd10 = (temppwd9 + eleven[num11])
    temppwd11 = (temppwd10 + twelve[num12])
    print('\nHere is your password: ' + temppwd11)
    file = open("info.txt", 'a')

    print()
    print()

    userName = input("Please enter the user name: ")
    password = (temppwd11)
    website = input("Please enter the website address here: ")

    print()
    print()

    usrnm = "Username: " + userName + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close
    print(time.thread_time_ns())

def test():
    print('test')

checkExistence()
while isvalidchoice == 'false':
    whattodo = input('What would you like to do? (exit, add, list or generate pwds): ')
    if whattodo == 'add':
        appendNew()
        isvalidchoice = 'true'
    elif whattodo == 'list':
        readPasswords()
        isvalidchoice = 'true'
    elif whattodo == 'generate':
        generatePasswords()
    elif whattodo == 'exit':
        print('\n')
        isvalidchoice = 'true'
    else:
        print('Please try again.')
    
exitvar = str(input('Press enter to exit '))
exitvar
