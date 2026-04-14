from typing import Optional

from pydantic import BaseModel, Field
from .enum.FinanceAppEnum import maritalstatus , HouseOwnership



class FinanceAppSchema(BaseModel):
    Id: Optional[int] =0
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
