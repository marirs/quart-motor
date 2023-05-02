import pytest
from quart import Quart
from werkzeug.exceptions import NotFound

from quart_motor import Motor


class TestCollection:
    uri = f"mongodb://localhost:27017/test"

    @pytest.mark.asyncio
    async def test_find_one_or_404_notfound(self):
        app = Quart(__name__)
        mongo = Motor(app=app, uri=self.uri)
        await app.startup()
        await mongo.db.things.delete_many({})
        with pytest.raises(NotFound):
            await mongo.db.things.find_one_or_404({"_id": "thing"})

    @pytest.mark.asyncio
    async def test_find_one_or_404_found(self):
        app = Quart(__name__)
        mongo = Motor(app=app, uri=self.uri)
        await app.startup()
        await mongo.db.things.insert_one({"_id": "thing", "val": "foo"})
        thing = await mongo.db.things.find_one_or_404({"_id": "thing"})
        assert thing["val"] == "foo"
        await mongo.db.things.delete_many({})
