from fastapi import APIRouter, Depends

router = APIRouter(prefix="/catalog", tags=["catalog"])

@router.get("/awards")
def list_awards():
    return {"min": [], "max": []}
