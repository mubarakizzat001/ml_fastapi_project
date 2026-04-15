from typing import Optional

from pydantic import BaseModel, Field
from .enum.FinanceAppEnum import maritalstatus , HouseOwnership
class FinanceAppBase(BaseModel):
    Income: float = Field(..., gt=0)
    Age: int = Field(..., ge=18, le=100)
    Experience: int
    marital_status: maritalstatus
    House_Ownership: HouseOwnership
    Car_Ownership: str
    Profession: str
    CITY: str
    STATE: str
    CURRENT_JOB_YRS: int
    CURRENT_HOUSE_YRS: int
class FinanceAppRead(FinanceAppBase):
    Id: int

class FinanceAppCreate(FinanceAppBase):
    pass 

class FinanceAppUpdate(BaseModel):
    Income: Optional[float] = Field(None, gt=0)
    Age: Optional[int] = Field(None, ge=18, le=100)
    Experience: Optional[int] = None
    marital_status: Optional[maritalstatus] = None
    House_Ownership: Optional[HouseOwnership] = None
    Car_Ownership: Optional[str] = None
    Profession: Optional[str] = None
    CITY: Optional[str] = None
    STATE: Optional[str] = None
    CURRENT_JOB_YRS: Optional[int] = None
    CURRENT_HOUSE_YRS: Optional[int] = None
    