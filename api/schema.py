from typing import Optional, List

import strawberry

from models.database import Session
from models.models import Staff as ModelStaff, City as ModelCity
from sqlalchemy import select


@strawberry.type
class City:
    id: strawberry.ID
    name: Optional[str]


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Staff:
    id: strawberry.ID
    name: str
    city: Optional[City]

    @strawberry.field
    def city(self) -> City:
        stmt = select(ModelCity).where(ModelCity.id == self.city_id)
        city = Session().scalars(stmt).one()
        return city


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)

    @strawberry.field(description="Информация о сотруднике")
    def staff(self, id: strawberry.ID) -> Staff:
        stmt = select(ModelStaff).where(ModelStaff.id == id)
        staff = Session().scalars(stmt).one()
        return staff

    @strawberry.field(description="Список сотрудников", name="staffList")
    def staff_list(self) -> List[Staff]:
        stmt = select(ModelStaff)
        staff_list = Session().scalars(stmt)
        return staff_list

    @strawberry.field(description="Список городов", name="cityList")
    def city_list(self) -> List[City]:
        stmt = select(ModelCity)
        city_list = Session().scalars(stmt)
        return city_list


schema = strawberry.Schema(query=Query)
