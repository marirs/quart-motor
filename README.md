Quart-Motor
=============
[![Build Status](https://travis-ci.org/marirs/quart-motor.svg?branch=master)](https://travis-ci.org/marirs/quart-motor)
[![codecov](https://codecov.io/gh/marirs/quart-motor/branch/master/graph/badge.svg)](https://codecov.io/gh/marirs/quart-motor)
[![GitHub license](https://img.shields.io/badge/license-BSD%203-brightgreen)](https://github.com/marirs/quart-motor/blob/master/LICENSE)
![PyPI - Downloads](https://img.shields.io/pypi/dd/Quart-Motor)

`MongoDB <http://www.mongodb.org/>` is an open source database that stores
flexible JSON-like "documents," which can have any number, name, or
hierarchy of fields within, instead of rows of data as in a relational
database. Python developers can think of MongoDB as a persistent, searchable
repository of Python dictionaries (and, in fact, this is how `PyMongo
<http://api.mongodb.org/python/current/>` represents MongoDB documents).

Quart-Motor bridges Quart and Motor and provides some convenience
helpers.


Quickstart
----------

First, install Quart-Motor:

```bash
$ pip install Quart-Motor
```

Next, add a :class:`~quart_motor.Motor` to your code:

```python
    from quart import Quart
    from quart_motor import Motor

    app = Quart(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    mongo = Motor(app)
```
:class:`~quart_motor.Motor` connects to the MongoDB server running on
port 27017 on localhost, to the database named ``myDatabase``. This database
is exposed as the :attr:`~quart_motor.Motor.db` attribute.

You can use :attr:`~quart_motor.Motor.db` directly in views:

```python

    @app.route("/")
    def home_page():
        online_users = mongo.db.users.find({"online": True})
        return render_template("index.html",
            online_users=online_users)
```

Compatibility
-------------

Quart-Motor depends on recent versions of Quart, Motor and PyMongo, where "recent"
is defined to mean "was released in the last 3 years". Quart-Motor *may*
work with older versions, but compatibility fixes for older versions will
not be accepted, and future changes may break compatibility in older
versions.

Quart-Motor is tested against `supported versions
<https://www.mongodb.com/support-policy>`_ of MongoDB, 3.5+.

Quart-Motor works very well with
- `uvicorn` asgi
- `hypercorn` asgi

Quart-Motor is tested against `Python 3.7+` versions.

Helpers
-------

Quart-Motor provides helpers for some common tasks:

.. automethod:: quart_motor.wrappers.Collection.find_one_or_404

.. automethod:: quart_motor.Motor.send_file

.. automethod:: quart_motor.Motor.save_file

.. autoclass:: quart_motor.helpers.BSONObjectIdConverter

.. autoclass:: quart_motor.helpers.JSONEncoder

Configuration
-------------

You can configure Quart-Motor either by passing a `MongoDB URI
<https://docs.mongodb.com/manual/reference/connection-string/>`_ to the
:class:`~quart_motor.Motor` constructor, or assigning it to the
``MONGO_URI`` `Quart configuration variable
<https://pgjones.gitlab.io/quart/how_to_guides/configuration.html>`_

The :class:`~quart_motor.Motor` instnace also accepts these additional
customization options:

* ``json_options``, a :class:`~bson.json_util.JSONOptions` instance which
  controls the JSON serialization of MongoDB objects when used with
  :func:`~quart.json.jsonify`.

You may also pass additional keyword arguments to the ``Motor``
constructor. These are passed directly through to the underlying
:class:`~motor.motor_asyncio.AsyncIOMotorClient` object.

Note:

    By default, Quart-Motor sets the ``connect`` keyword argument to
    ``False``, to prevent Motor from connecting immediately. Motor
    itself `is not fork-safe
    <https://pymongo.readthedocs.io/en/stable/faq.html#is-pymongo-fork-safe>`_,
    and delaying connection until the app is actually used is necessary to
    avoid issues. If you wish to change this default behavior, pass
    ``connect=True`` as a keyword argument to ``Motor``.

You can create multiple ``Motor`` instances, to connect to multiple
databases or database servers:

```python

    app = Quart(__name__)

    # connect to MongoDB with the defaults
    mongo1 = Motor(app, uri="mongodb://localhost:27017/databaseOne")

    # connect to another MongoDB database on the same host
    mongo2 = Motor(app, uri="mongodb://localhost:27017/databaseTwo")

    # connect to another MongoDB server altogether
    mongo3 = Motor(app, uri="mongodb://another.host:27017/databaseThree")
```
Each instance is independent of the others and shares no state.


API
===

Classes
-------

.. autoclass:: quart_motor.Motor
   :members:

   .. attribute:: cx

      The :class:`~quart_motor.wrappers.AsyncIOMotorClient` connected to the
      MongoDB server.

   .. attribute:: db

      The :class:`~quart_motor.wrappers.AsyncIOMotorDatabase` if the URI used
      named a database, and ``None`` otherwise.


Wrappers
--------

Quart-Motor wraps Motor's :class:`~motor.motor_asyncio.AsyncIOMotorClient`,
:class:`~motor.motor_asyncio.AsyncIOMotorDatabase`, and
:class:`~motor.motor_asyncio.AsyncIOMotorCollection` classes, and overrides their
attribute and item accessors. Wrapping the Motor classes in this way lets
Quart-Motor add methods to ``AsyncIOMotorCollection`` while allowing user code to use
MongoDB-style dotted expressions.

```python

    >>> type(mongo.cx)
    <type 'quart_motor.wrappers.AsyncIOMotorClient'>
    >>> type(mongo.db)
    <type 'quart_motor.wrappers.AsyncIOMotorDatabase'>
    >>> type(mongo.db.some_collection)
    <type 'quart_motor.wrappers.AsyncIOMotorCollection'>
```
.. autoclass:: quart_motor.wrappers.AsyncIOMotorCollection(...)
   :members:


History and Contributors
------------------------

Changes:

- 2.4.0: Unreleased

  - Flask-PyMongo port as released of Flask-PyMongo.

Flask-PyMongo:

- <https://github.com/dcrosta/flask-pymongo>


Contributors of Flask-PyMongo:

- `jeverling <https://github.com/jeverling>`
- `tang0th <https://github.com/tang0th>`
- `Fabrice Aneche <https://github.com/akhenakh>`
- `Thor Adam <https://github.com/thoradam>`
- `Christoph Herr <https://github.com/jarus>`
- `Mark Unsworth <https://github.com/markunsworth>`
- `Kevin Funk <https://github.com/k-funk>`
- `Ben Jeffrey <https://github.com/jeffbr13>`
- `Emmanuel Valette <https://github.com/karec>`
- `David Awad <https://github.com/DavidAwad>`
- `Robson Roberto Souza Peixoto <https://github.com/robsonpeixoto>`
- `juliascript <https://github.com/juliascript>`
- `Henrik Blidh <https://github.com/hbldh>`
- `jobou <https://github.com/jbouzekri>`
- `Craig Davis <https://github.com/blade2005>`
- `ratson <https://github.com/ratson>`
- `Abraham Toriz Cruz <https://github.com/categulario>`
- `MinJae Kwon <https://github.com/mingrammer>`
- `yarobob <https://github.com/yarobob>`
- `Andrew C. Hawkins <https://github.com/achawkins>`

Contributors of Quart-Motor

- `Sriram <https://github.com/marirs>`
- `Kiran <https://github.com/kirantambe>`
