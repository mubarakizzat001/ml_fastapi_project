from fastapi import APIRouter,HTTPException, status
from database.model import FinanceApp
from api.dependencies import servicedep
from api import FinanceAppCreate



router= APIRouter(prefix="/financeapp", tags=["FinanceApp"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_finance_app(finance_app: FinanceAppCreate,service:servicedep):
    try:
        created_app = await service.create_finance_app(finance_app)
        return {
            "Id": created_app.Id,
            "probability": created_app.probability,
            "prediction": created_app.prediction
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
        
@router.get("/{id}", status_code=status.HTTP_200_OK,response_model=FinanceApp)
async def get_finance_app(id: int, service: servicedep):
    try:
        finance_app = await service.get_finance_app(id)
        if not finance_app:
            raise HTTPException(status_code=404, detail="FinanceApp not found")
        return finance_app
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_finance_apps(service: servicedep,limit: int = 100, offset: int = 0):
    try:
        finance_apps = await service.get_all_finance_apps(limit, offset)
        return finance_apps
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_finance_app(id: int, service: servicedep):
    try:
        await service.delete_finance_app(id)
        return{
                "message": f"FinanceApp with id {id} has been deleted successfully."
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.patch("/{id}", status_code=status.HTTP_200_OK)
async def update_finance_app(id: int, finance_app: FinanceApp, service: servicedep):
    try:
        updated_app = await service.update_finance_app(id, finance_app)
        if not updated_app:
            raise HTTPException(status_code=404, detail="FinanceApp not found")
        return updated_app
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    