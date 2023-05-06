from sqlalchemy import Column, Integer, String, ForeignKey, Table
from db import Base
from sqlalchemy.orm import relationship


association_table = Table('association', Base.metadata,
                          Column('tournament_id', Integer, ForeignKey('tournaments.id')),
                          Column('participant_id', Integer, ForeignKey('participants.id')))


class Tournament(Base):
    __tablename__ = 'tournaments'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    winner = Column(String(250))
    participants = relationship('Participant', secondary=association_table, backref='participants_tournaments')

    def __repr__(self):
        return f"Tournament (ID: {self.id}, Name: {self.name}, Date: {self.date}, Winner: {self.winner})"
