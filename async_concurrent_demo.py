# --------------------------------------------------
# Async Concurrent Demo
#
# Java Equivalent:
# Multiple CompletableFutures running together
# --------------------------------------------------

import asyncio


async def make_tea():

    print("Tea: Boiling water...")

    await asyncio.sleep(3)

    print("Tea: Ready")


async def make_coffee():

    print("Coffee: Heating milk...")

    await asyncio.sleep(2)

    print("Coffee: Ready")


async def main():

    print("Starting both tasks")

    await asyncio.gather(
        make_tea(),
        make_coffee()
    )

    print("All tasks completed")


asyncio.run(main())