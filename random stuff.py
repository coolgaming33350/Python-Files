import time
valid = ("false")

print("\n" *42)

welcome = ("Hi, how are you?: ")

input(welcome)

print("\nWell I don't care")

time.sleep(4)

stage_2 = ("\nOk fine I care a little... maybe ")
print(stage_2)

time.sleep(3)

print("Ok, another question.")
time.sleep(1.5)
stage_3 = input("\nWhat is your favorite book?: ")

if stage_3 == "all books":
    print("well i like all books too :)\n\\")
else:
    print("well i like all books. :(")

time.sleep(2)

while valid == "false":
    password = input("\nPlease enter the password to continue: ")
    if password == "password":
        time.sleep(2)
        print("\nyay dat was da correct answer! :) you can continue!")
        valid = ("true")
    elif password != "password":
        print("That was incorrect. Please try again!")
        time.sleep(1)
        password = input("Please enter the password to continue.")

time.sleep(2)
print("\nNow you get to answer another question.")
time.sleep(2)
print("\n*thinks of question*")
stage_4 = input("What is your favorite food?: ")

if stage_4 == "macdonalds chicken nuggies":
    time.sleep(1)
    print("\nWow, we have alot in common! :D")
    time.sleep(0.5)
    print("Lets move on...")
elif stage_4 != "macdonalds chicken nuggies":
    print("Wow, you are so gross. macdonalds chicken nuggies are much, much, much better. :(")
    time.sleep(1)
    print("I dont like u anymore. :(")
    exit()

print("Ok, now this is a quiz! Dylan's quiz!")

stage_5 = input("What is dylans favorite sport?: ")

