import json

class Pizza:
   def __init__(self, name, ingredients, price):
       self.name = name
       self.ingredients = ingredients
       self.price = price

   def __str__(self):
       return f"{self.name} [{', '.join(self.ingredients)}] - {self.price} руб."


   class PizzaFactory:
       @staticmethod
       def create_pizza(choice, custom_data=None):
           recipes = {
               "1": ("Маргарита", ["томаты", "моцарелла"], 300),
               "2": ("Пепперони", ["пепперони", "моцарелла"], 400),
               "3": ("4 Сыра", ["чеддер", "пармезан", "дорблю", "моцарелла"], 450),
               "4": ("Гавайская", ["курица", "ананас"], 380),
               "5": ("Мясная", ["бекон", "говядина", "соус барбекю"], 500)
           }
           if choice in recipes:
               return Pizza(*recipes[choice])
           elif choice == "6" and custom_data:
               return Pizza(custom_data['name'], custom_data['ingreds'], custom_data['price'])
           return None