from typing import Optional, List

import strawberry


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
        return City(id=self.id, name=f"Город {self.id}")


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)

    @strawberry.field(description="Информация о сотруднике")
    def staff(self, id: strawberry.ID) -> Staff:
        return Staff(id=id, name=f'Сотрудник {id}')

    @strawberry.field(description="Список сотрудников", name="staffList")
    def staff_list(self) -> List[Staff]:
        return [Staff(id=id, name=f"Сотрудник {id}") for id in range(10)]


schema = strawberry.Schema(query=Query)
