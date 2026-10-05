import requests


BASE_URL = "http://127.0.0.1:5000"


def show_inventory():
    response = requests.get(f"{BASE_URL}/inventory")

    if response.status_code == 200:
        items = response.json()

        for item in items:
            print(
                f"{item['id']}: "
                f"{item['name']} | "
                f"Price: {item['price']} | "
                f"Stock: {item['stock']}"
            )
    else:
        print("Unable to get inventory.")


def view_item():
    item_id = input("Enter item ID: ")

    try:
        item_id = int(item_id)
    except ValueError:
        print("ID must be a number.")
        return

    response = requests.get(
        f"{BASE_URL}/inventory/{item_id}"
    )

    if response.status_code == 200:
        print(response.json())
    else:
        print("Item not found.")


def add_item():

    name = input("Product name: ")
    brand = input("Brand: ")
    price = input("Price: ")
    stock = input("Stock: ")
    barcode = input("Barcode: ")

    try:
        price = float(price)
        stock = int(stock)
    except ValueError:
        print("Price must be a number and stock must be an integer.")
        return

    data = {
        "name": name,
        "brand": brand,
        "price": price,
        "stock": stock,
        "barcode": barcode
    }

    response = requests.post(
        f"{BASE_URL}/inventory",
        json=data
    )

    if response.status_code == 201:
        print("Item added successfully.")
        print(response.json())
    else:
        print(response.json())


def update_item():

    item_id = input("Enter item ID: ")

    try:
        item_id = int(item_id)
    except ValueError:
        print("ID must be a number.")
        return

    price = input("New price (press Enter to skip): ")
    stock = input("New stock (press Enter to skip): ")

    data = {}

    if price:
        try:
            data["price"] = float(price)
        except ValueError:
            print("Invalid price.")
            return

    if stock:
        try:
            data["stock"] = int(stock)
        except ValueError:
            print("Invalid stock.")
            return

    if not data:
        print("Nothing to update.")
        return

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=data
    )

    if response.status_code == 200:
        print("Item updated successfully.")
        print(response.json())
    else:
        print(response.json())


def delete_item():

    item_id = input("Enter item ID: ")

    try:
        item_id = int(item_id)
    except ValueError:
        print("ID must be a number.")
        return

    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    if response.status_code == 200:
        print("Item deleted successfully.")
    else:
        print(response.json())


def find_product():

    barcode = input("Enter product barcode: ")

    response = requests.get(
        f"{BASE_URL}/products/{barcode}"
    )

    if response.status_code == 200:
        product = response.json()

        print("\nProduct found:")
        print(f"Name: {product['product_name']}")
        print(f"Brand: {product['brands']}")
        print(f"Ingredients: {product['ingredients_text']}")

    else:
        print("Product could not be found.")


def main():

    while True:

        print("\n===== INVENTORY MANAGEMENT =====")
        print("1. View inventory")
        print("2. View item")
        print("3. Add item")
        print("4. Update item")
        print("5. Delete item")
        print("6. Find product on OpenFoodFacts")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_inventory()

        elif choice == "2":
            view_item()

        elif choice == "3":
            add_item()

        elif choice == "4":
            update_item()

        elif choice == "5":
            delete_item()

        elif choice == "6":
            find_product()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()