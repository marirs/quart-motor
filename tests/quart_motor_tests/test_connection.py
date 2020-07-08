import time

from quart import Quart
from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo.errors import InvalidURI

from quart_motor import Motor
import pytest


class CouldNotConnect(Exception):
    pass


class TestQuartMotor:
    uri = f"mongodb://localhost:27017/test"
    client_uri = f"mongodb://localhost:27017/"

    @pytest.mark.asyncio
    async def test__motor_client_connection(self):
        app = Quart(__name__)
        mongo = Motor(app=app, uri=self.client_uri)
        assert isinstance(mongo, Motor)

    @pytest.mark.asyncio
    async def test_motor_invalid_uri(self):
        app = Quart(__name__)
        with pytest.raises(InvalidURI):
            mongo = Motor(app=app, uri="http://localhost:27017/test")

    @pytest.mark.asyncio
    async def test_motor_database_success(self):
        app = Quart(__name__)
        mongo = Motor(app=app, uri=self.uri)
        await app.startup()
        assert isinstance(mongo.db, AsyncIOMotorDatabase)

    @pytest.mark.asyncio
    async def test_motor_database_failure(self):
        app = Quart(__name__)
        with pytest.raises(ValueError):
            mongo = Motor(app=app)

    @pytest.mark.asyncio
    async def test_multiple_motor_db_connections(self):
        app = Quart(__name__)
        db1 = Motor(app=app, uri=f"{self.client_uri}test1")
        db2 = Motor(app=app, uri=f"{self.client_uri}test2")
        await app.startup()
        assert isinstance(db1.db, AsyncIOMotorDatabase)
        assert isinstance(db2.db, AsyncIOMotorDatabase)

    @pytest.mark.asyncio
    async def test_motor_no_database_name_in_uri(self):
        app = Quart(__name__)
        mongo = Motor(app=app, uri=self.client_uri)
        await app.startup()
        assert mongo.db is None

    @pytest.mark.asyncio
    async def test_motor_custom_document_class(self):
        class CustomDict(dict):
            pass

        app = Quart(__name__)
        mongo = Motor(app=app, uri=self.uri, document_class=CustomDict)
        await app.startup()
        things = await mongo.db.things.find_one()
        assert things is None

        await mongo.db.things.insert_one({"_id": "thing", "val": "foo"})
        things = await mongo.db.things.find_one()
        await mongo.db.things.delete_many({})
        assert type(things) == CustomDict

    @pytest.mark.asyncio
    async def test_motor_doesnt_connect_by_default(self):
        app = Quart(__name__)
        mongo = Motor(app=app, uri=self.uri)
        await app.startup()

        with pytest.raises(CouldNotConnect):
            _wait_until_connected(mongo, timeout=0.2)


def _wait_until_connected(mongo, timeout=1.0):
    start = time.time()
    while time.time() < (start + timeout):
        if mongo.cx.nodes:
            return
        time.sleep(0.05)
    raise CouldNotConnect("could not prove mongodb connected in %r seconds" % timeout)