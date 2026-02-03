# Завдання 1
# Користувач вводить з клавіатури значення у список. Після чого запускаються два потоки. Перший потік знаходить максимум у списку.
# Другий потік знаходить мінімум у списку. Результати обчислень виведіть на екран.
import threading
import os
import random

class MaxFinder(threading.Thread):
    def __init__(self, numbers, results):
        super().__init__()
        self.numbers = numbers
        self.results = results

    def run(self):
        if self.numbers:
            res = max(self.numbers)
            self.results['max'] = res
            print(f"[Потік Max] знайдено: {res}")


class MinFinder(threading.Thread):
    def __init__(self, numbers, results):
        super().__init__()
        self.numbers = numbers
        self.results = results

    def run(self):
        if self.numbers:
            res = min(self.numbers)
            self.results['min'] = res
            print(f"[Потік Min] знайдено: {res}")


class ListService:
    def __init__(self, numbers):
        self.numbers = numbers
        self.results = {}

    def process_data(self):
        t1 = MaxFinder(self.numbers, self.results)
        t2 = MinFinder(self.numbers, self.results)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return self.results


if __name__ == "__main__":
    user_input = input("Введіть числа через пробіл: ")
    data = [float(x) for x in user_input.split()]
    service = ListService(data)
    final_results = service.process_data()
    print(f"\n разом: {final_results}")
    print('*'*100)

# Завдання 2
# Користувач вводить з клавіатури шлях до файлу, що містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише парні елементи списку. Другий потік створює новий файл, в який запише лише непарні елементи списку.
# Кількість парних і непарних елементів виводиться на екран.
def save_even(numbers):
    even_list = [n for n in numbers if n % 2 == 0]
    with open("even.txt", "w") as f:
        f.write(str(even_list))
    print(f"Кількість парних: {len(even_list)}")

def save_odd(numbers):
    odd_list = [n for n in numbers if n % 2 != 0]
    with open("odd.txt", "w") as f:
        f.write(str(odd_list))
    print(f"Кількість непарних: {len(odd_list)}")

path = input("Введіть шлях до файлу: ")

with open(path, "r") as f:
    data = f.read().split()
    nums = [int(x) for x in data]

thread1 = threading.Thread(target=save_even, args=(nums,))
thread2 = threading.Thread(target=save_odd, args=(nums,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print('*' * 100)
# Завдання 3
# Користувач вводить з клавіатури шлях до файлу та слово для пошуку. Після чого запускається потік для пошуку цього слова у файлі.
# Результат пошуку виведіть на екран.



def search_word_in_file(file_path, search_word):
    try:
        if not os.path.exists(file_path):
            print(f"\nПомилка: Файл за шляхом '{file_path}' не знайдено.")
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        count = content.count(search_word)

        if count > 0:
            print(f"\nРезультат пошуку: Слово '{search_word}' знайдено {count} раз(ів).")
        else:
            print(f"\nРезультат пошуку: Слово '{search_word}' не знайдено.")

    except Exception as e:
        print(f"\nСталася помилка при читанні файлу: {e}")


def main():
    path = input("Введіть шлях до файлу: ")
    word = input("Введіть слово для пошуку: ")
    search_thread = threading.Thread(target=search_word_in_file, args=(path, word))
    print("Потік пошуку запущено...")
    search_thread.start()
    search_thread.join()


if __name__ == "__main__":
    main()

  print('*'*100)

# Завдання 4
# При старті додатку запускаються три потоки. Перший потік заповнює список випадковими числами. Два інші потоки очікують на заповнення.
# Коли перелік заповнений, обидва потоки запускаються. Перший потік знаходить суму елементів списку, другий потік знаходить середнє арифметичне
# значення у списку. Отриманий список, сума та середнє арифметичне виводяться на екран.

def fill():
    global nums
    nums = [random.randint(1, 100) for _ in range(10)]
    print(f"Список: {nums}")

def get_sum():
    print(f"Сума: {sum(nums)}")

def get_avg():
    print(f"Середнє: {sum(nums) / len(nums)}")


t1 = threading.Thread(target=fill)
t2 = threading.Thread(target=get_sum)
t3 = threading.Thread(target=get_avg)
t1.start()
t1.join()
t2.start()
t3.start()