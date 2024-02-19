def add_drink(drinks, title, price):
    drinks[title] = price


def remove_drink(drinks, title):
    drinks.pop(title)


def change_price_drink(drinks, title, new_price):
    drinks[title] = new_price


def add_employee(dict_employees, employee, salary):
    dict_employees[employee] = salary


def remove_employee(dict_employees, employee):
    dict_employees.pop(employee)


def change_salary_of_employee(dict_employee, employee, new_salary):
    dict_employee[employee] = new_salary


def show_employees(dict_employees):
    return dict_employees


def show_drinks(drinks):
    return drinks


def order_drink():
    pass
