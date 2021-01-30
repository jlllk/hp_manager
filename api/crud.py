from sqlalchemy.orm import Session

from . import models, schemas


def db_write(db: Session, obj):
    db.add(obj)
    db.commit()
    db.refresh(obj)


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserBase):
    db_user = models.User(name=user.name)
    db_write(db, db_user)
    return db_user


def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Game).offset(skip).limit(limit).all()


def create_game(db: Session, game: schemas.GameBase):
    db_game = models.Game(title=game.title)
    db_write(db, db_game)
    return db_game


def create_session(
        db: Session,
        session: schemas.SessionCreate, user_id: int, game_id: int):
    db_session = models.Session(
        **session.dict(),
        owner_id=user_id,
        game_id=game_id,
    )
    db_write(db, db_session)
