from models.example import ExampleModel
from modules.auth import UserModel as User
import typing


def welcome(user: User):
    return {'welcome': user.to_view()}

def test_orm_exception():
    t = ExampleModel(title="asdasd")
    t.save()

def test_doc(user: User.serializer) -> typing.List[User.serializer]:
    return [User.serializer({'name': str(x),
                             'other': 'stuff'}) for x in range(10)]