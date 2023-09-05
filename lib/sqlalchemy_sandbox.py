#!/usr/bin/env python3



from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base




Base = declarative_base()




class Student(Base):
    __tablename__= 'students'
    id=Column(Integer(),primary_key=True)
    name=Column(String())
    
    # this is a model class 

if __name__ == '__main__':
    # data  models

    engine=create_engine("sqlite:///students.db")
    try:
        Base.metadata.create_all(engine)
        print("Table was created Successfully",Student.__tablename__)
    except Exception as e:
        print("an error occured:",str(e))    