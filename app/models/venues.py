from uuid import UUID, uuid4

from geoalchemy2 import Geography, WKBElement
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, query_expression

from app.constants import SRID
from app.database import Base


class Venue(Base):
    __tablename__ = "venues"
    __table_args__ = (UniqueConstraint("town_id", "name", name="venues_town_id_name_key"),)

    id: Mapped[UUID] = mapped_column(primary_key=True, init=False, default_factory=uuid4)
    town_id: Mapped[UUID] = mapped_column(ForeignKey("towns.id"))
    name: Mapped[str] = mapped_column(String(100), index=True)
    point: Mapped[WKBElement] = mapped_column(Geography(geometry_type="POINT", srid=SRID))
    address: Mapped[str] = mapped_column(String(100), nullable=True, default=None)
    distance: Mapped[int] = query_expression()
