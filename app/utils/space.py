from geoalchemy2 import WKBElement, WKTElement
from shapely import wkb

from app.constants import SRID


def get_lat_lon_from_point(point: WKBElement) -> tuple[float, float]:
    point = wkb.loads(bytes(point.data))
    return point.y, point.x


def get_point_from_lat_lon(lat: float, lon: float) -> WKTElement:
    return WKTElement(f"POINT({lon} {lat})", srid=SRID)
