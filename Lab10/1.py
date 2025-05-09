import psycopg2
import csv

# Подключение к базе данных
def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",  
        user="postgres",           
        password="Dakota3012"        
    )

# Создание таблицы
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            phone_number VARCHAR(15) NOT NULL
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

# Ввод пользователя с консоли
def insert_user_console():
    first_name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (first_name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Контакт добавлен!")

# Загрузка данных из CSV
def insert_from_csv():
    filename = input("Введите имя CSV файла: ")
    conn = connect()
    cur = conn.cursor()

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропустить заголовок
        for row in reader:
            if len(row) >= 2:
                cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (row[0], row[1]))

    conn.commit()
    cur.close()
    conn.close()
    print("Данные из CSV загружены!")

# Обновление пользователя
def update_user():
    old_name = input("Введите текущее имя: ")
    new_name = input("Новое имя (оставьте пустым если не менять): ")
    new_phone = input("Новый номер телефона (оставьте пустым если не менять): ")

    conn = connect()
    cur = conn.cursor()
    if new_name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone_number = %s WHERE first_name = %s", (new_phone, old_name))
    conn.commit()
    cur.close()
    conn.close()
    print("Контакт обновлён!")

# Поиск по фильтру
def query_users():
    print("Фильтр: 1 - все, 2 - по имени, 3 - по номеру")
    choice = input("Ваш выбор: ")

    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        cur.execute("SELECT * FROM phonebook")
    elif choice == "2":
        name = input("Введите имя: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
    elif choice == "3":
        phone = input("Введите номер: ")
        cur.execute("SELECT * FROM phonebook WHERE phone_number = %s", (phone,))
    else:
        print("Неверный выбор.")
        return

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

# Удаление
def delete_user():
    print("Удалить по: 1 - имени, 2 - номеру")
    choice = input("Ваш выбор: ")

    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        name = input("Введите имя: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    elif choice == "2":
        phone = input("Введите номер: ")
        cur.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone,))
    else:
        print("Неверный выбор.")
        return

    conn.commit()
    cur.close()
    conn.close()
    print("Контакт удалён!")

# Меню
def main():
    create_table()
    while True:
        print("\n--- Телефонная книга ---")
        print("1. Добавить контакт с консоли")
        print("2. Загрузить контакты из CSV")
        print("3. Обновить контакт")
        print("4. Найти контакт")
        print("5. Удалить контакт")
        print("0. Выход")

        choice = input("Выберите опцию: ")

        if choice == "1":
            insert_user_console()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_user()
        elif choice == "4":
            query_users()
        elif choice == "5":
            delete_user()
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверная опция!")

if __name__ == "__main__":
    main()
