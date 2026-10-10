# Inventory Management System

A Flask REST API for managing inventory items, with an interactive command-line interface (CLI) and OpenFoodFacts product lookup.

## Features

- View all inventory items.
- View a single inventory item by ID.
- Add, update, and delete inventory items.
- Retrieve product information from OpenFoodFacts using a barcode.
- Use a menu-driven CLI to manage inventory.
- Run automated tests with pytest.

## Requirements

- Python 3
- pip
- Internet connection for OpenFoodFacts lookups

## Installation

Clone the repository:

```bash
git clone https://github.com/giftmutua-alt/inventory-management-api.git
cd inventory-management-api
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Start the Flask server:

```bash
python app.py
```

The API runs at `http://127.0.0.1:5000`.

Keep this terminal running while using the CLI.

## Running the CLI

Open a second terminal, navigate to the project directory, and activate the virtual environment:

```bash
cd inventory-management-api
source venv/bin/activate
python cli.py
```

Follow the menu prompts to view, add, update, delete, or find products.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/inventory` | Retrieve all inventory items |
| GET | `/inventory/<id>` | Retrieve one item by ID |
| POST | `/inventory` | Create an inventory item |
| PATCH | `/inventory/<id>` | Update an existing item |
| DELETE | `/inventory/<id>` | Delete an inventory item |
| GET | `/products/<barcode>` | Retrieve product details from OpenFoodFacts |

### Example: Create an inventory item

Send a POST request to `/inventory` with JSON data:

```json
{
  "name": "Oat Milk",
  "brand": "Example Brand",
  "price": 350,
  "stock": 10,
  "barcode": "1234567890123"
}
```

### External API

The application retrieves product details from the OpenFoodFacts API using a product barcode. An internet connection is required for this feature.

## Testing

Activate the virtual environment and run:

```bash
python -m pytest -v
```

## Project Structure

```text
inventory-management-api/
├── app.py
├── cli.py
├── requirements.txt
├── README.md
└── tests/
    ├── test_app.py
    └── test_openfoodfacts.py
```

## Features

- View all inventory items
- View a single item
- Add inventory items
- Update prices and stock
- Delete inventory items
- Search OpenFoodFacts by barcode
- CLI interface
- Automated tests

## Installation

Clone the repository:

git clone YOUR_REPOSITORY_URL

Enter the project:

cd inventory-management-api

Create a virtual environment:

python3 -m venv venv

Activate it:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

## Run the API

python app.py

The API runs at:

http://127.0.0.1:5000

## Run the CLI

In another terminal:

source venv/bin/activate

python cli.py

## API Routes

GET /inventory
GET /inventory/<id>
POST /inventory
PATCH /inventory/<id>
DELETE /inventory/<id>

## External API

The application uses OpenFoodFacts to retrieve product information by barcode.

## Testing

Run:

pytest
## Testing

Run the test suite with:

python -m pytest
