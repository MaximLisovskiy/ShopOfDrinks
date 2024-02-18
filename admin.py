
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


def remove_employee(dict_employees, employee):
    dict_employees.pop(employee)


def change_salary_of_employee(dict_employee, employee, new_salary):
    dict_employee[employee] = new_salary



def show_employees(dict_employees):
    print(dict_employees)


def show_drinks(drinks):
    print(drinks)



def order_drink():

    for drink, price in drinks.items():
        if drink_name in drinks:
            count.append(liters * price)

    order_info = {
        "Напій": drink_name,
        "Літраж": liters,
        "Номер телефону": number_of_phone,
        "Місто": city,
        "ПІБ": surname_name_patronymic,
        "Відділення пошти": post_office,
    }
    orders.append(order_info)
    print(f"До сплати {count[0]} грн")

