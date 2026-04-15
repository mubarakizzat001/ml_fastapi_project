from sqlmodel import SQLModel, Field
from .enum.FinanceAppEnum import maritalstatus , HouseOwnership


class FinanceApp(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
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
    prediction: int = Field(default=None)
    Probability: float = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    