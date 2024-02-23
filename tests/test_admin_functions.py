from admin import Admin
import unittest


class TestAdminFunction(unittest.TestCase):


    def test_add_drink(self):
        admin = Admin("Maxim Lisovskiy")
        drinks = {"Лагер": 30, "Горілка-Хортиця": 180}
        title = "Obolon"
        price = 34
        admin.add_drink(drinks, title, price)

        assert title in drinks
        assert drinks[title] == price
        assert type(drinks) == dict
        assert type(title) == str
        assert type(price) == int

    def test_remove_drink(self):
        admin = Admin("Maxim Lisovskiy")
        drinks = {"Лагер": 30, "Горілка-Хортиця": 180}
        title = "Горілка-Хортиця"
        admin.remove_drink(drinks, title)

        assert title not in drinks
        assert type(drinks) == dict
        assert type(title) == str


    def test_change_price_drinks(self):
        admin = Admin("Maxim Lisovskiy")
        drinks = {"Лагер": 30, "Горілка-Хортиця": 180}
        title = "Лагер"
        new_price = 50
        admin.change_price_drink(drinks, title, new_price)

        assert title in drinks
        assert drinks[title] == new_price
        assert type(drinks) == dict
        assert type(title) == str
        assert type(new_price) == int

    def test_add_employee(self):
        admin = Admin("Maxim Lisovskiy")
        dict_employees = {}
        employee = "Manager"
        salary = 4500
        admin.add_employee(dict_employees, employee, salary)

        assert employee in dict_employees
        assert dict_employees[employee] == salary
        assert type(employee) == str
        assert type(salary) == int
        assert type(dict_employees) == dict


    def test_remove_employee(self):
        admin = Admin("Maxim Lisovskiy")
        dict_employees = {"Manager": 500}
        employee = "Manager"
        admin.remove_employee(dict_employees, employee)

        assert employee not in dict_employees
        assert type(employee) == str
        assert type(dict_employees) == dict


    def test_change_salary_of_employee(self):
        admin = Admin("Maxim Lisovskiy")
        dict_employees = {"Manager": 4500}
        employee = "Manager"
        new_salary = 5000
        admin.change_salary_of_employee(dict_employees, employee, new_salary)

        assert dict_employees[employee] == new_salary
        assert type(dict_employees) == dict
        assert type(employee) == str
        assert type(new_salary) == int

    def test_show_employee(self):
        admin = Admin("Maxim Lisovskiy")
        dict_employees = {"Manager": 4500}

        assert admin.show_employees(dict_employees) == dict_employees
        assert type(dict_employees) == dict


    def test_show_drinks(self):
        admin = Admin("Maxim Lisovskiy")
        drinks = {"Лагер": 30, "Горілка-Хортиця": 180}

        assert admin.show_drinks(drinks) == drinks
        assert type(drinks) == dict
