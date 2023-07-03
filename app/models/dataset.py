# SQLAlchemy ORM table

# FIXME: Figure out what base model to import
from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship # TODO: create relationship between table
from db.database import Base

class Dataset(Base):
    """
    TODO: Update docstring
    field_name = Column(data_type)
    """

    __tablename__ = "datasets"

    # TODO: what does settin index=True do?
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    full_name = Column(String, unique=True, index=True)
    description = Column(String)
    added_on = Column(Date)
    start_date = Column(Date)
    end_date = Column(Date)
    owner = Column(String, index=True)
    deprecated = Column(Boolean)
