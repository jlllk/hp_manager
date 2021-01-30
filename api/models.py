from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    balance = Column(Integer, index=True, default=0)

    sessions = relationship('Session', back_populates='owner')


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    sessions = relationship('Session', back_populates='game')


class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True, index=True)
    deposit = Column(Integer, default=0)
    cash_out = Column(Integer, default=0)
    owner_id = Column(Integer, ForeignKey('users.id'))
    game_id = Column(Integer, ForeignKey('games.id'))

    owner = relationship('User', back_populates='sessions')
    game = relationship('Game', back_populates='sessions')




