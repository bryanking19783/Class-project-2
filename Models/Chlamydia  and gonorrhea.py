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
 first_name: Mapped[str] = mapped_column(String(100))
 middle_name: Mapped[Optional[str]] = mapped_column(String(100))
 last_name: Mapped[str] = mapped_column(String(100))
 date_of_birth: Mapped[datetime] = mapped_column(DateTime)
 country_of_birth: Mapped[str] = mapped_column(String(150))
 gender: Mapped[str] = mapped_column(String(30))
 gender_identity: Mapped[str] = mapped_column(String(50))
 phone_number: Mapped[Optional[str]] = mapped_column(String(30))
 address: Mapped[Optional[str]] = mapped_column(String(255))
 city: Mapped[Optional[str]] = mapped_column(String(100))
 state: Mapped[Optional[str]] = mapped_column(String(100))
 zip_code: Mapped[Optional[str]] = mapped_column(String(20))
 country: Mapped[Optional[str]] = mapped_column(String(150))
 email: Mapped[Optional[str]] = mapped_column(String(150))
 ethnicity: Mapped[str] = mapped_column(String(100))
 race: Mapped[str] = mapped_column(String(50))
 sexual_orientation: Mapped[str] = mapped_column(String(64))
 employment_status: Mapped[str] = mapped_column(String(64))
 class ClientScreening(BaseModel, Base):
    __tablename__ = "client_screening"
 id: Mapped[int] = mapped_column(Integer, primary_key=True)
 created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
 created_by: Mapped[str] = mapped_column(String(64), insert_default="system")
 updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
 updated_by: Mapped[str] = mapped_column(String(64), insert_default="system")

 unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", 
onupdate="CASCADE", ondelete="CASCADE"))
 date_of_screening: Mapped[datetime] = mapped_column(DateTime)
 health_care_provider: Mapped[str] = mapped_column(String(64))
 reporter_name: Mapped[str] = mapped_column(String(64))
 reporter_contact: Mapped[str] = mapped_column(String(64))
 sexual_partner_gender: Mapped[str] = mapped_column(String(64))
 sexual_partner_gender_identity: Mapped[str] = mapped_column(String(64))
 previous_HIV_screening: Mapped[str] = mapped_column(String(10))
 previous_HIV_screening_date: Mapped[datetime] = mapped_column(DateTime)
 previous_HIV_screening_result: Mapped[str] = mapped_column(String(64))
 reason_for_testing: Mapped[str] = mapped_column(String(64))
 screening_type: Mapped[str] = mapped_column(String(64))
 site_of_sample_collection: Mapped[str] = mapped_column(String(64))
 sample_collection_date: Mapped[datetime] = mapped_column(DateTime)
 screening_result: Mapped[str] = mapped_column(String(64))
 screening_notes: Mapped[Optional[str]] = mapped_column(String(64))
 diagnosis: Mapped[str] = mapped_column(String(64))
class ClientTreatment(BaseModel, Base):
 __tablename__ = "client_treatment"
 id: Mapped[int] = mapped_column(Integer, primary_key=True)
 created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
 created_by: Mapped[str] = mapped_column(String(64), insert_default="system")
 updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
 updated_by: Mapped[str] = mapped_column(String(64), insert_default="system")
 unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", 
onupdate="CASCADE", ondelete="CASCADE"))
 date_of_treatment: Mapped[datetime] = mapped_column(DateTime)
 health_care_provider: Mapped[str] = mapped_column(String(64))
 reporter_name: Mapped[str] = mapped_column(String(64))
 reporter_contact: Mapped[str] = mapped_column(String(64))
 treatment_type: Mapped[str] = mapped_column(String(64))
 treatment_plan: Mapped[Optional[str]] = mapped_column(String(64))
 treatment_notes: Mapped[Optional[str]] = mapped_column(String(64))
 treatment_result: Mapped[str] = mapped_column(String(64)

 class PartnerManagement(BaseModel, Base):
 __tablename__ = "partner_management"
 id: Mapped[int] = mapped_column(Integer, primary_key=True)
 created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
 created_by: Mapped[str] = mapped_column(String(64), insert_default="system")
 updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
 updated_by: Mapped[str] = mapped_column(String(64), insert_default="system")
 unique_id: Mapped[str] = mapped_column(String(64),unique=True)
 partner_unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", 
onupdate="CASCADE", ondelete="CASCADE"))
 date_of_partner_management: Mapped[datetime] = mapped_column(DateTime)
 health_care_provider: Mapped[str] = mapped_column(String(64))
 reporter_name: Mapped[str] = mapped_column(String(64))
 reporter_contact: Mapped[str] = mapped_column(String(64))
 partner_management_type: Mapped[str] = mapped_column(String(64))
 partner_management_plan: Mapped[Optional[str]] = mapped_column(String(64))
 partner_management_notes: Mapped[Optional[str]] = mapped_column(String(64))
 partner_management_result: Mapped[str] = mapped_column(String(64)