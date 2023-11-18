from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from models.models import Person
app = Flask(__name__)
app.secret_key = "somesecretkeythatonlyishouldknow"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:course123@localhost/users"
engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], echo=True)
Person.__table__.create(engine, checkfirst=True)
@app.route("/")
def index():
 return "Hello World!"
if __name__ == "__main__":
 app.run(debug=True)

 from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy.ext.declarative import declared_attr
class Base(DeclarativeBase):
 pass
class BaseModel:
 @declared_attr
 def __tablename__(cls):
    return cls.__name__.lower()
class Person(BaseModel, Base):
 __tablename__ = 'person'
 id:Mapped[int] = mapped_column(Integer, primary_key=True)
 name:Mapped[str] = mapped_column(String(50))

from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime
from typing import Optional
class Base(DeclarativeBase):
 pass
class BaseModel:
 @declared_attr
 def __tablename__(cls):
    return cls.__name__.lower()
class Base(DeclarativeBase):
 pass
class ClientProfile(BaseModel: Base)
__tablename__ = "client_profile"
id: Mapped[int] = mapped_column(Integer, primary_key=True)
created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
created_by: Mapped[str] = mapped_column(String(100), insert_default="system")
updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
updated_by: Mapped[str] = mapped_column(String(100), insert_default="system")
unique_id: Mapped[str] = mapped_column(String(64), unique=True)
