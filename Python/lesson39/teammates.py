from sqlalchemy import Column, Integer, String, ForeignKey
from db import Base


class Teammate(Base):
    __tablename__ = 'teammates'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(250), nullable=False)
    team = Column(Integer, ForeignKey('participants.id'))

    def __init__(self, nickname, team):
        self.nickname = nickname
        self.team = team

    def __repr__(self):
        return f"Teammate (nickname: {self.nickname}, team_ID: {self.team})"
