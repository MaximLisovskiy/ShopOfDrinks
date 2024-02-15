def Choose_the_option():
    option = int(
        input("Вибери спеціальність: \n" "1. Адмін\n" "2. Менеджер\n" "3. Покупець\n")
    )
    return option


option = Choose_the_option()

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

def Function_of_admin():
    if option == 1:
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


choose_Admin = Function_of_admin()

def Add_or_remove_drink():
    if choose_Admin == 1:
        name = input("Введіть назву напою: ").title()
        price = int(input("Введіть ціну напою: "))
        if name not in drinks:
            drinks[name] = price

    if choose_Admin == 2:
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


Add_or_remove_drink()

def Change_price_drink():
    if choose_Admin == 3:
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


Change_price_drink()

dict_of_employees = {}


def Add_and_assign_salary_or_remove_employee():
    if choose_Admin == 4:
        add_employee = input(
            "Введіть посаду працівника для прийняття на роботу: "
        ).title()
        salary = int(input("Введіть заробітню плату для працівника: "))
        dict_of_employees[add_employee] = salary
    elif choose_Admin == 5:
        remove_employee = input(
            "Введіть посаду працівника для звільнення з роботи: "
        ).title()
        if remove_employee in dict_of_employees:
            dict_of_employees.pop(remove_employee)


Add_and_assign_salary_or_remove_employee()

def Change_salary_of_employee():
    if choose_Admin == 6:
        for employee in dict_of_employees:
            if employee in dict_of_employees:
                position = input("Введіть посаду для зміни заробітньої плати: ").title()
                new_salary = int(input("Введіть нову заробітню плату: "))
                dict_of_employees[position] = new_salary


Change_salary_of_employee()