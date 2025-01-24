import asyncio
import websockets
import keyboard

async def start_client(): 
    try: 
        async with websockets.connect("ws://localhost:8675/") as websocket: 
            print("Connected to server")
            done = False
            while not done: 
                if keyboard.is_pressed("space"):
                    await websocket.send("buzz")
                    print("Buzz sent")
                    message = await websocket.recv()
                    print(f"Received: {message}")
                    done = True
    except websockets.exceptions.ConnectionClosedError as e: 
        print(f"Connection closed: {e}")
    except Exception as e: 
        print(f"Error {e}")

asyncio.run(start_client())