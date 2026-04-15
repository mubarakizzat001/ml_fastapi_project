from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime,timedelta
from ..api import FinanceAppCreate, FinanceAppRead, FinanceAppUpdate
from src.database.models import FinanceApp
from service.ModelService import ModelService



class FinanceAppService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_finance_app(self,app_id: int)->FinanceApp:
        result = await self.session.get(FinanceApp, app_id)
        
        return result
    async def create_finance_app(self,finance_app_create: FinanceAppCreate)->FinanceApp:
        serivce= ModelService()
        new_app = FinanceApp(**finance_app_create.model_dump())
        prediction_result = serivce.predict(finance_app_create)
        new_app.prediction = prediction_result.get("Prediction:")
        new_app.Probability = prediction_result.get("Probability:")
        new_app.created_at = datetime.utcnow()
        new_app.updated_at = datetime.utcnow()

        self.session.add(new_app)
        await self.session.commit()
        await self.session.refresh(new_app)
        return new_app
    
    async def update_finance_app(self,app_id:int, finance_app_update: FinanceAppUpdate)->FinanceApp:
        app_update = await self.get_finance_app(app_id)
        if not app_update:
            return None
        finance_app= FinanceApp(**finance_app_update.model_dump(exclude_unset=True)))
        finance_app.updated_at = datetime.utcnow()
        app_update.sqlmodel_update(finance_app)
        await self.session.commit()
        await self.session.refresh(app_update)
        return app_update
    
    async def delete_finance_app(self,app_id:int)->None:
        app_delete = await self.get_finance_app(app_id)

        await self.session.delete(app_delete)
        await self.session.commit()
        
        
