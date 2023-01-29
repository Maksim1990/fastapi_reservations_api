from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    reservations = relationship("Reservation", back_populates="user")

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(String(255), index=True)
    country = Column(String(255), index=True)

    rooms = relationship("Room", back_populates="hotel")

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(String(255), index=True)
    country = Column(String(255), index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))

    hotel = relationship("Hotel", back_populates="rooms")
    reservations = relationship("Reservation", back_populates="room")

class Reservation(Base):
    __tablename__ = "reservations"


    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))

    user = relationship("User", back_populates="reservations")
    room = relationship("Room", back_populates="reservations")