import random
import time

addlist = '+', 'addition', 'add', 'plus'
sublist = '-', 'subtract', 'minus', 'sub'
mullist = 'x', '*', 'multiply', 'mul'
divlist = '/', 'divide', 'div'
mathtype = input('What type of math would you like to do?: ')
if mathtype in addlist:
    num1 = int(input('waht is the first number in da equazion: '))
    num2 = int(input('waht is the second number in da equazion: '))
    result = num1 + num2
    print(result)
elif mathtype in sublist:
    print('noice')
elif mathtype in mullist:
    print('noice')
elif mathtype in divlist:
    print('noice')
else:
    print('no u')

