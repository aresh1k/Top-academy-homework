from faker import Faker
from db import create_db, Session
from tournaments import Tournament
from participants import Participant
from teammates import Teammate


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    tournaments_titles = ['Cybermos 1', 'Cybermos 2', 'Cyberpiter 1', 'Cyberpiter 2']

    team1 = Participant(team_name="Team 1")
    team2 = Participant(team_name="Team 2")
    session.add(team1)
    session.add(team2)

    faker = Faker("ru_RU")
    team_list = [team1, team2]

    for key, it in enumerate(tournaments_titles):
        tournament = Tournament(name=it, date='01.05.2023', winner=faker.random.choice(team_list).team_name)
        tournament.participants.append(team1)
        if key % 2 == 0:
            tournament.participants.append(team2)
        session.add(tournament)

    session.commit()

    for _ in range(50):
        nickname = faker.name()
        team = faker.random.choice(team_list)
        teammate = Teammate(nickname, team.id)
        session.add(teammate)

    session.commit()
    session.close()
