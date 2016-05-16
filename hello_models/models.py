from sqlalchemy import Column, Integer, String
from hello_models.database import Base


class Room(Base):
    __tablename__ = 'room'
    room_id = Column(Integer, primary_key=True)
    building_link = Column(String(100))
    floorplan_image_link = Column(String(100))


class TestObject(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    key = Column(String(100))
    value = Column(String(100))

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __repr__(self):
        return '<TestObject {}:{}>'.format(self.key, self.value)


class KeyVal(Base):
    __tablename__ = 'keyval'
    id = Column(Integer, primary_key=True)
    key = Column(String(200))
    value = Column(String(200))

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
