"""  len() """
print(len("Robinette"))
s = "sausages"
m = "Yolo swag"

""" Slice and Range Slice """
print(s[3: ])

""" index() """
print(s.index("g"))

name = input("Please enter your full name: ")

print("Good morning " + name[ : name.index(" ")])
print (name[name.index(" "):])