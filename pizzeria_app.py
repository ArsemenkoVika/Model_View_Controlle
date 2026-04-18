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


class StatsManager:
   FILE_NAME = "sales.json"

   @staticmethod
   def save_order(pizza_name, final_price):
       try:
           with open(StatsManager.FILE_NAME, "r") as f:
               data = json.load(f)
       except (FileNotFoundError, json.JSONDecodeError):
           data = []

       data.append({"pizza": pizza_name, "price": final_price})
       with open(StatsManager.FILE_NAME, "w", encoding="utf-8") as f:
           json.dump(data, f, ensure_ascii=False, indent=4)


   @staticmethod
   def show_admin_stats():
       try:
           with open(StatsManager.FILE_NAME, "r") as f:
               orders = json.load(f)

       except:
           print("история заказов пуста")
           return

       total_revenue = sum(item['price'] for item in orders)
       profit = total_revenue * 0.3
       print(f"\n----АДМИН ПАНЕЛЬ---")
       print(f"Продано пицц: {len(orders)}")
       print(f"Общая выручка: {total_revenue} руб.")
       print(f"Чистая прибыль (30%): {profit} руб.")
