
def add_drink(drinks, name, price):
    drinks[name] = price

def remove_drink(drinks, name):
        drink_name_parts = name.split()
        if len(drink_name_parts) == 1:
            drink_name = drink_name_parts[0]
            if drink_name in drinks:
                drinks.pop(name)
        elif len(drink_name_parts) >= 2:
            drink_name = "-".join(drink_name_parts)
            if drink_name in drinks:
                drinks.pop(drink_name)


def change_price_drink(drinks, name, new_price):
        drinks[name] = new_price


def add_employee(dict_employees, employee, salary):
    dict_employees[employee] = salary

# def remove_employee():
#     if choose_Admin == 5:
#         remove_employee = input(
#             "Введіть посаду працівника для звільнення з роботи: "
#         ).title()
#         if remove_employee in dict_of_employees:
#             dict_of_employees.pop(remove_employee)
#
#
# def change_salary_of_employee():
#     if choose_Admin == 6:
#         for employee in dict_of_employees:
#             if employee in dict_of_employees:
#                 position = input("Введіть посаду для зміни заробітньої плати: ").title()
#                 new_salary = int(input("Введіть нову заробітню плату: "))
#                 dict_of_employees[position] = new_salary
#
#
#
# def show_employees():
#     if choose_Admin == 7:
#         print(dict_of_employees)
#
#
# def show_drinks():
#     if choose_Admin == 8:
#         print(drinks)
#
#
# orders = []
#
#
# def order_drink():
#     count = []
#     if choose_Admin == 10:
#         drink_name = input("Введіть назву напою для замовлення: ").title()
#         liters = float(input("Введіть літраж напою: "))
#         number_of_phone = int(input("Введіть номер телефону: "))
#         city = input("Введіть місто: ").title()
#         surname_name_patronymic = input("Ваш ПІБ: ").title()
#         post_office = int(input("Введіть відділення пошти: "))
#
#         for drink, price in drinks.items():
#             if drink_name in drinks:
#                 count.append(liters * price)
#
#         order_info = {
#             "Напій": drink_name,
#             "Літраж": liters,
#             "Номер телефону": number_of_phone,
#             "Місто": city,
#             "ПІБ": surname_name_patronymic,
#             "Відділення пошти": post_office,
#         }
#         orders.append(order_info)
#         print(f"До сплати {count[0]} грн")
#
#
# def back():
#     if choose_Admin == 11:
#         function_of_admin()
