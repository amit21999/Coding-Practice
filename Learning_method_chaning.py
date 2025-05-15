class Pizza:
    def __init__(self, size="Medium"):
        self.size = size
        self.toppings = []
        self.crust_type = "Regular"
        self.extra_cheese = False
        self.is_baked = False

    def set_size(self, size):
        self.size = size
        return self

    def add_topping(self, topping):
        self.toppings.append(topping)
        return self

    def set_crust(self, crust_type):
        self.crust_type = crust_type
        return self

    def add_cheese(self):
        self.extra_cheese = True
        return self

    def bake(self):
        self.is_baked = True
        print("Your pizza is now baking...")
        return self

    def serve(self):
        if not self.is_baked:
            print("Please bake the pizza before serving!")
            return self

        print("\n✅ Pizza Ready!")
        print(f"Size: {self.size}")
        print(f"Crust: {self.crust_type}")
        print(f"Toppings: {', '.join(self.toppings) if self.toppings else 'None'}")
        print(f"Extra Cheese: {'Yes' if self.extra_cheese else 'No'}")
        return self


# ======================
# 🍽️ USING METHOD CHAINING
# ======================

def main():
    my_pizza = Pizza()

    my_pizza.set_size("Large")\
            .set_crust("Thin Crust")\
            .add_topping("Pepperoni")\
            .add_topping("Mushrooms")\
            .add_topping("Olives")\
            .add_cheese()\
            .bake()\
            .serve()


if __name__ == "__main__":
    main()
