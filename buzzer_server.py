import asyncio 
import websockets

clients = []

# Define function to handle message 
async def handle_message(websocket, path): 
    global clients
    global fastest_time 

    try: 
        print(f"New connection on path : {path}")
        message = await websocket.recv()
        if message == "buzz":
            response_time = asyncio.get_event_loop().time()
            clients.append((websocket, response_time))

            if len(clients) == 1: 
                fastest_time = response_time
                await websocket.send("First place!")
            else: 
                t = round(response_time - fastest_time, 2)
                await websocket.send(f"Response time : {t} sec slower.")

    except websockets.exceptions.ConnectionClosedError as e : 
        print(f"Connection closed error : {e}")
    except websockets.exceptions.ConnectionClosedOK: 
        print("Connection closed gracefully by the client.")
    except Exception as e: 
        print(f"Unexpected error: {e}")
    finally: 
        clients = [client for client in clients if client[0] != websocket]
        print(f"Client removed. Total clients: {len(clients)}")

# start websockt 
async def start_server(): 
    async with websockets.serve(handle_message, "localhost", 8675):
        print('Websockets Server started')
        await asyncio.Future()

asyncio.run(start_server())
