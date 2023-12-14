"""myTuple = ("apple", "banana", "cheery")
y=list(myTuple)
# y[1]="kiwi"
# myTuple=tuple(y)
# print(myTuple)

y.append("orange")
myTuple=tuple(y)
print(myTuple)  """



# unpack tuples
fruits = ("apple", "banana", "cherry")
'''(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)'''

# underasterisk
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


#





