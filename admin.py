def add_drink(drinks, title, price):
    if title not in drinks:
        drinks[title] = price


def remove_drink(drinks, title):
    if title in drinks:
        drinks.pop(title)


def change_price_drink(drinks, title, new_price):
    for title in drinks.keys():
        if title in drinks:
            drinks[title] = new_price


def add_employee(dict_employees, employee, salary):
    dict_employees [employee] = salary


def remove_employee(dict_employees, employee):
    if employee in dict_employees:
        dict_employees.pop(employee)


def change_salary_of_employee(dict_employee, employee, new_salary):
    for employee in dict_employee.keys():
        if employee in dict_employee:
            dict_employee[employee] = new_salary


def show_employees(dict_employees):
    return dict_employees


def show_drinks(drinks):
    return drinks

