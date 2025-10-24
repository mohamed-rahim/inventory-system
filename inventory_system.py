import json

FILE_NAME = "products.json"
products = []

def save_products():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(products, file, indent=4)
        print("Products saved successfully!")
    except Exception as e:
        print(f"Error saving products: {e}")

def load_products():
    global products
    try:
        with open(FILE_NAME, "r") as file:
            products = json.load(file)
        print(f"Loaded {len(products)} products from file.")
    except FileNotFoundError:
        print("No existing product file found — starting fresh.")
    except json.JSONDecodeError:
        print("File found but data is corrupted. Starting with empty list.")
        products = []



# inventory_system.py

def main_menu():
    print("\n=== Hami MiniMarket Inventory System ===")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Stock")
    print("4. Calculate Total Value")
    print("5. Exit")

# List to store products
products = []

def add_product():
    print("\n--- Add New Product ---")
    name = input("Enter product name: ")
    category = input("Enter product category: ")

    # Validate that price and quantity are numbers
    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
    except ValueError:
        print("Invalid input! Price must be a number and quantity must be an integer.")
        return  # exit the function early

    # Store product details in a dictionary
    product = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }

    # Add to the main product list
    products.append(product)
    print(f"{name} added successfully!")

def view_products():
    print("\n--- Product List ---")

    if not products:
        print("No products found. Please add some first.")
        return

    print(f"{'Name':<15} {'Category':<15} {'Price':<10} {'Quantity':<10}")
    print("-" * 50)

    for product in products:
        print(f"{product['name']:<15} {product['category']:<15} "
              f"${product['price']:<10.2f} {product['quantity']:<10}")

    print("-" * 50)


def update_stock():
    print("\n--- Update Product Stock ---")

    if not products:
        print("No products available to update.")
        return

    name = input("Enter the product name to update: ")

    # Search for product
    for product in products:
        if product['name'].lower() == name.lower():
            try:
                new_quantity = int(input(f"Enter new quantity for {product['name']}: "))
                product['quantity'] = new_quantity
                print(f"✅ Stock for {product['name']} updated successfully!")
                return
            except ValueError:
                print("Invalid input! Quantity must be an integer.")
                return

    print("Product not found.")


def calculate_total_value():
    print("\n--- Calculate Total Stock Value ---")

    if not products:
        print("No products available to calculate value.")
        return

    # Using list comprehension to calculate total value
    total_value = sum(p['price'] * p['quantity'] for p in products)
    print(f"Total stock value: ${total_value:.2f}")


def main():
    load_products()
    while True:
        main_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_product()
            save_products()
        elif choice == "2":
            view_products()
        elif choice == "3":
            update_stock()
            save_products()
        elif choice == "4":
            calculate_total_value()
        elif choice == "5":
            save_products()
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
