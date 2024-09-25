"""
Write a Python program that creates an asynchronous function to print "Python Exercises!" with a two second delay.
"""
import asyncio


async def printDelay():
    await asyncio.sleep(2)
    print("Python Exercises!")


asyncio.run(printDelay())