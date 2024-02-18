from admin import (function_of_admin, add_drink,
                   remove_drink, change_price_drink, add_employee,
                   remove_employee, change_salary_of_employee, show_employees,
                   show_drinks, order_drink, back)
option = int(input("Вибери спеціальність: \n" "1. Адмін\n"))

boolean = True
while boolean:
    admin_function = function_of_admin()
    if option == 1:
        if admin_function == 1:
            add_drink()
        elif admin_function == 2:
            remove_drink()
        elif admin_function == 3:
            change_price_drink()
        elif admin_function == 4:
            add_employee()
        elif admin_function == 5:
            remove_employee()
        elif admin_function == 6:
            change_salary_of_employee()
        elif admin_function == 7:
            show_employees()
        elif admin_function == 8:
            show_drinks()
        elif admin_function == 10:
            order_drink()
        elif admin_function == 11:
            back()
        elif admin_function == 12:
            boolean = False

