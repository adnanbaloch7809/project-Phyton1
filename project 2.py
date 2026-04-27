import pandas as pd

class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def use_item(self, amount):
        self.quantity -= amount

df = pd.read_csv("Morning_stock.csv")

df.columns = df.columns.str.strip()

df.rename(columns={"Qty_kg": "Current_Quantity"}, inplace=True)

coffee_row = df[df["Ingredient"] == "Coffee Beans"]

name = coffee_row.iloc[0]["Ingredient"]
quantity = coffee_row.iloc[0]["Current_Quantity"]

coffee = Ingredient(name, quantity)

coffee.use_item(2.5)

df.rename(columns={"Qty_kg": "Current_Quantity"}, inplace=True)

df.to_csv("evening_stock.csv", index=False)

print("Evening stock report created successfully!")