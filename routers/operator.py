from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
from cruds import crud_operator

router=APIRouter()


# Function POST
@router.post("/operators/", response_model=schemas.Operator)
def create_operator(operator: schemas.OperatorCreate, db: Session = Depends(get_db)):
    return crud_operator.create_operator(db=db, operator=operator)


# Function GET
@router.get("/operators/", response_model=list[schemas.Operator])
def read_operators(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    operators = crud_operator.get_operators(db, skip=skip, limit=limit)
    return operators


# By ID
@router.get("/operators/{operator_id}", response_model=schemas.Operator)
def read_operator(operator_id: int, db: Session = Depends(get_db)):
    db_operator = crud_operator.get_operator(db, operator_id=operator_id)
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    return db_operator


# By Weapon
@router.get("/operators/filter-weapon/{weapon_id}", response_model=list[schemas.Operator])
def read_operator_weapon(weapon_id: int, db: Session = Depends(get_db)):
    db_operator = crud_operator.get_operator_weapon(db, weapon_id=weapon_id)
    return db_operator

# By Quarter General
@router.get("/operators/filter-qg/{qg_id}", response_model=list[schemas.Operator])
def read_operator_weapon(qg_id: int, db: Session = Depends(get_db)):
    db_operator = crud_operator.get_operator_qg(db, qg_id=qg_id)
    return db_operator

# By Mission
@router.get("/operators/filter-mission/{mission_id}", response_model=list[schemas.Operator])
def read_operator_mission(mission_id: int, db: Session = Depends(get_db)):
    db_operator = crud_operator.get_operator_mission(db, mission_id=mission_id)
    return db_operator


# By Name
@router.get("/operators/filter-name/{name}", response_model=list[schemas.Operator])
def read_operator_name(name: str, db: Session = Depends(get_db)):
    db_operator = crud_operator.get_operator_name(db, name=name)
    return db_operator


# By Nationality
@router.get("/operators/filter-nationality/{nationality}", response_model=list[schemas.Operator])
def read_operator_nationality(nationality: str, db: Session = Depends(get_db)):
    db_operator = crud_operator.get_operator_nationality(db, nationality=nationality)
    return db_operator


# Function DELETE
@router.delete("/operators/{operator_id}")
def delete_operator(operator_id: int, db: Session = Depends(get_db)):
    db_operator = crud_operator.delete_operator(db, operator_id=operator_id)
    return "Operator eliminated"


# Function PUT
@router.put("/operators/{operator_id}", response_model=schemas.Operator)
def change_operator(operator: schemas.OperatorCreate, operator_id: int, db: Session = Depends(get_db)):
    db_operator = crud_operator.put_operator(db, operator_id=operator_id, operator=operator)

    return db_operator
