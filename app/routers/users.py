from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.models import User
from app.schemas import (
    UserInSchema,
    UserOutSchema,
)

users_router = APIRouter(
    prefix='/users',
    tags=['users']
)


@users_router.post('/register', response_model=UserOutSchema)
async def register_user(user_data: UserInSchema, session: AsyncSession = Depends(get_session)):
    new_user = User(**dict(user_data))
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


@users_router.get('/{user_id}', response_model=UserOutSchema | None)
async def register_user(user_id: int, session: AsyncSession = Depends(get_session)):
    try:
        user = await session.get_one(User, user_id)
    except NoResultFound as err:
        print(err)
        user = None
    return user
