from unittest.mock import patch

from app import app


def test_openfoodfacts_api():

    fake_response = {
        "status": 1,
        "product": {
            "product_name": "Test Milk",
            "brands": "Test Brand",
            "ingredients_text": "Water, milk"
        }
    }

    with patch("app.requests.get") as mock_get:

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = fake_response

        client = app.test_client()

        response = client.get(
            "/products/123456789"
        )

        assert response.status_code == 200
        assert response.json["product_name"] == "Test Milk"

        mock_get.assert_called_once()