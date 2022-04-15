myList = []

word = ["Cat", "Dog", "Cow"]

cnt = 0
while cnt < 10:
   
    cnt = cnt + 1
    if word[cnt%3] == "Cow":
        myList.append(word[cnt % 3] + "-" + str(cnt))
        break

   
print (cnt)

a = 10
b = 20
c = 30

sum = a + b + c

print (sum)
