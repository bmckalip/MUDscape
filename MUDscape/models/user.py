from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (UniqueConstraint('name', name='_name_uc'),)

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
