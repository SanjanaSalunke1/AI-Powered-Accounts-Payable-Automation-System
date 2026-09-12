from pydantic import BaseModel, ConfigDict, EmailStr

from app.models.role import UserRole


class UserResponse(BaseModel):
    id: str
    email: EmailStr
    first_name: str
    last_name: str
    role: UserRole
    is_active: bool

    model_config = ConfigDict(
        from_attributes=True,
    )