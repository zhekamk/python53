# Завдання 1
# Створіть наступні запити для таблиці з оцінками студентів із попереднього завдання:
#
# Відображати всієї інформації з таблиці зі студентами та оцінками.
# Відображати ПІБ усіх студентів.
# Відображати усіх середніх оцінок.
# Показати ПІБ усіх студентів з мінімальною оцінкою, більшою, ніж зазначена.
# Показати країни студентів. Назви країн мають бути унікальними.
# Показати міста студентів. Назви міст мають бути унікальними.
# Показати назви груп. Назви груп мають бути унікальними.
# Показати назви усіх предметів із мінімальними середніми оцінками. Назви пред­метів мають бути унікальними.
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

    cursor.execute("SELECT * FROM StudentGrades")
    for row in cursor.fetchall(): print(row)

    cursor.execute("SELECT full_name FROM StudentGrades")
    for row in cursor.fetchall(): print(row[0])

    cursor.execute("SELECT avg_year_grade FROM StudentGrades")
    for row in cursor.fetchall(): print(row[0])

    cursor.execute("SELECT full_name FROM StudentGrades WHERE avg_year_grade")
    for row in cursor.fetchall(): print(row[0])

    cursor.execute("SELECT DISTINCT country FROM StudentGrades")
    for row in cursor.fetchall(): print(row[0])

    cursor.execute("SELECT DISTINCT city FROM StudentGrades")
    for row in cursor.fetchall(): print(row[0])

    cursor.execute("SELECT DISTINCT group_name FROM StudentGrades")
    for row in cursor.fetchall(): print(row[0])

    cursor.execute("SELECT DISTINCT min_subject_name FROM StudentGrades")
    for row in cursor.fetchall(): print(row[0])
    connection.close()

if __name__ == '__main__':
    main()

# Показати ПІБ усіх студентів з мінімальною оцінкою у вказаному діапазоні.
# Показати інформацію про студентів, яким виповнилося 20 років.
# Показати інформацію про студентів з віком, у вказаному діапазоні.
# Показати інформацію про студентів із конкретним ім'ям. Наприклад, показати студентів з ім'ям Борис.
# Показати інформацію про студентів, в номері яких є три сімки.
# Показати електронні адреси студентів, що починаються з конкретної літери.3

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

    min_val, max_val = 10.0, 12.0
    cursor.execute("SELECT full_name FROM StudentGrades WHERE avg_year_grade BETWEEN ? AND ?", (min_val, max_val))
    for row in cursor.fetchall(): print(row)

    cursor.execute("SELECT * FROM StudentGrades WHERE (strftime('%Y', 'now') - strftime('%Y', birth_date)) = 20")
    for row in cursor.fetchall(): print(row)


    age_start, age_end = 18, 21
    cursor.execute("""
        SELECT * FROM StudentGrades 
        WHERE (strftime('%Y', 'now') - strftime('%Y', birth_date)) BETWEEN ? AND ?
    """, (age_start, age_end))
    for row in cursor.fetchall(): print(row)


    name_to_search = "Іван"
    cursor.execute("SELECT * FROM StudentGrades WHERE full_name LIKE ?", (f'%{name_to_search}%',))
    for row in cursor.fetchall(): print(row)


    cursor.execute("SELECT * FROM StudentGrades WHERE phone LIKE '%777%'")
    for row in cursor.fetchall(): print(row)


    start_letter = 'i'
    cursor.execute("SELECT email FROM StudentGrades WHERE email LIKE ?", (f'{start_letter}%',))
    for row in cursor.fetchall(): print(row)
    connection.close()

if __name__ == '__main__':
    main()