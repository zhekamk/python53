# Завдання 1
# Напиши функцію async_counter(n), яка виводить числа від 1 до n з паузою в 1 секунду між виведенням.
# Використай asyncio.sleep() для затримки.
import asyncio

async def async_counter(n):
    for i in range(1, n + 1):
        print(i, end=' ')
        await asyncio.sleep(1)

asyncio.run(async_counter(10))
print('\n'+'*'*100)


# Завдання 2
# Напиши програму, яка запускає одночасно три асинхронні функції:
# download_file_1() чекає 3 секунди і друкує "File 1 downloaded"
# download_file_2() чекає 2 секунди і друкує "File 2 downloaded"
# download_file_3() чекає 1 секунду і друкує "File 3 downloaded"
# Запусти всі три функції одночасно за допомогою asyncio.gather()
async def download_file_1():
    await asyncio.sleep(3)
    print("File 1 downloaded")

async def download_file_2():
    await asyncio.sleep(2)
    print("File 2 downloaded")

async def download_file_3():
    await asyncio.sleep(1)
    print("File 3 downloaded")

async def main():
    await asyncio.gather(
        download_file_1(),
        download_file_2(),
        download_file_3()
    )

asyncio.run(main())
print('*'*100)
# Завдання 3
# Напиши функцію async_write_file(filename, text), яка асинхронно записує переданий текст у файл.
# Напиши функцію async_read_file(filename), яка асинхронно читає файл і виводить його вміст.
# Використай asyncio.gather(), щоб записати 3 різних файли одночасно, а потім їх прочитати.
# Треба використовувати aiofiles для роботи з файлами без блокування головного потоку.
import aiofiles

async def async_write_file(filename, text):
    async with aiofiles.open(filename, mode='w', encoding='utf-8') as f:
        await f.write(text)
    print(f"Записано у {filename}")

async def async_read_file(filename):
    async with aiofiles.open(filename, mode='r', encoding='utf-8') as f:
        content = await f.read()
    print(f"Зміст {filename}: {content}")

async def main():
    await asyncio.gather(
        async_write_file("f1.txt", "Привіт з файлу 1"),
        async_write_file("f2.txt", "Текст для файлу 2"),
        async_write_file("f3.txt", "Асинхронний запис 3")
    )
    await asyncio.gather(
        async_read_file("f1.txt"),
        async_read_file("f2.txt"),
        async_read_file("f3.txt")
    )

asyncio.run(main())