import random
loop = 0
while loop <3125:
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

