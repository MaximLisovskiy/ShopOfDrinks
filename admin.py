class Admin:
    def __init__(self, name: str):
        self.full_name = name

    def add_drink(self, drinks: dict, title: str, price: int):
        if title not in drinks:
            drinks[title] = price

        if type(price) != int:
            return "Price can be integer or float"

    def remove_drink(self, drinks: dict, title: str):
        if title in drinks:
            drinks.pop(title)
        else:
            return "Drink not found"

    def change_price_drink(self, drinks: dict, title: str, new_price: int):
        if title in drinks:
            drinks[title] = new_price
        else:
            return "Drink not found"

    def add_employee(self, dict_employees: dict, employee: str, salary: int):
        dict_employees[employee] = salary

    def remove_employee(self, dict_employees: dict, employee: str):
        if employee in dict_employees:
            dict_employees.pop(employee)
        else:
            return "Employee not found"

    def change_salary_of_employee(self, dict_employees: dict, employee: str, new_salary: int):
        if employee in dict_employees:
            dict_employees[employee] = new_salary
        else:
            return "Employee not found"

    def show_employees(self, dict_employees: dict):
        return dict_employees

    def show_drinks(self, drinks: dict):
        return drinks
