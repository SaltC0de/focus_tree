from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from deps import get_current_user, get_db
from models import FocusSettings, User
from schemas import FocusSettingsRead, FocusSettingsUpdate


router = APIRouter(prefix="/focus-settings", tags=["focus-settings"])


@router.get("/", response_model=FocusSettingsRead)
def get_focus_settings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    settings = db.query(FocusSettings).filter(FocusSettings.user_id == current_user.id).first()

    if not settings:
        settings = FocusSettings(
            user_id=current_user.id,
            mode="timer",
            duration_minutes=25,
            allowed_apps=[],
        )
        db.add(settings)
        db.commit()
        db.refresh(settings)

    return settings


@router.put("/", response_model=FocusSettingsRead)
def update_focus_settings(
    payload: FocusSettingsUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    settings = db.query(FocusSettings).filter(FocusSettings.user_id == current_user.id).first()

    if not settings:
        settings = FocusSettings(user_id=current_user.id)
        db.add(settings)

    settings.mode = payload.mode
    settings.duration_minutes = payload.duration_minutes
    settings.allowed_apps = payload.allowed_apps

    db.commit()
    db.refresh(settings)

    return settings