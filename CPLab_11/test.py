srepair = "0000fixed!"

print(srepair)
print(srepair.strip("0"))



sides = "       <--I would love to touch the sides-->         "

#original: nothing removed
print("|" + sides + "|")

#removes leading whitespace....
print("|" + sides.lstrip() + "|")

#removes trailning whitespace...
print("|" + sides.rstrip() + "|")


print("|" + sides.strip(" ") + "|")


name = "pRofesSor haNdSome"

name = name.upper()
print(name)

name = name.lower()
print(name)

name = name.title()
print(name)

name = "pRofesSor haNdSome"
name = name.swapcase()
print(name)


print (name.replace("s", "$"))

sentence = "Many grannies ran to catch the aardvark"

print (sentence.replace ("a", "@"))


word = "aardvark"
do = "zebra"

print(word<do)

if word > do:
    print("Word comes first")

if word < do:
    print("Do comes first")

name = str("James")
print(name)

