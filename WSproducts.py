class Product:
    def __init__(self, name, id, image, description, quantity):
        self.name = name
        self.id = id
        self.image = image
        self.description = description
        self.quantity = quantity

    def increasing_the_amount(self, number):
        self.quantity += number
        print("the available number of this product is", self.quantity)

    def decreasing_the_amount(self, number):
        self.quantity -= number
        if self.quantity < 0:  # check the amount of product #
            print("Sorry the product is unavailable")
            raise ValueError
        else:
            print("the available number of this product is", self.quantity)

    def __str__(self):
        return f"this product is {self.name}, with id {self.id}, {self.description}, and the available amount is " \
               f"{self.quantity}"


# creating user object with specification username and password
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# storage increase and decrease and tedad manfi nashe

product0 = Product("banana", 0, None, "this is a delicious fruit", 2)
print(product0)
product0.decreasing_the_amount(1)
product0.increasing_the_amount(20)
product0.decreasing_the_amount(21)
# product0.decreasing_the_amount(1)   # this line is for testing value error
