# --------------------------------------------------
# Async Demo
#
# Java Equivalent:
# CompletableFuture
# --------------------------------------------------

import asyncio


async def make_tea():

    print("Boiling water...")

    # Wait 3 seconds
    # Java equivalent:
    # Thread.sleep(3000)
    #
    # BUT non-blocking
    await asyncio.sleep(3)

    print("Tea Ready")


async def main():

    print("Starting")

    await make_tea()

    print("Finished")


asyncio.run(main())