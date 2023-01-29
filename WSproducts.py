class Product:
    def __init__(self, name, id, image, description):
        self.name = name
        self.id = id
        self.image = image
        self.description = description

    def __str__(self):
        return f"this product is {self.name}, with id {self.id}, {self.description}"


product0 = Product("banana", 0, None, "this is a delicious fruit")
print(product0)