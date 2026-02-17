# Завдання 1
#
# Створіть базу для зберігання оцінок студентів. Всередині бази даних створіть таблицю "Оцінки студентів". Потрібно зберігати таку інформацію:
#
# ■ ПІБ студента;
# ■ Місто;
# ■ Країна;
# ■ Дата народження;
# ■ Електронна адреса;
# ■ Контактний телефон;
# ■ Назва групи;
# ■ Середня оцінка за рік з усіх предметів;
# ■ Назва предмета з мінімальною, середньою оцінкою;
# ■ Назва предмета з максимальною, середньою оцінкою.
import sqlite3

def main():
    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS StudentGrades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        city TEXT,
        country TEXT,
        birth_date DATE,
        email TEXT,
        phone TEXT,
        group_name TEXT,
        avg_year_grade REAL,
        min_subject_name TEXT,
        max_subject_name TEXT
    )
    ''')

    students_data = [
        ('Іваненко Іван Іванович', 'Київ', 'Україна', '2005-05-15', 'ivan@email.com', '+380501112233', 'ПЗ-21', 11.5, 'Фізика', 'Математика'),
        ('Петренко Марія Олександрівна', 'Львів', 'Україна', '2004-10-20', 'maria@email.com', '+380674445566', 'ПЗ-21', 10.2, 'Хімія', 'Англійська мова')
    ]

    cursor.executemany('''
    INSERT INTO StudentGrades (full_name, city, country, birth_date, email, phone, group_name, avg_year_grade, min_subject_name, max_subject_name)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', students_data)

    connection.commit()

    cursor.execute("SELECT * FROM StudentGrades")
    rows = cursor.fetchall()

    print(f"{'ID':<3} | {'ПІБ':<25} | {'Група':<7} | {'Середня':<8}")
    print("-" * 50)
    for row in rows:
        print(f"{row[0]:<3} | {row[1]:<25} | {row[7]:<7} | {row[8]:<8}")

    connection.close()

if __name__ == '__main__':
    main()

# Завдання 2
# Створіть базу даних Лікарня (Hospital), яка міститиме інформацію про обстеження, які проводяться в лікарні.
#
# Обстеження, які проводяться в лікарні, представлені у вигляді таблиці Обстеження (Examinations), в якій зібрано основну інформацію: назва обстеження, день тижня, коли проводиться обстеження, а також час початку та завершення.
#
# Також у базі даних є інформація про персонал лікарні, яка зберігається в таблиці Лікарі (Doctors). Дані про відділення та захворювання містяться в таблицях Відділення (Departments) та Захворювання (Diseases) відповідно. Опис палат зберігається в таблиці Палати (Wards).
#
# Таблиці
# Нижче наведено детальний опис структури кожної таблиці.
#
# Відділення (Departments)
#
# Ідентифікатор (Id). Унікальний ідентифікатор відділення.
#   Тип даних — int.
#   Автоприріст.
#   Не містить null-значення.
#   Первинний ключ.
# Корпус (Building). Номер корпусу, в якому знаходиться відділення.
#   Тип даних — int.
#   Не містить null-значення.
#   Має бути в діапазоні від 1 до 5.
# Фінансування (Financing). Фонд фінансування відділення.
#   Тип даних для зберігання грошових значень.
#   Не містить null-значення.
#   Не може бути менше, ніж 0.
#   Значення за замовчуванням — 0.
# Назва (Name). Назва відділення.
#   Тип даних — nvarchar(100).
#   Не містить null-значення.
#   Не може бути порожньою.
#   Має бути унікальною.
#
# Захворювання (Diseases)
#
# Ідентифікатор (Id). Унікальний ідентифікатор захворювання.
#   Тип даних — int.
#   Автоприріст.
#   Не містить null-значення.
#   Первинний ключ.
# Назва (Name). Назва захворювання.
#   Тип даних — nvarchar(100).
#   Не містить null-значення.
#   Не може бути порожньою.
#   Має бути унікальною.
#   Ступінь тяжкості (Severity). Ступінь тяжкості захворювання.
#   Тип даних — int.
#   Не містить null-значення.
#   Не може бути менше, ніж 1.
#   Значення за замовчуванням — 1.
#
# Лікарі (Doctors)
#
# Ідентифікатор (Id). Унікальний ідентифікатор лікаря.
#   Тип даних — int.
#   Автоприріст.
#   Не містить null-значення.
#   Первинний ключ.
# Ім'я (Name). Ім'я лікаря.
#   Тип даних — nvarchar(max).
#   Не містить null-значення.
#   Не може бути порожнє.
#   Телефон (Phone). Телефонний номер лікаря.
#   Тип даних — char(10).
#   Може містити null-значення.
# Ставка (Salary). Ставка лікаря.
#   Тип даних для зберігання грошових значень.
#   Не містить null-значення.
#   Не може бути меншою або дорівнювати 0.
# Прізвище (Surname). Прізвище лікаря.
#   Тип даних — nvarchar(max).
#   Не містить null-значення.
#   Не може бути порожнє.
#
# Обстеження (Examinations)
#
# Ідентифікатор (Id). Унікальний ідентифікатор обстеження.
#   Тип даних — int.
#   Автоприріст.
#   Не містить null-значення.
#   Первинний ключ.
# День тижня (DayOfWeek). День тижня, коли проводиться обстеження.
#   Тип даних — int.
#   Не містить null-значення.
#   Має бути в діапазоні від 1 до 7.
#   Час завершення (EndTime). Час завершення обстеження.
#   Тип даних для зберігання часу.
#   Не містить null-значення.
#   Має бути більше, ніж час початку обстеження.
# Назва (Name). Назва обстеження.
#   Тип даних — nvarchar(100).
#   Не містить null-значення.
#   Не може бути порожньою.
#   Має бути унікальною.
#   Час початку (StartTime). Час початку обстеження.
#   Тип даних для зберігання часу.
#   Не містить null-значення.
#   Має бути в діапазоні від 8:00 до 18:00.
#
# Палати (Wards)
#
# Ідентифікатор (Id). Унікальний ідентифікатор.
#  Тип даних — int.
#  Автоприріст.
#  Не містить null-значення.
#  Первинний ключ.
# Корпус (Building). Номер корпусу, де знаходиться палата.
#  Тип даних — int.
#  Не містить null-значення.
#  Має бути в діапазоні від 1 до 5.
# Поверх (Floor). Номер поверху, на якому знаходиться палата.
#  Тип даних — int.
#  Не містить null-значення.
#  Не може бути менше, ніж 1.
# Назва (Name). Назва палати.
#  Тип даних — nvarchar(20).
#  Не містить null-значення.
#  Не може бути порожньою.
#  Має бути унікальною.


def main():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    # 1. Відділення (Departments)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Building INTEGER NOT NULL CHECK (Building BETWEEN 1 AND 5),
        Financing DECIMAL(15, 2) NOT NULL DEFAULT 0 CHECK (Financing >= 0),
        Name NVARCHAR(100) NOT NULL UNIQUE CHECK (Name <> '')
    );
    ''')

    # 2. Захворювання (Diseases)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Diseases (
        Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Name NVARCHAR(100) NOT NULL UNIQUE CHECK (Name <> ''),
        Severity INTEGER NOT NULL DEFAULT 1 CHECK (Severity >= 1)
    );
    ''')

    # 3. Лікарі (Doctors)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Doctors (
        Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Name TEXT NOT NULL CHECK (Name <> ''),
        Phone CHAR(10),
        Salary DECIMAL(15, 2) NOT NULL CHECK (Salary > 0),
        Surname TEXT NOT NULL CHECK (Surname <> '')
    );
    ''')

    # 4. Обстеження (Examinations)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Examinations (
        Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        DayOfWeek INTEGER NOT NULL CHECK (DayOfWeek BETWEEN 1 AND 7),
        StartTime TIME NOT NULL CHECK (StartTime BETWEEN '08:00:00' AND '18:00:00'),
        EndTime TIME NOT NULL CHECK (EndTime > StartTime),
        Name NVARCHAR(100) NOT NULL UNIQUE CHECK (Name <> '')
    );
    ''')

    # 5. Палати (Wards)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Wards (
        Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Building INTEGER NOT NULL CHECK (Building BETWEEN 1 AND 5),
        Floor INTEGER NOT NULL CHECK (Floor >= 1),
        Name NVARCHAR(20) NOT NULL UNIQUE CHECK (Name <> '')
    );
    ''')
    try:
        cursor.execute("INSERT INTO Departments (Building, Financing, Name) VALUES (2, 150000.00, 'Терапія')")
        cursor.execute(
            "INSERT INTO Doctors (Name, Surname, Salary, Phone) VALUES ('Олег', 'Петренко', 25000, '0671112233')")
        cursor.execute(
            "INSERT INTO Examinations (DayOfWeek, StartTime, EndTime, Name) VALUES (1, '09:00', '10:30', 'УЗД')")
        conn.commit()
        print("Дані успішно додано!")
    except sqlite3.IntegrityError as e:
        print(f"Помилка валідації: {e}")


    try:
        cursor.execute("INSERT INTO Departments (Building, Name) VALUES (6, 'Хірургія')")
    except sqlite3.IntegrityError as e:
        print(f"Заблоковано базою: {e}")

    
    cursor.execute("SELECT * FROM Departments")
    for row in cursor.fetchall():
        print(row)
    cursor.execute("SELECT * FROM Doctors")
    for row in cursor.fetchall():
        print(row)
    cursor.execute("SELECT * FROM Examinations")
    for row in cursor.fetchall():
        print(row)
    conn.commit()


if __name__ == '__main__':
    main()