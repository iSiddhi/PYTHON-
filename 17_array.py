cars = ["Ford", "Volvo", "BMW"]
x=cars[0]
print(x)
cars[0]="toyoto"
print(cars)
x=len(cars)

for x in cars:
    print(x)

cars.append("honda")
cars.pop(1)

cars.remove("volvo")