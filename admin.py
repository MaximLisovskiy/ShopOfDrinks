def add_drink(drinks: dict, title: str, price: int):
    if title not in drinks:
        drinks[title] = price


def remove_drink(drinks: dict, title: str):
    if title in drinks:
        drinks.pop(title)


def change_price_drink(drinks: dict, title: str, new_price: int):
    for title in drinks.keys():
        if title in drinks:
            drinks[title] = new_price


def add_employee(dict_employees: dict, employee: str, salary: int):
    dict_employees[employee] = salary


def remove_employee(dict_employees: dict, employee: str):
    if employee in dict_employees:
        dict_employees.pop(employee)


def change_salary_of_employee(dict_employee: dict, employee: str, new_salary: int):
    for employee in dict_employee.keys():
        if employee in dict_employee:
            dict_employee[employee] = new_salary


def show_employees(dict_employees: dict):
    return dict_employees


def show_drinks(drinks: dict):
    return drinks

