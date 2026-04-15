from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.seesion import get_session
from .services import FinanceAppService
from typing import Annotated

sessiondep= Annotated[AsyncSession, Depends(get_session)]


def get_finance_app_service(session: sessiondep):
    return FinanceAppService(session)


servicedep= Annotated[FinanceAppService, Depends(get_finance_app_service)]

