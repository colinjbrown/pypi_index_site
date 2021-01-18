# pypi_index_site

This repository contains a front-facing page for a Pypi Reverse Index website. This particular page relies on the existance of the PyPI reverse index database.

This is a publicly facing database that contains package information about Python package modules and submodules mapped directly to packages including all versions of packages where this is true.

To reach the database without accessing this site directly the database can be reached with this public information.

`23.234.231.89`
with the following credentials
Username: `public1`
Password: `public1`

## Requirements:

`flask`
`pymongo`
`wtforms`

## Usage:
To run locally use:

`FLASK_APP=app.py flask run`

To expose ports to act as a mirror please run

`FLASK_APP=app.py flask run --host=<ip>`
