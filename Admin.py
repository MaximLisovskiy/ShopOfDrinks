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