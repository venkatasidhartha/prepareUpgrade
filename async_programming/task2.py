"""
Write a Python program that creates three asynchronous functions and displays their 
respective names with different delays (1 second, 2 seconds, and 3 seconds).
"""
import asyncio

async def name1():
    await asyncio.sleep(1)
    print("name1")

async def name2():
    await asyncio.sleep(3)
    print("name2")

async def name3():
    await asyncio.sleep(2)
    print("name3")

async def main():
    await asyncio.gather(name1(),name2(),name3()) 

asyncio.run(main())