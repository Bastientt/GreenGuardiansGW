import asyncio
import socket
from AI.AI import *


async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Handling client {addr}")

    try:
        with open('./GreenGuardiansGW/Pictures/lastImage.jpg', 'wb') as f:
            print("Receiving image...")
            while True:
                data = await reader.read(1024)
                if not data:
                    break
                print(f"Received {len(data)} bytes")
                f.write(data)
        print("New image received")

        # AI part
        resultAI = startSearch("./GreenGuardiansGW/Pictures/lastImage.jpg")
        print(f"AI result: {resultAI}")
        writer.write(f"result: {resultAI}".encode('utf-8'))
        await writer.drain()
    
    except Exception as e:
        print(f"Error handling connection {addr}: {e}")
    
    finally:
        writer.close()
        await writer.wait_closed()
        print(f"Connection closed from {addr}")

async def start_server(host='192.168.43.201', port=2000):
    server = await asyncio.start_server(handle_client, host, port)
    addr = server.sockets[0].getsockname()
    print(f"Server listening on {addr}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(start_server())
