from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, String, TIMESTAMP, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Event(Base):
    __tablename__ = "events"
    __table_args__ = (UniqueConstraint("venue_id", "name", "start", name="events_venue_id_name_start_key"),)

    id: Mapped[UUID] = mapped_column(primary_key=True, init=False, default_factory=uuid4)
    venue_id: Mapped[UUID] = mapped_column(ForeignKey("venues.id"))
    name: Mapped[str] = mapped_column(String(100))
    start: Mapped[datetime] = mapped_column(TIMESTAMP, index=True)
    end: Mapped[datetime] = mapped_column(TIMESTAMP, index=True)
    desc: Mapped[str] = mapped_column(String(1000), nullable=True, default=None)
