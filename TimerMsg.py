import asyncio 
import keyboard
import RiotEventListener

async def Corout1s(): 
    while True:
        await asyncio.sleep(1)
        RiotEventListener.UpdateAll()
async def Corout10s(): 
    while True:
        await asyncio.sleep(10)
        RiotEventListener.Send_Msg()

#asyncio.run(main())

loop = asyncio.get_event_loop()

try : 
    #loop.run_until_complete(main())
    asyncio.ensure_future(Corout1s())
    #asyncio.ensure_future(Corout10s())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.close()