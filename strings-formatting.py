"""
Examples to show how string formatting works in python
"""

city = "nyc"
event = "show"

print("Welcome to " + city + " and enjoy the " + event)
print("Welcome to %s" % city)
print("Welcome to %s and enjoy the %s" % (city, event))
print("Welcome to {} and Enjoy the {}".format(city, event))

print("********************")
a = "one two three"


k = a.split()

print(k)
print(k[4])
x ='abc'
print(x[-1])
print(x[1])
print(x[2])

b = "test"
t = b[:2]
print(t)
