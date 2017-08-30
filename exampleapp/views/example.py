from models.example import ExampleModel


def welcome():
    return {'hello': 'world', 'example_count': ExampleModel.objects.count()}
