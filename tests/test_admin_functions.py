from admin import *


def test_add_drink():
    drinks = {"Лагер": 30, "Горілка-Хортиця": 180}
    title = "Obolon"
    price = 34
    add_drink(drinks, title, price)

    assert title in drinks
    assert drinks[title] == price



def test_remove_drink():
    drinks = {"Лагер": 30, "Горілка-Хортиця": 180}
    title = "Горілка-Хортиця"
    remove_drink(drinks, title)

    assert title not in drinks


def test_change_price_drinks():
    drinks = {"Лагер": 30, "Горілка-Хортиця": 180}
    title = "Лагер"
    new_price = 50
    change_price_drink(drinks, title, new_price)

    assert title in drinks
    assert drinks[title] == new_price


def test_add_employee():
    dict_employees = {}
    employee = "Manager"
    salary = 4500
    add_employee(dict_employees, employee, salary)

    assert employee in dict_employees
    assert dict_employees[employee] == salary

def test_remove_employee():
    dict_employees = {"Manager": 500}
    employee = "Manager"
    remove_employee(dict_employees, employee)

    assert employee not in dict_employees


def test_change_salary_of_employee():
    dict_employees = {"Manager": 4500}
    employee = "Manager"
    new_salary = 5000
    change_salary_of_employee(dict_employees, employee, new_salary)

    assert dict_employees[employee] == new_salary


def test_show_employee():
    dict_employees = {"Manager": 4500}
    show_employees(dict_employees)

    assert print(show_employees(dict_employees)) == print(dict_employees)

def test_show_drinks():
    drinks = {"Лагер": 30, "Горілка-Хортиця": 180}
    show_drinks(drinks)

    assert print(show_drinks(drinks)) == print(drinks)

