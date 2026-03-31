from fastapi import APIRouter, Depends

from app.modules.catalog.catalog_depency_injection import get_repository
from app.modules.catalog.repositories.award_repository_sqlalchemy import AwardRepositorySQLAlchemy
from app.modules.catalog.services.award_service import AwardService

router = APIRouter(prefix="/catalog", tags=["catalog"])

@router.get("/awards")
def list_awards(repo = Depends(get_repository(AwardRepositorySQLAlchemy))):
    service = AwardService(repo)
    return service.get_award_list()
