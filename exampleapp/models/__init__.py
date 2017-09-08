from settings import MONGODB

from mongoengine import connect, ValidationError
from mongoengine.base.document import BaseDocument
from apistar.exceptions import ValidationError as HTTPError
from apistar import typesystem


print("connect db", MONGODB)
DB = connect(**MONGODB)

def validate(self, *args, **kwargs):
    try:
        print("validate")
        self.validate_original(*args, **kwargs)
    except ValidationError as ex:
        raise HTTPError(ex.to_dict(), 400)


# MONKEYPACHING
def to_dict(self):
    return dict(self.to_mongo())

def to_view(self):
    return self.c(self.to_dict())

def serializer(values):
    return type('Clean', (typesystem.Object,), {'properties': values})

BaseDocument.validate_original = BaseDocument.validate
BaseDocument.validate = validate
BaseDocument.serializer = serializer
BaseDocument.to_dict = to_dict
BaseDocument.to_view = to_view

print("inyect validation")
