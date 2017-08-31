from models.example import ExampleModel


def welcome():
    return {'hello': 'worldz', 'example_count': ExampleModel.objects.count()}

def test_orm_exception():
    ExampleModel(title="asdasd").save()
