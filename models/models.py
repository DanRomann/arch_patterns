from sqlalchemy import Column, Integer, String, ForeignKey
from models.database import Base


class City(Base):
    __tablename__ = "city"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return self.name + str(self.id)


class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city_id = Column(Integer, ForeignKey("city.id"), nullable=True)

    def __repr__(self):
        return f"{self.name} + {self.id}"