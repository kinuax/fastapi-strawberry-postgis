from uuid import UUID, uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Town(Base):
    __tablename__ = "towns"

    id: Mapped[UUID] = mapped_column(primary_key=True, init=False, default_factory=uuid4)
    name: Mapped[str] = mapped_column(String(100), unique=True)
