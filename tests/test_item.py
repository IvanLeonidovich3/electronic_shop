"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item
from src.pathich import Csv_path, No_file, Csv_test
from src.phone import Phone


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


def test__item_repr():
    item1 = Item('Смартфон', 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test__item_str():
    item1 = Item('Смартфон', 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_instantiate_from_csv():
    Item.instantiate_from_csv(Csv_path)
    assert len(Item.all) == 5
    assert Item.instantiate_from_csv(Csv_path) is True
    assert Item.instantiate_from_csv(No_file) is "Отсутствует файл items.csv"
    assert Item.instantiate_from_csv(Csv_test) is "Файл items.csv поврежден"