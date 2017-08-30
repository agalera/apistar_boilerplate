from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls


routes = [
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]