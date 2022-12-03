import time
import random

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
		if y == 0:
			print("Error. Cannot Divide By 0. (error code no0divide)")
			exit()
		elif y != 0:
			return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))

if choice == '1':
		finalnum = add(num1, num2)
		print(num1, "+", num2, "=", finalnum)

elif choice == '2':
		finalnum = subtract(num1, num2)
		print(num1, "-", num2, "=", finalnum)
elif choice == '3':
		finalnum = multiply(num1, num2)
		print(num1, "*", num2, "=", finalnum)

elif choice == '4':
		finalnum = divide(num1, num2)
		print(num1, "/", num2, "=", finalnum)

next_calculation = input("do you want to do another calculation with same final number? (yes/no): ")
if next_calculation == "no":
		exit()


while True:
	choice2 = input("Enter choice(1/2/3/4): ")

	if choice2 in ('1', '2', '3', '4'):
		num1 = finalnum
		num2 = float(input("Enter number: "))

	if choice2 == '1':
		finalnum = add(num1, num2)
		print(num1, "+", num2, "=", finalnum)

	elif choice2 == '2':
		finalnum = subtract(num1, num2)
		print(num1, "-", num2, "=", finalnum)
	elif choice2 == '3':
		finalnum = multiply(num1, num2)
		print(num1, "*", num2, "=", multiply(num1, num2))

	elif choice2 == '4':
		finalnum = divide(num1, num2)
		print(num1, "/", num2, "=", divide(num1, num2))

	next_calculation = input("do you want to do another calculation with same final number? (yes/no): ")
	if next_calculation == "no":
		exit()
	else:
		if next_calculation == "yes":
			print("continuing...")
		else:
			print("Invalid Input")
