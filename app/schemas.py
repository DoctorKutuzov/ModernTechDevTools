from datetime import datetime

from pydantic import BaseModel


class UserInSchema(BaseModel):
    last_name: str | None = None
    first_name: str | None = None
    middle_name: str | None = None
    email: str


class UserOutSchema(UserInSchema):
    user_id: int
    created_at: datetime
