# # """Дополнить телефонный справочник возможностью изменения и удаления данных.
# # Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# # для изменения и удаления данных."""

filename = 'phonebook.txt'

def work_with_phone_book():
    choice = show_menu()
    phone_book = read_txt(filename)  
    while choice !=7: 
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = str(input('Введите Фамилию: '))
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            phone_number = input('Введите номер телефона: ').strip()
            if phone_number.isdigit():
                print(find_by_phone_number(phone_book, phone_number))  
        elif choice == 4:
            user_data = input('Введите данные (Фамилия, Имя, Телефон, Описание) через запятую: ')
            add_user(filename, user_data)
            phone_book = read_txt(filename)
            print("Данные добавлены.")
        elif choice == 5:
            last_name = input('Введите фамилию для удаления: ').strip()
            delete_by_lastname(filename, last_name)
        elif choice == 6:
            print("Выход из программы.")
            break
        input('Press Enter to contunue..')
    
        choice = show_menu()

def show_menu():
    print("Выберите необходимое ")
    print("1. Отобразить весь справочник")
    print("2. Найти абонента по фамилии")
    print("3. Найти абонента по номеру телефона")
    print("4. Добавить абонента в справочник")
    print("5. Удалить абонента в справочнике") 
    print("6. Закончить работу")   
    choice = int(input("Введите номер от 1 до 6: "))
    if 1 <= choice <= 7:
        return choice
    else:
        choice = 0
    return choice
    
import re
def write_txt(filename, phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

def read_txt(filename):
    phone_book = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    pattern = re.compile(r'Фамилия:(.*?),s*Имя:(.*?),s*Телефон:(.*?),s*Описание:(.*)')
    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            print(f"Обрабатывается строка: '{line.strip()}'")  # Для отладки
            match = pattern.match(line.strip())
            if match:
                record = dict(zip(fields, match.groups()))
                phone_book.append(record)
            else:
                print("Строка не соответствует шаблону")  # Для отладки
    return phone_book

"1. Отобразить весь справочник"
def print_result(phone_book):
    if not phone_book:
        print("Справочник пуст")
    else:
        for record in phone_book:
            print(f"Фамилия:{record['Фамилия']}, Имя:{record['Имя']}, Телефон:{record['Телефон']}, Описание:{record['Описание']}")

            
"2. Найти абонента по фамилии"          
def find_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record["Фамилия"] == last_name:
            return record
    return 'Абонент не найден'

"3. Найти абонента по номеру телефона"
def find_by_phone_number(phone_book, phone_number):
    result = [record for record in phone_book if record.get('Телефон') == phone_number]
    if result:
        for record in result:
            print(f"Фамилия' {record['Фамилия']}, 'Имя' {record['Имя']}, 'Телефон' {record['Телефон']}, 'Описание' {record['Описание']}")
    else:
        return 'Абонент не найден'
    
"4. Добавить абонента в справочник"
def add_user(filename, user_data):
    parts = user_data.split(',')
    if len(parts) < 4:
        print("Ошибка: необходимо ввести Фамилию, Имя, Телефон и Описание, разделенные запятой.")
        return
    new_contact = f"Фамилия:{parts[0].strip()},Имя:{parts[1].strip()},Телефон:{parts[2].strip()},Описание:{parts[3].strip()}n"
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(new_contact)

"5. Удалить абонента в справочнике"
def delete_by_lastname(filename, last_name):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if last_name not in line]

    if len(lines) == len(filtered_lines):
        print(f"Фамилии {last_name} не найдено.")
    else:
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(filtered_lines)
        print(f"Абонент с фамилией {last_name} удален.")

work_with_phone_book()