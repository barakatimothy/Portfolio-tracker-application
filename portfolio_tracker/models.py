# portfolio_tracker/models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)

    portfolios = relationship('Portfolio', back_populates='user')

class Portfolio(Base):
    __tablename__ = 'portfolios'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='portfolios')
    assets = relationship('Asset', back_populates='portfolio')

class Asset(Base):
    __tablename__ = 'assets'
    id = Column(Integer, primary_key=True)
    symbol = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    portfolio_id = Column(Integer, ForeignKey('portfolios.id'), nullable=False)

    portfolio = relationship('Portfolio', back_populates='assets')
