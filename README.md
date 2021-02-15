# Live Stream VOD Indexer

- [WIP] JSON API for indexing livestreams.
- Will complete the README.md in the coming patches

## Endpoints

```plaintext
stream/date/<int:year>/<int:month>/<int:day>/     #streams-by-date
stream/game/<slug:slug>/                          #streams-by-game-slug
stream/id/<int:id>/                               #streams-by-stream-id (DjangoModel)

info/slugs/                                       # Returns all game slugs available
info/last-updated/                                # Returns last change date
info/streamer/                                    # Returns Info About Streamer
info/endpoints/                                   # Returns all endpoints available now
info/version/                                     # Returns the version of current server

help/                                             # Link to HELP Documentation
<path:path>/                                      # Wildcard for all unassigned paths
```

## Installation

1. `python -m pip install -r requirements.txt`
2. `python manage.py makemigrations \\ Incase the migrations are behind for some reason.`
3. `python manage.py migrate`

- To run the server, run `python manage.py runserver`
- If desired, place custom static files in the ./static/ folder

## Changelog

- ### v0.0.6

  - ./static/ contains global css, javascript
  - ./staticfiles/ is automatically populated by Django COLLECTSTATIC Command

- ### v0.0.5

  - Added Endpoint Information to README.md

- ### v0.0.4

  - Modified GameStorage to add Game Website Links
  - Modified GameStorage.game_slug to use models.SlugField
  - Modified StreamStorage to add VOD Link, VOD Status
  - Added StreamViews for
    - by-date
    - by-slug
    - by-id
  - Added ModelAdmin to GameStorage
    - Autofills game_slug according to GameStorage.game_name
  - Modified URLResolverPaths
    - Corrected stream/yyyy/mm/dd/ to stream/date/yyyy/mm/dd/

- ### v0.0.3 - README.md

  - Added installation instructions to README.md

- ### v0.0.2 - Base Server

  - Added Database Migrations for app.
  - Corrected DEBUG vs not DEBUG logic in server/settings.py
  - Corrected formatting and spelling in README.md

- ### v0.0.1 - Initial Patch

  - Added Initial Files
  - Setup Django Mapping
