def choose_the_option():
    option = int(input("Вибери спеціальність: \n" "1. Адмін\n"))
    return option



drinks = {
    "Лагер": 30,
    "Ель": 35,
    "Оболонь": 28,
    "Чернігівське": 30,
    "Львівське": 32,
    "Обрій": 31,
    "Горілка-Хортиця": 180,
    "Горілка-Хлібна слобода": 200,
    "Горілка-Вознесенська": 150,
}


def function_of_admin():
    if choose_the_option() == 1:
        choose_Admin = int(
            input(
                "Опції Адміна:\n"
                "1. Додати до асортименту напій\n"
                "2. Видалити з асортименту напій\n"
                "3. Змінити ціну на товар\n"
                "4. Прийняти на роботу працівника\n"
                "5. Звільнити з роботи працівника\n"
                "6. Змінити заробітню плату працівнику\n"
                "7. Переглянути список робітників\n"
                "8. Переглянути список напоїв\n"
                "9. Переглянути замовлений товар\n"
                "10. Замовити напій\n"
                "11. Назад\n"
                "12. Вийти\n"
            )
        )
        return choose_Admin



def add_drink():
    if function_of_admin() == 1:
        name = input("Введіть назву напою: ").title()
        price = int(input("Введіть ціну напою: "))
        if name not in drinks:
            drinks[name] = price

def remove_drink():
    if function_of_admin() == 2:
        drink = input("Введіть напій для видалення: ").title()
        drink_name_parts = drink.split()
        if len(drink_name_parts) == 1:
            drink_name = drink_name_parts[0]
            if drink_name in drinks:
                drinks.pop(drink)
            else:
                print("Такого напою не існує")
        elif len(drink_name_parts) >= 2:
            drink_name = "-".join(drink_name_parts)
            if drink_name in drinks:
                drinks.pop(drink_name)
            else:
                print("Такого напою не існує")



def change_price_drink():
    if function_of_admin() == 3:
        drink_name_input = input(
            "Введіть назву напою ціну якого хочете змінити: "
        ).title()

        # Заносимо в список напій який має одне слова
        drink_name_parts = drink_name_input.split()
        if len(drink_name_parts) == 1:
            drink_name = drink_name_parts[0]
            if drink_name in drinks:
                new_price = int(input("Введіть нову ціну напою: "))
                if new_price >= 0:
                    drinks[drink_name] = new_price
                else:
                    print("Ціна не може бути менше 0 грн")
        else:
            print("Такого напою не існує")

        if len(drink_name_parts) >= 2:
            drink_name = "-".join(drink_name_parts)
            if drink_name in drinks:
                new_price = int(input("Введіть нову ціну напою: "))
                if new_price >= 0:
                    drinks[drink_name] = new_price
                else:
                    print("Ціна не може бути менше 0 грн")
        else:
            print("Такого напою не існує")



dict_of_employees = {}


def add_employee():
    if function_of_admin() == 4:
        add_employee = input(
            "Введіть посаду працівника для прийняття на роботу: "
        ).title()
        salary = int(input("Введіть заробітню плату для працівника: "))
        dict_of_employees[add_employee] = salary

def remove_employee():
    if function_of_admin() == 5:
        remove_employee = input(
            "Введіть посаду працівника для звільнення з роботи: "
        ).title()
        if remove_employee in dict_of_employees:
            dict_of_employees.pop(remove_employee)


def change_salary_of_employee():
    if function_of_admin() == 6:
        for employee in dict_of_employees:
            if employee in dict_of_employees:
                position = input("Введіть посаду для зміни заробітньої плати: ").title()
                new_salary = int(input("Введіть нову заробітню плату: "))
                dict_of_employees[position] = new_salary



def show_employees():
    if function_of_admin() == 7:
        print(dict_of_employees)


def show_drinks():
    if function_of_admin() == 8:
        print(drinks)


show_drinks()

orders = []


def order_drink():
    count = []
    if function_of_admin() == 10:
        drink_name = input("Введіть назву напою для замовлення: ").title()
        liters = float(input("Введіть літраж напою: "))
        number_of_phone = int(input("Введіть номер телефону: "))
        city = input("Введіть місто: ").title()
        surname_name_patronymic = input("Ваш ПІБ: ").title()
        post_office = int(input("Введіть відділення пошти: "))

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


