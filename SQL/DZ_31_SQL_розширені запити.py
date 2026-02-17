# Завдання 1
# Створіть тритабличну базу даних Sales. У цій базі даних мають бути таблиці: Sales (інформація про конкретні продажі),
# Salesmen (інформація про продавців), Customers (інформація про покупців).
# Напишіть наступні запити
#
# Відображення усіх угод;
# Відображення угод конкретного продавця;
# Відображення максимальної за сумою угоди;
# Відображення мінімальної за сумою угоди;
# Відображення максимальної суми угоди для конкретного продавця;
# Відображення мінімальної за сумою угоди для конкретного продавця;
# Відображення максимальної за сумою угоди для конкретного покупця;
# Відображення мінімальної за сумою угоди для конкретного покупця;
# Відображення продавця з максимальною сумою продажів за всіма угодами;
# Відображення продавця з мінімальною сумою продажів за всіма угодами;
# Відображення покупця з максимальною сумою покупок за всіма угодами;
# Відображення середньої суми покупки для конкретного покупця;
# Відображення середньої суми покупки для конкретного продавця.
import sqlite3

def main():
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Salesmen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount DECIMAL(10, 2) NOT NULL,
        sale_date DATE,
        salesman_id INTEGER,
        customer_id INTEGER,
        FOREIGN KEY (salesman_id) REFERENCES Salesmen(id),
        FOREIGN KEY (customer_id) REFERENCES Customers(id)
    )''')

    salesmen = [('Андрій',), ('Марія',), ('Олег',)]
    cursor.executemany("INSERT INTO Salesmen (name) VALUES (?)", salesmen)

    customers = [('ТОВ "Вектор"',), ('Іван Петренко',), ('Магазин "Світ"',)]
    cursor.executemany("INSERT INTO Customers (name) VALUES (?)", customers)

    sales = [
        (5000.00, '2023-10-01', 1, 1),
        (12000.50, '2023-10-02', 2, 2),
        (300.00, '2023-10-03', 1, 3),
        (8500.00, '2023-10-04', 3, 1),
        (1500.00, '2023-10-05', 2, 1)
    ]
    cursor.executemany("INSERT INTO Sales (amount, sale_date, salesman_id, customer_id) VALUES (?, ?, ?, ?)", sales)

    print("1. Усі угоди:")
    cursor.execute("SELECT * FROM Sales")
    for r in cursor.fetchall(): print(r)

    print("\n2. Угоди продавця з ID 1 (Андрій):")
    cursor.execute("SELECT * FROM Sales WHERE salesman_id = 1")
    for r in cursor.fetchall(): print(r)

    print("\n3. Максимальна за сумою угода:")
    cursor.execute("SELECT * FROM Sales ORDER BY amount DESC LIMIT 1")
    print(cursor.fetchone())

    print("\n4. Мінімальна за сумою угода:")
    cursor.execute("SELECT * FROM Sales ORDER BY amount ASC LIMIT 1")
    print(cursor.fetchone())

    print("\n5. Макс. сума для продавця ID 2 (Марія):")
    cursor.execute("SELECT MAX(amount) FROM Sales WHERE salesman_id = 2")
    print(cursor.fetchone()[0])

    print("\n6. Мін. сума для продавця ID 2:")
    cursor.execute("SELECT MIN(amount) FROM Sales WHERE salesman_id = 2")
    print(cursor.fetchone()[0])

    print("\n7. Макс. сума для покупця ID 1 (Вектор):")
    cursor.execute("SELECT MAX(amount) FROM Sales WHERE customer_id = 1")
    print(cursor.fetchone()[0])

    print("\n8. Мін. сума для покупця ID 1:")
    cursor.execute("SELECT MIN(amount) FROM Sales WHERE customer_id = 1")
    print(cursor.fetchone()[0])

    print("\n9. Продавець з максимальною загальною сумою продажів:")
    cursor.execute('''SELECT Salesmen.name, SUM(Sales.amount) as total 
                      FROM Sales JOIN Salesmen ON Sales.salesman_id = Salesmen.id 
                      GROUP BY Salesmen.id ORDER BY total DESC LIMIT 1''')
    print(cursor.fetchone())

    print("\n10. Продавець з мінімальною загальною сумою продажів:")
    cursor.execute('''SELECT Salesmen.name, SUM(Sales.amount) as total 
                      FROM Sales JOIN Salesmen ON Sales.salesman_id = Salesmen.id 
                      GROUP BY Salesmen.id ORDER BY total ASC LIMIT 1''')
    print(cursor.fetchone())

    print("\n11. Покупець з максимальною сумою покупок:")
    cursor.execute('''SELECT Customers.name, SUM(Sales.amount) as total 
                      FROM Sales JOIN Customers ON Sales.customer_id = Customers.id 
                      GROUP BY Customers.id ORDER BY total DESC LIMIT 1''')
    print(cursor.fetchone())

    print("\n12. Середня сума покупки для покупця ID 1:")
    cursor.execute("SELECT AVG(amount) FROM Sales WHERE customer_id = 1")
    print(cursor.fetchone()[0])

    print("\n13. Середня сума покупки для продавця ID 2:")
    cursor.execute("SELECT AVG(amount) FROM Sales WHERE salesman_id = 2")
    print(cursor.fetchone()[0])

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()