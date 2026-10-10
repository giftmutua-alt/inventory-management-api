
import builtins
from unittest.mock import Mock, patch

import cli


@patch("cli.requests.get")
def test_show_inventory(mock_get, capsys):
    mock_get.return_value = Mock(
        status_code=200,
        json=lambda: [
            {
                "id": 1,
                "name": "Milk",
                "price": 100,
                "stock": 5,
            }
        ],
    )

    cli.show_inventory()

    assert "Milk" in capsys.readouterr().out


@patch("cli.requests.get")
def test_view_item(mock_get, capsys, monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "1")
    mock_get.return_value = Mock(
        status_code=200,
        json=lambda: {"id": 1, "name": "Milk"},
    )

    cli.view_item()

    assert "Milk" in capsys.readouterr().out


@patch("cli.requests.post")
def test_add_item(mock_post, capsys, monkeypatch):
    answers = iter(["Milk", "Example Brand", "100", "5", "12345"])
    monkeypatch.setattr(builtins, "input", lambda _: next(answers))
    mock_post.return_value = Mock(
        status_code=201,
        json=lambda: {"id": 3, "name": "Milk"},
    )

    cli.add_item()

    assert "added successfully" in capsys.readouterr().out


@patch("cli.requests.patch")
def test_update_item(mock_patch, capsys, monkeypatch):
    answers = iter(["1", "120", ""])
    monkeypatch.setattr(builtins, "input", lambda _: next(answers))
    mock_patch.return_value = Mock(
        status_code=200,
        json=lambda: {"id": 1, "price": 120},
    )

    cli.update_item()

    assert "updated successfully" in capsys.readouterr().out


@patch("cli.requests.delete")
def test_delete_item(mock_delete, capsys, monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "1")
    mock_delete.return_value = Mock(status_code=200)

    cli.delete_item()

    assert "deleted successfully" in capsys.readouterr().out


@patch("cli.requests.get")
def test_find_product(mock_get, capsys, monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "12345")
    mock_get.return_value = Mock(
        status_code=200,
        json=lambda: {
            "product_name": "Milk",
            "brands": "Example Brand",
            "ingredients_text": "Milk",
        },
    )

    cli.find_product()

    assert "Product found" in capsys.readouterr().out
