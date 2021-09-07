import asyncio
import pyautogui
import time

async def func(i: int):
    while True:
        await asyncio.sleep(0.3)
        print(f"I waited {i} seconds")


def findAnnie():
    base = time.time()
    annie = pyautogui.locateOnScreen("images/annie.png")
    if annie != None:
        print(annie[0],annie[1])

    print('time to execute ' + str(time.time()-base))
    
    
    
async def locate():
    loop = asyncio.get_event_loop()
    
    loop.run_in_executor(None,findAnnie)
    await asyncio.sleep(0.5)
    await locate()



async def main():

    task1 = [asyncio.create_task(func(5 - i)) for i in range(5)]
    task2 =  [asyncio.create_task(locate())]
    tasks = task1+task2
    print(tasks)
    print(type(task1))
    print(type(task2))

    [await task for task in tasks]


    



if __name__ == "__main__":
    asyncio.run(main())