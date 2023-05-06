from sqlalchemy import Column, Integer, String, ForeignKey, Table
from db import Base
from sqlalchemy.orm import relationship


class Participant(Base):
    __tablename__ = 'participants'

    id = Column(Integer, primary_key=True)
    team_name = Column(String(250), nullable=False)
    participants = relationship('Teammate')

    def __repr__(self):
        return f"Team (ID: {self.id}, Name: {self.team_name})"
