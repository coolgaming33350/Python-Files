import random
import time

sentences = int(input("How many sentences would you like to make?: "))
loop = 0
while loop < sentences:
    nouns = ("puppy", "car", "rabbit", "girl", "monkey")
    verbs = ("runs", "hits", "jumps", "drives", "barfs") 
    adv = ("crazily", "dutifully", "foolishly", "merrily", "occasionally")
    adj = ("adorable", "clueless", "dirty", "odd", "stupid")
    pun = (".", ",", "!", "?", " :)")
    num1 = random.randrange(0,5)
    num2 = random.randrange(0,5)
    num3 = random.randrange(0,5)
    num4 = random.randrange(0,5)
    num5 = random.randrange(0,5)
    print (nouns[num1] + ' ' + verbs[num2] + ' ' + adv[num3] + ' ' + adj[num4] + pun[num5])
    loop = (loop + 1)
print("Done printing, made " + str(sentences) + " sentences!")
entervar = input('Press enter to exit... ')
