from mongoengine import Document, StringField
from apistar import typesystem


class ExampleModel(Document):
    serializer = Document.serializer(
        {'title': typesystem.string()}
    )
    title = StringField(required=True, max_length=2)
