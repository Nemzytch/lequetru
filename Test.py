#import TimerMsg
import time
import asyncio
import threading


async def main():
    print("0.5")
    await asyncio.sleep(0.5)

asyncio.run(main())


async def Corout1s(): 
    while True:
        await asyncio.sleep(0.5)
        print("0.5+")


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

try : 
    #loop.run_until_complete(main())
    asyncio.ensure_future(Corout1s())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.close()

def begin_load_TimerMsg():
    global TimerMsg_thread
    TimerMsg_thread = threading.Thread(target=load_TimerMsg_thread)
    TimerMsg_thread.start()

def load_TimerMsg_thread():
    global TimerMsg
    print("start importing")
    TimerMsg = __import__('TimerMsg')
    print("done importing")

def wait_TimerMsg():
    print('wait')
    TimerMsg_thread.join()
    print('done')

def do_other_things():
    time.sleep(1)

begin_load_TimerMsg()
do_other_things()
wait_TimerMsg()


