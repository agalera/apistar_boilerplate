from mongoengine import Document, StringField


class ExampleModel(Document):
    title = StringField(required=True, max_length=200)
