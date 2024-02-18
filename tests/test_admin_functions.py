from admin import *

def test_add_drink():
    drinks = {}
    name = "Lager"
    price = 34
    add_drink(drinks, name, price)

    assert name in drinks
    assert drinks[name] == price

def test_remove_drink():
    drinks = {}
    name = "Lager"
    price = 40
    add_drink(drinks, name, price)
    remove_drink(drinks, name)

    assert name not in drinks

def test_change_price_drinks():
    drinks = {}
    name = "Lager"
    price = 40
    new_price = 50
    add_drink(drinks, name, price)
    change_price_drink(drinks, name, new_price)

    assert drinks[name] == new_price