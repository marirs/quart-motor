from quart import Quart
from werkzeug.exceptions import HTTPException

from quart_motor import Motor


class TestCollection:
    uri = f"mongodb://localhost:27017/test"

    async def test_find_one_or_404(self):
        app = Quart(__name__)
        mongo = Motor(app=app, uri=self.uri)
        mongo.db.things.delete_many({})
        try:
            mongo.db.things.find_one_or_404({"_id": "thing"})
        except HTTPException as notfound:
            assert notfound.code == 404, "raised wrong exception"