from pydantic import BaseModel


class ReservationBase(BaseModel):
    title: str
    description: str | None = None


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    reservations: list[Reservation] = []

    class Config:
        orm_mode = True