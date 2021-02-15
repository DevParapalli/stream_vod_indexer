# Live Stream VOD Indexer

- [WIP] JSON API for indexing livestreams.
- Will complete the README.md in the coming patches

## Installation

1. `python -m pip install -r requirements.txt`
2. `python manage.py makemigrations \\ Incase the migrations are behind for some reason.`
3. `python manage.py migrate`

- To run the server, run `python manage.py runserver`

## Changelog

- ### v0.0.3 - README.md

  - Added installation instructions to README.md

- ### v0.0.2 - Base Server

  - Added Database Migrations for app.
  - Corrected DEBUG vs not DEBUG logic in server/settings.py
  - Corrected formatting and spelling in README.md

- ### v0.0.1 - Initial Patch

  - Added Initial Files
  - Setup Django Mapping
