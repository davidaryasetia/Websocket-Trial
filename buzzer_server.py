import asyncio
import websockets

# empty list to store client 
clients = []

# define a function to handle incoming message from client 
async def handle_message(websocket, path): 
    global clients
    global fastest_time
    message = await websocket.recv()
    if message == "buzz": 
        response_time = asyncio.get_event_loop().time
        clients.append({websocket, response_time})
        if len(clients) == 1: 
            fastest_time = response_time
        else: 
            t = round(response_time - fastest_time, 2)
            await websocket.send(f"Response time : {t} sec slower.")

# start websocket server 
async def start_server(): 
    async with websockets.serve(handle_message, "localhost", 8765): 
        print('Websockets Server started')
        await asyncio.Future()

# Run the server
asyncio.run(start_server())