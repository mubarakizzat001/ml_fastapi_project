from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from typing import Annotated
from config import settings

engine= create_async_engine(settings.database_url, echo=True)


async def create_db_and_tables():
    async with engine.begin() as conn:
        from .models import FinanceApp 
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session

