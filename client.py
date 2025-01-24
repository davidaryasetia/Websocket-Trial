import asyncio
import websockets

# create an empty list to store clients
clients = []

# define a function to handle incoming messages from clients
async def handle_message(websocket, path):  # Pastikan 'path' ada sebagai parameter
    global clients
    global fastest_time

    try:
        # Receive message from client
        message = await websocket.recv()
        if message == "buzz":
            response_time = asyncio.get_event_loop().time()
            clients.append([websocket, response_time])
            if len(clients) == 1:
                await websocket.send("First place!")
                fastest_time = response_time
            else:
                t = round(response_time - fastest_time, 2)
                await websocket.send(f"Response time: {t} sec slower.")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

# start the websocket server
async def start_server():
    async with websockets.serve(handle_message, "localhost", 8765):
        print('Websockets Server Started')
        await asyncio.Future()  # Keep server running forever

# run the server
asyncio.run(start_server())
