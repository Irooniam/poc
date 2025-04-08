import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, exc
from sqlalchemy.orm import Mapped, mapped_column
import logging
logger = logging.getLogger(__name__)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class User(db.Model):
    __tablename__ = "leads"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    address1: Mapped[str] = mapped_column(String(100))
    address2: Mapped[str] = mapped_column(String(100))
    city: Mapped[str] = mapped_column(String(100))
    state: Mapped[str] = mapped_column(String(2))
    city: Mapped[str] = mapped_column(String(100))
    zip: Mapped[int] = mapped_column(Integer)
    phone: Mapped[str] = mapped_column(String(20))


def connectDB(app):
    try:
        with app.app_context():
            db.create_all()
            return True 
    except exc.OperationalError as e:
        logger.error("cant connect to database error {}".format(e))
        return False 
