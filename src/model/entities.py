from sqlalchemy import Column, Integer, String, Sequence
from database import connector

class Message(connector.Manager.Base):
    __tablename__ = 'message'
    id = Column(Integer, Sequence('message_id_seq'), primary_key=True, autoincrement=True)
    message = Column(String(255))
    topic = Column(String(255))
