from views.example import welcome, test_orm_exception

from apistar import Include, Route


routes = [
    Route('/', 'GET', welcome),
    Route('/test_orm', 'GET', test_orm_exception),
]