from fastapi import HTTPException
from sqlalchemy.orm import Session
from appsql import models, schemas


# GET function
def get_qg(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.GQ).offset(skip).limit(limit).all()


# Create function
def create_qg(db: Session, qg: schemas.QGCreate):
    db_qg = models.GQ(country=qg.country)
    db.add(db_qg)
    db.commit()
    db.refresh(db_qg)
    return db_qg

# DELETE function
def delete_qg(db: Session, qg_id: int):
    db_qg = db.query(models.GQ).filter(models.GQ.id == qg_id).first()
    if db_qg is None:
        raise HTTPException(status_code=404, detail="Quarter general not found")
    db.delete(db_qg)
    db.commit()
    return db_qg
