shopping_list = {
    "piekarnia": ['chleb', 'bułki', 'pączek'],
    "warzywniak": ['marchew', 'seler', 'rukola']
}

print("Lista zakupów")
amount_products = 0
for place, products in shopping_list.items():
    products_capitalize = [product.capitalize() for product in products]
    amount_products += len(products)
    print(f"Ide do {place.capitalize()} i kupuję tam następujące rzeczy: {products_capitalize}")
print(f"W sumie kupuję {str(amount_products)} produktów")
