class Admin:
    def __init__(self, name):
        self.name = name


    def add_drink(self, title: str, price: int or float):
        if title not in self.drinks:
            self.drinks[title] = price

        if type(price) != int or float:
            return "Price can be integer or float"

    def remove_drink(self, title: str):
        if title in self.drinks:
            self.drinks.pop(title)
        else:
            return "Drink not found"

    def change_price_drink(self, drinks: dict, new_price: int):
        for title in self.drinks.keys():
            if title in drinks:
                self.drinks[title] = new_price
            else:
                return "Drink not found"

    def add_employee(self, employee: str, salary: int):
        self.dict_employees[employee] = salary

    def remove_employee(self, employee: str):
        if employee in self.dict_employees:
            self.dict_employees.pop(employee)
        else:
            return "Employee not found"

    def change_salary_of_employee(
        self, dict_employee: dict, new_salary: int
    ):
        for employee in self.dict_employees.keys():
            if employee in dict_employee:
                self.dict_employees[employee] = new_salary
            else:
                return "Employee not found"

    def show_employees(self):
        return self.dict_employees

    def show_drinks(self):
        return self.drinks
