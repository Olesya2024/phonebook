import os

filename = 'phonebook.txt'

def work_with_phone_book():
    ensure_file_exists()
    choice = show_menu()
    phone_book = read_txt(filename)  
    while choice != 6: 
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ').strip()
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            phone_number = input('Введите номер телефона: ').strip()
            print(find_by_phone_number(phone_book, phone_number))
        elif choice == 4:
            user_data = input('Введите данные (Фамилия, Имя, Телефон, Описание) через запятую: ').strip()
            add_user(filename, user_data)
            phone_book = read_txt(filename)  # Обновление данных
            print("Данные добавлены.")
        elif choice == 5:
            last_name = input('Введите фамилию для удаления: ').strip()
            delete_by_lastname(filename, last_name)
            phone_book = read_txt(filename)  # Обновление данных
        elif choice == 6:
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

        input('Нажмите Enter, чтобы продолжить...')
        choice = show_menu()

def ensure_file_exists():
    """Создаёт файл, если он не существует."""
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write('')

def show_menu():
    """Выводит меню и запрашивает выбор пользователя."""
    print("\nВыберите необходимое действие:")
    print("1. Отобразить весь справочник")
    print("2. Найти абонента по фамилии")
    print("3. Найти абонента по номеру телефона")
    print("4. Добавить абонента в справочник")
    print("5. Удалить абонента из справочника") 
    print("6. Закончить работу")   
    while True:
        try:
            choice = int(input("Введите номер от 1 до 6: "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Ошибка: введите число от 1 до 6.")
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное число.")

def write_txt(filename, phone_book):
    """Записывает данные телефонной книги в файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        for record in phone_book:
            file.write(f"{','.join(record.values())}\n")

def read_txt(filename):
    """Читает данные из файла телефонной книги."""
    phone_book = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == len(fields):
                phone_book.append(dict(zip(fields, parts)))
            else:
                print(f"Пропущена строка из-за неправильного формата: {line.strip()}")
    return phone_book

def print_result(phone_book):
    """Выводит телефонную книгу."""
    if not phone_book:
        print("Справочник пуст.")
    else:
        for record in phone_book:
            print(', '.join(f"{key}: {value}" for key, value in record.items()))

def find_by_lastname(phone_book, last_name):
    """Ищет абонента по фамилии."""
    results = [record for record in phone_book if record["Фамилия"] == last_name]
    return results if results else "Абонент не найден."

def find_by_phone_number(phone_book, phone_number):
    """Ищет абонента по номеру телефона."""
    results = [record for record in phone_book if record["Телефон"] == phone_number]
    return results if results else "Абонент не найден."

def add_user(filename, user_data):
    """Добавляет абонента в справочник."""
    parts = user_data.split(',')
    if len(parts) != 4:
        print("Ошибка: необходимо ввести Фамилию, Имя, Телефон и Описание через запятую.")
        return
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"{','.join(part.strip() for part in parts)}\n")

def delete_by_lastname(filename, last_name):
    """Удаляет абонента из справочника по фамилии."""
    phone_book = read_txt(filename)
    updated_phone_book = [record for record in phone_book if record["Фамилия"] != last_name]
    if len(phone_book) == len(updated_phone_book):
        print(f"Фамилия '{last_name}' не найдена.")
    else:
        write_txt(filename, updated_phone_book)
        print(f"Абонент с фамилией '{last_name}' удалён.")

work_with_phone_book()
