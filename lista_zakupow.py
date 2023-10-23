shopping_list = {
    "piekarnia": ['chleb', 'bułki', 'pączek'],
    "warzywniak": ['marchew', 'seler', 'rukola']
}

print("Lista zakupów")

for place, products in shopping_list.items():
    products_capitalize = [product.capitalize() for product in products]
    print(f"Ide do {place.capitalize()} i kupuję tam następujące rzeczy: {products_capitalize}")