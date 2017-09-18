__author__ = 'Surya'
myList = [1, 2, 3, 4, 5]
print(myList[2])
print(myList[:2])
print(myList[2:3])
print(myList)

output = ""
j = 0
for i in myList:
    output += str(i)
    if j < len(myList)-1:
        output += ", "
    j += 1


print(output)

myList = []

for i in range (0, 8):
    myList.append(i*4)

output = ""
j = 0
for i in myList:
    output += str(i)
    if j < len(myList)-1:
        output += ", "
    j += 1

print(output)

word = "P r o f e s s o r"
myList = word.split(" ")
print(myList)
output = ""
for i in myList:
    output += (i)

print(output)
