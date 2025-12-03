from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    
    def __repr__(self):
        return f"<Message(id={self.id}, content='{self.content}', timestamp={self.timestamp})>"


class MessageDB: 
    def __init__(self, session: Session):
        self.session = session

    def add_message(self, content, timestamp):
        new_message = Message(content=content, timestamp=timestamp)
        try: 
            self.session.add(new_message)
            self.session.commit()
            return new_message
        except Exception as e:
            self.session.rollback()
            raise e

    def get_all_messages(self):
        try: 
            messages = self.session.query(Message).all()
            return messages
        except Exception as e:
            self.session.rollback()
            raise e
