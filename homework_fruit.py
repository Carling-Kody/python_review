
class Fruit(object):
    seeds = "shiz loads"
    recom_daily_dose = 3

    def __init__(self):
        print("You just created a fruit object")

    def nutrition(self):
        print("You are eating fruit so is probably good for you")

    def fruit_shape(self):
        print("All fruit has a different shape")


class Apple(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("you just created an apple object and inherited from fruit")

    def nutrition(self):
        super(Apple, self).nutrition()
        print("An apple a day keeps the doctor away!")

    def color(self):
        print("Apples are usually either Green, Red, or Yellow")


f = Fruit()
f.nutrition()
f.fruit_shape()
f.seeds = str(30)
print(f.seeds)

print("*" * 30)

a = Apple()
a.color()
a.fruit_shape()
a.nutrition()
a.color()
print(a.seeds)
