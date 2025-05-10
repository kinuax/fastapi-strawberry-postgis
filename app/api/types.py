import strawberry


@strawberry.type
class Point:
    lat: float
    lon: float


@strawberry.type
class Town:
    id: str
    name: str


@strawberry.type
class Venue:
    id: str
    town: Town
    name: str
    point: Point
    address: str | None
    distance: int | None


@strawberry.type
class Event:
    id: str
    venue: Venue
    name: str
    start: str
    end: str
    desc: str | None
