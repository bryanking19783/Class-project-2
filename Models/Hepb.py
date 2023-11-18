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
 class ClientProfile(BaseModel: Base;)
__tablename__ = "client_profile"
id: Mapped[int] = mapped_column(Integer, primary_key=True)
created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
created_by: Mapped[str] = mapped_column(String(100), insert_default="system")
updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
updated_by: Mapped[str] = mapped_column(String(100), insert_default="system")
unique_id: Mapped[str] = mapped_column(String(64), unique=True)
Last_Name: Mapped[str] = mapped_column(String(64))
First_Name: Mapped[str] = mapped_column(String(64))
Middle_Name: Mapped[str] = mapped_column(String(64))
Date_of_Birth:Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
Estimated_Delivery_Date:Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
Patient_aware_of_HepB_status:Mapped[str] = mapped_column(String(150))
Address:Mapped[str] = mapped_column(String(150))
City:Mapped[str] = mapped_column(String(150))
State:Mapped[str] = mapped_column(String(150))
Zip:Mapped[str] = mapped_column(String(150))
Phone_Number:Mapped[str] = mapped_column(String(150))
Type_of_Insurance:Mapped[str] = mapped_column(String(150))
Race:Mapped[str] = mapped_column(String(150))
Hispanic:Mapped[str] = mapped_column(String(150))
Country_of_Birth: Mapped[str] = mapped_column(String(150))
Primary_Language: Mapped[str] = mapped_column(String(150))
class labatory_results(BaseModel, Base):
 __tablename__ = "LABOTORY RESULTS"
 id: Mapped[int] = mapped_column(Integer, primary_key=True)
 created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
 created_by: Mapped[str] = mapped_column(String(64), insert_default="system")
 updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
 updated_by: Mapped[str] = mapped_column(String(64), insert_default="system")
 unique_id: Mapped[str] = mapped_column(String(64),unique=True)
Laboratory_Results: Mapped[str] = mapped_column(String(150))
class Clinical_Information(BaseModel, Base):
 __tablename__ = "Clinical Information"
id: Mapped[int] = mapped_column(Integer, primary_key=True)
created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
created_by: Mapped[str] = mapped_column(String(64), insert_default="system")
updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
updated_by: Mapped[str] = mapped_column(String(64), insert_default="system")
unique_id: Mapped[str] = mapped_column(String(64),unique=True)
OB_Provider_Last_Name:Mapped[str] = mapped_column(String(64),unique=True)
OB_Provider_First_Name:Mapped[str] = mapped_column(String(64),unique=True)
Expected_Delivery_Facility:Mapped[str] = mapped_column(String(64),unique=True)
Reporting_Health_Care_Facility:Mapped[str] = mapped_column(String(64),unique=True)
Address:Mapped[str] = mapped_column(String(150))
City:Mapped[str] = mapped_column(String(150))
State:Mapped[str] = mapped_column(String(150))
Zip:Mapped[str] = mapped_column(String(150))
Contact_person_reporting_at_facility:Mapped[str] = mapped_column(String(150))
Direct_Phone:Mapped[str] = mapped_column(String(150))
Date_Form_Completed:Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())