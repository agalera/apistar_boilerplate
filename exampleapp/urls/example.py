from views.example import welcome

from apistar import Include, Route


routes = [
    Route('/', 'GET', welcome),
]