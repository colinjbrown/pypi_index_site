# Pypi Reverse Index

This repository contains a front-facing page for a [Pypi Reverse Index website](http://www.pypi-rev-idx.site/). This particular page relies on the existance of the PyPI reverse index database.

This is a publicly facing database that contains package information about Python package modules and submodules mapped directly to packages including all versions of packages where this is true.

This database can be reached without accessing the web copy directly via the following MongoDB database:

IP: `23.234.231.89`

Port: 12438

Username: `public1`

Password: `public1`

Authorization Database: `admin`

#### Pymongo usage example:

`pymongo.MongoClient("mongodb://public1:public1@23.234.231.89:12438/pypi_mod_index",authSource="admin")`

## Requirements:

`flask`

`pymongo`

`wtforms`

## Usage:
To run locally use:

`FLASK_APP=app.py flask run`

To expose ports to act as a mirror please run

`FLASK_APP=app.py flask run --host=<ip>`
