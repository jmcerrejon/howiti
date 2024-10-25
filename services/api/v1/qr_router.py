from typing import Union

from fastapi import APIRouter, HTTPException, Path

from model import models
from model.database import DBSession
from schemas import QR, UserType

QR_DEFAULT_PATH = "qr"
qr_router = APIRouter(prefix="/v1/qr")


@qr_router.get("/")
async def read_QRs():
    db = DBSession()
    try:
        qrs = db.query(models.QR).all()
    finally:
        db.close()
    return qrs


@qr_router.post("/")
def add_QR(qr: QR):
    db = DBSession()
    try:
        if len(qr.email) == 0 and len(qr.qr_content) == 0:
            raise HTTPException(
                status_code=400,
                detail={
                    "status": "Error 400 - Bad Request",
                    "msg": "Both 'title' and 'note_body' are empty. These are optional attributes but at least one must be provided.",
                },
            )
        new_qr = models.QR(id=qr.id, email=qr.email, qr_info=qr.qr_info)
        db.add(new_qr)
        db.commit()
        db.refresh(new_qr)
    finally:
        db.close()
    return new_qr


@qr_router.get(f"/{{user_type}}/{QR_DEFAULT_PATH}/{{qr_id}}")
async def read_qr(
    user_type: UserType, qr_id: int = Path(..., ge=1), q: Union[str, None] = None
):
    return {
        "id": qr_id,
        "user": user_type,
    }


@qr_router.put(f"/{{user_type}}/{QR_DEFAULT_PATH}/{{qr_id}}")
async def update_qr(user_type: UserType, item: QR, qr_id: int = Path(..., ge=1)):
    return {
        "id": qr_id,
        "name": item.name,
        "user": user_type,
    }
