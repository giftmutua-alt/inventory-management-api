from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


# Temporary inventory database
inventory = [
    {
        "id": 1,
        "name": "Organic Almond Milk",
        "brand": "Silk",
        "price": 450,
        "stock": 10,
        "barcode": "03000671234",
        "ingredients": "Filtered water, almonds, cane sugar"
    },
    {
        "id": 2,
        "name": "Nutella",
        "brand": "Ferrero",
        "price": 600,
        "stock": 15,
        "barcode": "3017624010701",
        "ingredients": "Sugar, palm oil, hazelnuts, cocoa"
    }
]


# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Inventory Management API"
    })


# GET /inventory
# Return all inventory items
@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200


# GET /inventory/<id>
# Return one inventory item
@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):

    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item), 200

    return jsonify({
        "error": "Inventory item not found"
    }), 404


# POST /inventory
# Add a new inventory item
@app.route("/inventory", methods=["POST"])
def create_item():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    required_fields = ["name", "brand", "price", "stock"]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"{field} is required"
            }), 400

    new_id = max(
        [item["id"] for item in inventory],
        default=0
    ) + 1

    new_item = {
        "id": new_id,
        "name": data["name"],
        "brand": data["brand"],
        "price": data["price"],
        "stock": data["stock"],
        "barcode": data.get("barcode", ""),
        "ingredients": data.get("ingredients", "")
    }

    inventory.append(new_item)

    return jsonify(new_item), 201


# PATCH /inventory/<id>
# Update an inventory item
@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    for item in inventory:

        if item["id"] == item_id:

            # Only update fields provided by the user
            if "name" in data:
                item["name"] = data["name"]

            if "brand" in data:
                item["brand"] = data["brand"]

            if "price" in data:
                item["price"] = data["price"]

            if "stock" in data:
                item["stock"] = data["stock"]

            if "barcode" in data:
                item["barcode"] = data["barcode"]

            if "ingredients" in data:
                item["ingredients"] = data["ingredients"]

            return jsonify(item), 200

    return jsonify({
        "error": "Inventory item not found"
    }), 404


# DELETE /inventory/<id>
# Delete an inventory item
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):

    for item in inventory:

        if item["id"] == item_id:

            inventory.remove(item)

            return jsonify({
                "message": "Inventory item deleted successfully"
            }), 200

    return jsonify({
        "error": "Inventory item not found"
    }), 404


# GET /products/<barcode>
# Fetch product information from OpenFoodFacts
@app.route("/products/<barcode>", methods=["GET"])
def get_product_from_api(barcode):

    url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}"

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "InventoryManagementLab/1.0"
            }
        )

        if response.status_code != 200:
            return jsonify({
                "error": "Unable to contact OpenFoodFacts"
            }), 502

        data = response.json()

        if data.get("status") != 1:
            return jsonify({
                "error": "Product not found"
            }), 404

        product = data.get("product", {})

        result = {
            "barcode": barcode,
            "product_name": product.get("product_name", ""),
            "brands": product.get("brands", ""),
            "ingredients_text": product.get(
                "ingredients_text",
                ""
            )
        }

        return jsonify(result), 200

    except requests.RequestException:
        return jsonify({
            "error": "OpenFoodFacts API request failed"
        }), 502


if __name__ == "__main__":
    app.run(debug=True)