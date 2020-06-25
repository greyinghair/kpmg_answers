## Q6
# Create a Sandwich class with the attributes order_number and ingredients.
# i. The ingredients attributes is given as a list - (Note: use list() to enable this).
# Only the ingredients attributes will be given as input.
# ii. The order attribute will be a method that counts the order number.
# iii. Make three methods for the following favourite sandwiches, for customers who don't want to create a sandwich:
# vegan_hot - vegan cheese, meatless meatballs, jalapenos
# meat_feast - steak, peppers, cheese
# veggie - tomato, spinach, mushroom, eggs


class Sandwich:
    order_num = 0

    def __init__(self,*args):
        self.ingredients = list(args) # add all passed parameters into a list called ingredients
        print(self.ingredients) # print ingredients
        self.order_num = self.order() # pass something to order method

    def order(self):
        Sandwich.order_num += 1 # increment order number by 1 each time
        print("Order # " + str(self.order_num)) # print order number

    def vegan_hot(): # don't use self as this will be called first and pass parameters back to the Class
        return Sandwich(["vegan cheese", "meatless meatballs", "jalapenos"])

    def meat_feast():
        return Sandwich(["steak, peppers, cheese"])

    def veggie():
        return Sandwich(["tomato, spinach, mushroom, eggs"])

# Create your own sandwich
Sandwich("carrots","tomatoes")
Sandwich("ham","eggs")
Sandwich("cheese","tomatoes","no mayo")

# choose pre-made sandwiches
Sandwich.vegan_hot()
Sandwich.meat_feast()
Sandwich.veggie()