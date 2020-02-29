"""
Dictionary Methods
"""

car = {'make': 'bmw', 'model': '550i', 'year': 2016}
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}

print(car.keys())
print("")
print(cars.keys())
print()
print(car.values())
print()
print(cars.values())
print()
print(car.items())
print("")

car_copy = car.copy()
print(car_copy)
print("")
print(car.pop('model'))
print("")
print(car)
