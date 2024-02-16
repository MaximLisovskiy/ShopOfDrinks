from admin import choose_the_option, function_of_admin, add_drink, remove_drink, change_price_drink
from admin import add_employee, remove_employee

boolean = True
while boolean:
    if choose_the_option == 1:
        if function_of_admin() == 1:
            add_drink()
        elif function_of_admin() == 2:
            remove_drink()
        elif function_of_admin() == 3:
            change_price_drink()
        elif function_of_admin() == 4:
            add_employee()
        elif function_of_admin() == 5:
            remove_employee()


