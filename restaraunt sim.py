import time
valid = ("false")
print("""
                                                                         
           |-----    |     |    |          |
           |         |     |    |          |
           |-----    |     |    |          |
           |         |     |    |          |
           |         |     |    |          |
           |         |     |    |          |
           |         |     |    |          |
           |         \_____/    |_______   |_______ Screen, Please! :)""")
time.sleep(1)
print("Loading.")
time.sleep(1)
print("Loading..")
time.sleep(0.8)
print("Loading...")
time.sleep(0.7)
print("Loading....")
time.sleep(0.6)
print("Loading.....")
time.sleep(0.5)
print("\n" *42)


realmenu = ("Chicken Nuggies", "Hot Dog", "Cheeseburger", "Mac and Cheese", "Poggers sandwich", "Uno Reverse Card", "chicken nuggies", "hot dog", "cheeseburger", "mac and cheese", "poggers sandwich", "uno reverse card")
menu = ("We sell Chicken Nuggies, Hot Dog, Cheeseburger, Mac and Cheese, Poggers Sandwiches, and Uno Reverse Cards.")
print (menu)
choice = input("Hi there! What would you like to eat?(dont use capitals): ")
print("Checking if response is on menu... (may take a while)")


while valid == "false":
    if choice in realmenu:

        print("\n" *42)
        valid = ("true")
        time.sleep(1)
        print("Ok! I'll be right back with your " + choice + "!")
        time.sleep(5)
        givefood = ("Here you go!")
        print(givefood + " I hope you enjoy your " + choice + "!")
        time.sleep(1)
        print("*eating...*")

        time.sleep(3)
        print("""


              O
              |=   / 
              |   ------
             / \  |    |
            ---------------""")
                        
        Tip = input("Would you like to tip us?(yes/no)")
        if Tip == "yes":
            percent = int(input("\nThank you, how much percent?: "))
            if percent > 50:
                print("That is too high, max is 50%.")
                percent = int(input("How much percent?"))
            elif percent <= 50:
                print("Thank you for your tip of " + percent + "!")
                print("Thanks for tipping us! Have a great rest of your day!!")
        else:
            print("Okay! We hope you have a great day!")
            print("Also, play my other games too!")
        break
    elif choice == "secret":
        print("You found the secret!!! Good job! :) Have a great day!! :)")
    elif choice not in realmenu:
        print("That is not on our menu, please try again!")
        valid = ("false")
        choice = input("What will your order be today? (case sensitive): ")
        print("Checking if choice is on menu...")



