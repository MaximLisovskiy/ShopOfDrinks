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
