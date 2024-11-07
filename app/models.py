from datetime import datetime

from sqlalchemy import (
    func,
    Integer
)
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    user_id = mapped_column(Integer, primary_key=True)
    last_name: Mapped[str]
    first_name: Mapped[str]
    middle_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
