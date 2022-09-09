import random
import time

#Start
print("\n" * 42)

#Variables
nouns = ("Puppy", "Car", "Rabbit", "Girl", "Monkey")
verbs = ("runs", "hits", "jumps", "drives", "barfs")
adv = ("crazily", "dutifully", "foolishly", "merrily", "occasionally")
adj = ("adorable", "clueless", "dirty", "odd", "stupid")
pun = (".", "...", "!", "?", " :)")

duplicateLoopCount = []

sentences_list = []

#Definitions
def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

def Average(lst):
    return sum(lst) / len(lst)

sentences = int(input("How many sentences would you like to make: "))

#Lists
nouns_dict = {
    1:"Puppy",
    2:"Car",
    3:"Rabbit",
    4:"Girl",
    5:"Monkey"
}
verbs_dict = {
    10:"runs",
    20:"hits",
    30:"jumps",
    40:"drives",
    50:"barfs"
}
adv_dict = {
    100:"crazily",
    200:"dutifully",
    300:"foolishly",
    400:"merrily",
    500:"occasionally"
}
adj_dict = {
    1000:"adorable",
    2000:"clueless",
    3000:"dirty",
    4000:"odd",
    5000:"stupid"
}
pun_dict = {
    10000:"!",
    20000:".",
    30000:"...",
    40000:":)",
    50000:"?"
}
#Sentence generator
print("\n")

numberOfTimes = 0
while numberOfTimes < sentences:
    loop = 0
    while loop < sentences:
        num1 = random.randrange(0,5)
        num2 = random.randrange(0,5)
        num3 = random.randrange(0,5)
        num4 = random.randrange(0,5)
        num5 = random.randrange(0,5)
        sentence = nouns[num1] + ' ' + verbs[num2] + ' ' + adv[num3] + ' ' + adj[num4] + pun[num5]
        if search(sentences_list,sentence) == True:
            print(loop)
            print(sentence)
            duplicateLoopCount.append(loop)
            numberOfTimes = (numberOfTimes + 1)
            random.seed(time.time())
            sentences_list = []
            break

        sentences_list.append(sentence)
        line = str(loop) + " " + sentence
        #print(line)
        loop = (loop + 1)

print("\nThe Average duplicate value is: " + str(Average(duplicateLoopCount)))

print("\nDone printing, made " + str(sentences) + " sentences!")
