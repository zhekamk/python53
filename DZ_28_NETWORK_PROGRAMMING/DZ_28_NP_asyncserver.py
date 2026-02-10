# Завдання
# Додати нікнейм користувача
# після підключення клієнт надсилає своє імʼя
# Сервер:
# зберігає nickname → writer
# показує повідомлення у форматі [Anna]: Привіт всім
# При підключенні нового користувача: сервер надсилає всім
# Anna joined the chat
# Підказка
# перше повідомлення після connect — це імʼя
# зберігати клієнтів у dict
import asyncio

HOST = "127.0.0.1"
PORT = 8080

clients = {}


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info('peername')

    try:
        data = await reader.read(1024)
        if not data:
            writer.close()
            return

        nickname = data.decode().strip()
        clients[writer] = nickname

        join_message = f"*** {nickname} joined the chat ***\n"
        print(f"{addr} registered as {nickname}")

        for client in clients:
            if client != writer:
                client.write(join_message.encode())
                await client.drain()

        while True:
            data = await reader.read(1024)
            if not data:
                break

            message = data.decode().strip()
            broadcast_msg = f"[{nickname}]: {message}\n"
            print(f"Broadcast from {nickname}: {message}")

            for client in list(clients.keys()):
                if client != writer:
                    try:
                        client.write(broadcast_msg.encode())
                        await client.drain()
                    except ConnectionError:
                        if client in clients:
                            del clients[client]

    except Exception as e:
        print(f"Error with {addr}: {e}")
    finally:
        if writer in clients:
            nickname = clients[writer]
            print(f"{nickname} ({addr}) disconnected")
            del clients[writer]

            leave_msg = f"*** {nickname} left the chat ***\n"
            for client in clients:
                client.write(leave_msg.encode())

        writer.close()
        await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    print(f'Async Chat Server started on {HOST}:{PORT}')
    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer stopped.")