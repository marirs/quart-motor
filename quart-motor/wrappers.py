"""
Wrappers
"""
from quart import abort
from motor import motor_asyncio


class AsyncIOMotorClient(motor_asyncio.AsyncIOMotorClient):

    """Wrapper for :class:`AsyncIOMotorClient.MongoClient`.
    Returns instances of Quart-Motor
    :class:`~quart_motor.wrappers.Database` instead of native motor
    :class:`~AsyncIOMotorDatabase` when accessed with dot notation.
    """

    def __getattr__(self, name):  # noqa: D105
        attr = super(AsyncIOMotorClient, self).__getattr__(name)
        if isinstance(attr, AsyncIOMotorDatabase):
            return AsyncIOMotorDatabase(self, name)
        return attr

    def __getitem__(self, item):  # noqa: D105
        attr = super(AsyncIOMotorClient, self).__getitem__(item)
        if isinstance(attr, AsyncIOMotorDatabase):
            return AsyncIOMotorDatabase(self, item)
        return attr


class AsyncIOMotorDatabase(motor_asyncio.AsyncIOMotorDatabase):

    """Wrapper for :class:`~AsyncIOMotorDatabase`.
    Returns instances of Quart-Motor
    :class:`~quart_motor.wrappers.AsyncIOMotorCollection` instead of native PyMongo
    :class:`~motor.motor_asyncio.AsyncIOMotorCollection` when accessed with dot notation.
    """

    def __getattr__(self, name):  # noqa: D105
        attr = super(AsyncIOMotorDatabase, self).__getattr__(name)
        if isinstance(attr, AsyncIOMotorCollection):
            return AsyncIOMotorCollection(self, name)
        return attr

    def __getitem__(self, item):  # noqa: D105
        item_ = super(AsyncIOMotorDatabase, self).__getitem__(item)
        if isinstance(item_, AsyncIOMotorCollection):
            return AsyncIOMotorCollection(self, item)
        return item_


class AsyncIOMotorCollection(motor_asyncio.AsyncIOMotorCollection):

    """Sub-class of Motor :class:`~AsyncIOMotorCollection` with helpers.
    """

    def __getattr__(self, name):  # noqa: D105
        attr = super(AsyncIOMotorCollection, self).__getattr__(name)
        if isinstance(attr, AsyncIOMotorCollection):
            db = self._Collection__database
            return AsyncIOMotorCollection(db, attr.name)
        return attr

    def __getitem__(self, item):  # noqa: D105
        item_ = super(AsyncIOMotorCollection, self).__getitem__(item)
        if isinstance(item_, AsyncIOMotorCollection):
            db = self._Collection__database
            return AsyncIOMotorCollection(db, item_.name)
        return item_

    def find_one_or_404(self, *args, **kwargs):
        """Find a single document or raise a 404.
        This is like :meth:`~AsyncIOMotorCollection.Collection.find_one`, but
        rather than returning ``None``, cause a 404 Not Found HTTP status
        on the request.
        .. code-block:: python
            @app.route("/user/<username>")
            def user_profile(username):
                user = mongo.db.users.find_one_or_404({"_id": username})
                return render_template("user.html",
                    user=user)
        """
        found = self.find_one(*args, **kwargs)
        if found is None:
            abort(404)
        return found
