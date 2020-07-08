from quart import Quart
import asyncio

from quart_motor import Motor


async def main():
    app = Quart(__name__)
    db = Motor(app=app, uri="mongodb://localhost:27017/test").db
    print(await db['things'].find_one({"_id": "59674459"}))

if __name__ == "__main__":
    asyncio.run(main())
