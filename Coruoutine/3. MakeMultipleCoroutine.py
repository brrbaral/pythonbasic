#THIS IS ONLY A SYNTAX TO CREATE MULTIPLE COROUTINE
import asyncio
async def Hello():
    await asyncio.gather(
        coro1(),
        coro2(),
        coron()
    )
asyncio.run(Hello())
