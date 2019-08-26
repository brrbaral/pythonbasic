import asyncio
async def Hello():
    print("Hello")
    await asyncio.sleep(2)
    print("World")
asyncio.run(Hello())
