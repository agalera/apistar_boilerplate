from mongoengine import Document, StringField
from apistar import typesystem


class UserModel(Document):
    serializer = Document.serializer(
        {'title': typesystem.string()}
    )
    username = StringField(required=True, max_length=100)
    token = StringField(required=True, max_length=100)
