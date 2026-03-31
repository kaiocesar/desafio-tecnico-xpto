from fastapi import APIRouter, Depends

from app.modules.catalog.catalog_depency_injection import get_repository
from app.modules.catalog.repositories.award_repository_sqlalchemy import AwardRepositorySQLAlchemy

router = APIRouter(prefix="/catalog", tags=["catalog"])

@router.get("/awards")
def list_awards(repo = Depends(get_repository(AwardRepositorySQLAlchemy))):
    return repo.find_all()
