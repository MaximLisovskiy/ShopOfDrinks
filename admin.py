class Admin:
    def __init__(self):
        self.drinks = {}
        self.dict_employees = {}

    def add_drink(self, drinks: dict, title: str, price: int):
        if title not in self.drinks:
            self.drinks[title] = price

    def remove_drink(self, drinks: dict, title: str):
        if title in self.drinks:
            self.drinks.pop(title)

    def change_price_drink(self, drinks: dict, title: str, new_price: int):
        for title in self.drinks.keys():
            if title in drinks:
                self.drinks[title] = new_price

    def add_employee(self, dict_employees: dict, employee: str, salary: int):
        self.dict_employees[employee] = salary

    def remove_employee(self, dict_employees: dict, employee: str):
        if employee in self.dict_employees:
            self.dict_employees.pop(employee)

    def change_salary_of_employee(
        self, dict_employee: dict, employee: str, new_salary: int
    ):
        for employee in self.dict_employees.keys():
            if employee in dict_employee:
                self.dict_employees[employee] = new_salary

    def show_employees(self, dict_employees: dict):
        return self.dict_employees

    def show_drinks(self, drinks: dict):
        return self.drinks

