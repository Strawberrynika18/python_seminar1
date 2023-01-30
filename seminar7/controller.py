import add_in_phone_number as aipn
import user_interface as ui
import change_number as cn
import change_sirname as cs
import delete_phone_number as dpn
import view_contact as vc
import export_in_file as eif


def user_choice():

    choice_num = ui.menu()
    if choice_num < 0 or choice_num > 7:
        print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')
        user_choice()
    elif choice_num == 0:
        aipn.create_json()
    elif choice_num == 1:
        ui.add_to_json()
    elif choice_num == 2:
        cn.change_phone_number()
    elif choice_num == 3:
        cs.change_surname()
    elif choice_num == 4:
        dpn.delete_contact()
    elif choice_num == 5:
        vc.view_all_contacts()
    elif choice_num == 6:
        eif.export_txt()
    elif choice_num == 7:
        print('\n<Thank for using\n')
        exit()