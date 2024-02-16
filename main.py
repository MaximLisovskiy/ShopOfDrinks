from admin import choose_the_option, function_of_admin, add_or_remove_drink
import admin

boolean = True
while boolean:
    if choose_the_option == 1:
        choose_Admin = function_of_admin()
        if choose_Admin == 1 or choose_Admin == 2:
            add_or_remove_drink()
