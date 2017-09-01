from models.example import ExampleModel
from modules.auth import UserModel as User


def welcome(user: User, name):
    return {'hello': user.username}

def test_orm_exception(token: User):
    ExampleModel(title="asdasd").save()
