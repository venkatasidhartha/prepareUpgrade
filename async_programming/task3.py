"""
Write a Python program that creates an asyncio event loop and runs a coroutine that prints 
numbers from 1 to 7 with a delay of 1 second each.
"""
import asyncio
async def display_numbers():
    for i in range(1, 8):
        print(i)
        await asyncio.sleep(1)
# Run the coroutine using asyncio.run()
asyncio.run(display_numbers())
