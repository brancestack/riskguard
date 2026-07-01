from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.repositories.dashboard_repository import DashboardRepository
from app.schemas.dashboard import DashboardSummaryResponse
from app.schemas.transaction import TransactionResponse
from app.services.dashboard_service import DashboardService

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


def get_dashboard_service(db: Session = Depends(get_db)) -> DashboardService:
    repository = DashboardRepository(db)
    return DashboardService(repository)


@router.get("/summary", response_model=DashboardSummaryResponse)
def get_dashboard_summary(
    current_user: User = Depends(get_current_user),
    service: DashboardService = Depends(get_dashboard_service)
):
    return service.get_summary()


@router.get("/high-risk", response_model=list[TransactionResponse])
def get_high_risk_transactions(
    limit: int = Query(default=10, ge=1, le=50),
    current_user: User = Depends(get_current_user),
    service: DashboardService = Depends(get_dashboard_service)
):
    return service.get_high_risk_transactions(limit=limit)