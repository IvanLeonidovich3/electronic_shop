"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item


@pytest.fixture
def test_class():
    item = Item(name='some', price=7, quantity=52, )
    return item


def test_calculate_total_price(test_class):
    """общая стоимость конкретного товара"""
    assert test_class.calculate_total_price() == 364


def test_apply_discount(test_class):
    test_class.apply_discount()
    assert test_class.price == 7


def test_string_to_number():
    assert Item.string_to_number("10.5") == 10
    with pytest.raises(ValueError):
        Item.string_to_number("abc")
    assert Item.string_to_number(10) == None


def test_instantiate_from_csv():
    Item.instantiate_from_csv("../src/items.csv")
    assert len(Item.all) == 5
