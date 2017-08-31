from settings import MONGODB

from apistar.exceptions import ValidationError as HTTPError
from mongoengine import connect, ValidationError
from mongoengine.base.document import BaseDocument

print("connect db", MONGODB)
DB = connect(**MONGODB)

BaseDocument.validate_original = BaseDocument.validate
def validate(self, *args, **kwargs):
    try:
        print("validate")
        self.validate_original(*args, **kwargs)
    except ValidationError as ex:
        raise HTTPError(ex.to_dict(), 400)

BaseDocument.validate = validate
print("inyect validation")
