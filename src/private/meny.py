from core.format import FORMATS
import models.UserData as UserDataModule

#TODO: Переделать все методы с print -> чтобы вместо вывода возвращали строки

# Метод print_startup выводит на экран меню приложения.
def print_startup():
    print("""
Приложение "Телефонный справочник:"
    
МЕНЮ
1. Вывод данных по пользователям из БД 
2. Преобразование формата хранения данных 
3. Добавление нового пользователя
0. Выйти из приложения
    
Введите пожалуйста номер желаемого действия из меню: 
    """)

# Метод print_shutdown выводит на экран сообщение перед закрытием приложения.
def print_shutdown():
    print("""
Спасибо что воспользовались нашим приложением!
    """)

# Метод print_unhandle_error выводит на экран сообщение об ошибке в приложении.
def print_unhandle_error():
    print("""
Что-то пошло не так с приложением :'(
Пожалуйста перезапустите его
    """)

def print_unknown_command():
    print("Неизвестная команда.")

def print_success_convert_format(output_full_file_name):
    print(f"""
Преобразование формата хранения данных прошло успешно.
Файл был сохранен по адресу:{output_full_file_name}
    """)

def print_select_format_view():
    print(f"""
Приложение "Телефонный справочник:"
    
МЕНЮ
""")
    for format_id in range(len(FORMATS)):
        formatDataDelimeter = FORMATS[format_id]['formatDataDelimeter']
        userDataDelimeter = FORMATS[format_id]['userDataDelimeter']
        userPropertiesDelimeter = FORMATS[format_id]['userPropertiesDelimeter']
        example = FORMATS[format_id]['example']
        print(f'format_id={format_id}) formatDataDelimeter=\'{formatDataDelimeter}\', userDataDelimeter=\'{userDataDelimeter}\', userPropertiesDelimeter=\'{userPropertiesDelimeter}\', example=\'{example}\'')
    print()

def print_pause():
    input("Для продолжения нажмите Enter")

def msg_add_new_user_view():
    user_properties = map(lambda prop: f'[{prop}]', UserDataModule.UserData.__annotations__.keys())
    user_properties_str = ' '.join(user_properties)
    return f"""
Укажите данные пользователя в формате: '{user_properties_str}'

    """

def msg_add_new_user_success(user_data: UserDataModule.UserData):
        return f"""
Пользователь с данными
{UserDataModule.to_str(user_data)}
Успешно добавлен в БД!
    """