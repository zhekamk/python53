import asyncio

HOST = "127.0.0.1"
PORT = 8080


async def receive_messages(reader):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        print(f"\n{data.decode().strip()}")
        print("> ", end="", flush=True)


async def main():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    print("--- Підключено до асинхронного сервера ---")

    nickname = input("Введіть ваш нік: ")
    writer.write(nickname.encode())
    await writer.drain()

    asyncio.create_task(receive_messages(reader))

    while True:
        msg = await asyncio.get_event_loop().run_in_executor(None, input, "> ")
        if msg.lower() == '/exit':
            break

        writer.write(msg.encode())
        await writer.drain()

    writer.close()
    await writer.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())