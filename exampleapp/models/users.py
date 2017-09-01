from mongoengine import Document, StringField


class UserModel(Document):
    username = StringField(required=True, max_length=100)
    token = StringField(required=True, max_length=100)
