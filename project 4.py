import pandas as pd

df = pd.read_csv("products.csv")

class Product:
    def __init__(self, prod_id, price):
        self.prod_id = prod_id
        self.price = price

    def apply_discount(self, percent_off):
        self.price = self.price - (self.price * percent_off / 100)

electronics_df = df[df["Category"] == "Electronics"].copy()

updated_prices = []

for index, row in electronics_df.iterrows():
    product = Product(row["Product_ID"], row["Price"])
    product.apply_discount(20)
    updated_prices.append(product.price)

electronics_df["Price"] = updated_prices
electronics_df["Promo_Active"] = "Yes"

electronics_df.to_csv("holiday_promos.csv", index=False)
print("File created successfully: holiday_promos.xlsx")