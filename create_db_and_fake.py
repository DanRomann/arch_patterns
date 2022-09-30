from faker import Faker

from models.database import create_db, Session
from models.models import City, Staff


def create_database(load_fake: bool = True):
    create_db()
    if not load_fake:
        _load_fake_data(Session())


def _load_fake_data(session: Session):

    faker = Faker("ru_RU")

    for _ in range(50):
        name = faker.city()
        city = City(name=name)
        session.add(city)

    for id in range(1, 5):
        name = faker.name()
        staff = Staff(name=name, city_id=id)
        session.add(staff)

    session.commit()
    session.close()
