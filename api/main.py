import uvicorn

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from api import crud, models, schemas
from database import SessionLocal


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/users', response_model=schemas.User)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400,
                            detail='This name is already registered')
    return crud.create_user(db=db, user=user)


@app.get('/users/{user_id}', response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@app.patch('/users/{user_id}', response_model=schemas.User)
def update_user_balance(user_id: int,
                        balance: schemas.Balance,
                        db: Session = Depends(get_db)):
    db_user = crud.update_balance(db=db, user_id=user_id, update=balance)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
