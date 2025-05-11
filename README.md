# ***FastrawGIS***

[![PYTHON](https://img.shields.io/badge/python-3.12.10-0352fc?style=for-the-badge&logo=python&logoColor=white)](https://github.com/python/cpython/)

[![FASTAPI](https://img.shields.io/badge/fastapi-0.115.12-009485?style=for-the-badge&logo=fastapi&logoColor=white)](https://github.com/fastapi/fastapi/)

[![STRAWBERRY](https://img.shields.io/badge/strawberry-0.266.1-b80202?style=for-the-badge&logo=graphql&logoColor=white)](https://github.com/strawberry-graphql/strawberry/)

[![STARLETTE](https://img.shields.io/badge/starlette-0.46.2-174da3?style=for-the-badge&logo=starlette&logoColor=white)](https://github.com/encode/starlette/)

[![ANYIO](https://img.shields.io/badge/anyio-4.9.0-1f5ab8?style=for-the-badge&logo=anyio&logoColor=white)](https://github.com/agronholm/anyio/)

[![PYDANTIC](https://img.shields.io/badge/pydantic-2.11.4-e92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://github.com/pydantic/pydantic/)

[![PYDANTIC-SETTINGS](https://img.shields.io/badge/pydantic_settings-2.9.1-e92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://github.com/pydantic/pydantic-settings/)

[![POSTGIS](https://img.shields.io/badge/postgis-16-0b3373?style=for-the-badge&logo=postgresql&logoColor=white)](https://github.com/postgis/postgis/)

[![SQLALCHEMY](https://img.shields.io/badge/sqlalchemy-2.0.40-b80202?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://github.com/sqlalchemy/sqlalchemy/)

[![GEOALCHEMY](https://img.shields.io/badge/geoalchemy2-0.17.1-b80202?style=for-the-badge&logo=geoalchemy&logoColor=white)](https://github.com/geoalchemy/geoalchemy2/)

[![ASYNCPG](https://img.shields.io/badge/asyncpg-0.30.0-b87811?style=for-the-badge&logo=asyncpg&logoColor=white)](https://github.com/MagicStack/asyncpg/)

[![TYPER](https://img.shields.io/badge/typer-0.15.3-080606?style=for-the-badge&logo=typer&logoColor=white)](https://github.com/fastapi/typer/)

[![CLICK](https://img.shields.io/badge/click-8.1.8-080606?style=for-the-badge&logo=click&logoColor=white)](https://github.com/pallets/click/)

[![RICH](https://img.shields.io/badge/rich-14.0.0-5e5c78?style=for-the-badge&logo=rich&logoColor=white)](https://github.com/Textualize/rich/)

[![HYPERCORN](https://img.shields.io/badge/hypercorn-0.17.3-0094?style=for-the-badge&logo=hypercorn&logoColor=white)](https://github.com/pgjones/hypercorn/)

[![UVLOOP](https://img.shields.io/badge/uvloop-0.21.0-b87811?style=for-the-badge&logo=uvloop&logoColor=white)](https://github.com/MagicStack/uvloop/)

[![DOCKER](https://img.shields.io/badge/docker-0352fc?style=for-the-badge&logo=docker&logoColor=white)](https://github.com/docker-library/python/)

![LICENSE-MIT](https://img.shields.io/badge/LICENSE-MIT-202235.svg?logo=&labelColor=202235&color=edb641&logoColor=edb641)

-   [Motivation](#motivation)
-   [Description](#description)
-   [Features](#features)
-   [Requirements](#requirements)
-   [Setup](#setup)
-   [Usage](#usage)
-   [GraphQL Schema](#graphql-schema)
-   [Diagram](#diagram)

## Motivation

This repository is intended to serve as a working example of an API that
combines several tools and topics. Basically, **FastrawGIS** supports
asynchronous handling of HTTP requests with GraphQL syntax, converting
them into database queries and returning the proper results.

## Description

The main purpose of the app is to design and model events, locations,
and timetables so that the underlying spatial database allows queries regarding
distance and time factors.

## Features

- Simple setup.
- Fast response.
- Validation of requests.
- Type hinted code, divided in different layers.
- Easily extendable with more models, fields, and filters.
- Search by space, supporting geographic coordinates and radius with meters accuracy.
- Search by time, supporting schedules with minutes accuracy.

## Requirements

- Docker Compose.
- Some GraphQL client, like for example [Bruno](https://github.com/usebruno/bruno/).

## Setup

```bash
docker compose up
```

Host's port 80 should be available. Otherwise, it can be customized at `docker-compose.yml`.

The following two commands create and load the database.

```bash
docker exec -it fastrawgis-app python app/cli/database/main.py create
docker exec -it fastrawgis-app python app/cli/database/main.py load
```

## Usage

We can leverage real sample data and perform `POST` requests to `http://localhost/graphql`,
obtaining two items with each of the following queries.

Search by space.

```graphql
{
  events (
    day: "25-07-12",
    lat: 41.39491039820101,
    lon: 2.1755553553648936,
    radius: 2500,
  ) {
    id
    venue {
      id
      town {
        id
        name
      }
      name
      point {
        lat
        lon
      }
      address
      distance
    }
    name
    start
    end
    desc
  }
}
```

Search by time.

```graphql
{
  events (
    day: "25-07-12",
    startTime: "8:00",
    endTime: "12:00",
  ) {
    id
    venue {
      id
      town {
        id
        name
      }
      name
      point {
        lat
        lon
      }
      address
    }
    name
    start
    end
    desc
  }
}
```
## GraphQL Schema

If you change the GraphQL schema at `schema.py` and want to check
the corresponding `schema.gql`, it can be generated this way.

```bash
docker exec -it fastrawgis-app strawberry export-schema app.api.schema:schema > app/api/schema.gql
```

## Diagram

The diagram shows the interaction between the main components of the application.

![DIAGRAM](images/diagram.png)