from views.example import welcome, test_orm_exception, test_doc

from apistar import Include, Route


routes = [
    Route('/welcome', 'GET', welcome),
    Route('/test_orm', 'POST', test_orm_exception),
    Route('/test_doc', 'POST', test_doc)
]