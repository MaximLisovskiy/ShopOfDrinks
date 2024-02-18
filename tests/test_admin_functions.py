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


def test_add_employee():
    dict_employees = {}
    employee = "Manager"
    salary = 4500
    add_employee(dict_employees, employee, salary)

    assert employee in dict_employees
    assert dict_employees[employee] == salary

def test_remove_employee():
    dict_employees = {}
    employee = "Manager"
    salary = 4500
    add_employee(dict_employees, employee, salary)
    remove_employee(dict_employees, employee)

    assert employee not in dict_employees


def test_change_salary_of_employee():
    dict_employees = {}
    employee = "Manager"
    salary = 4500
    new_salary = 5000
    add_employee(dict_employees, employee, salary)
    change_salary_of_employee(dict_employees, employee, new_salary)

    assert dict_employees[employee] == new_salary


def test_show_employee():
    dict_employees = {}
    employee = "Manager"
    salary = 4500
    add_employee(dict_employees, employee, salary)
    show_employees(dict_employees)

    assert show_employees(dict_employees) == print(dict_employees)


def test_show_drinks():
    drinks = {}
    name = "Lager"
    price = 34
    add_drink(drinks, name, price)
    show_drinks(drinks)

    assert show_drinks(drinks) == print(drinks)

