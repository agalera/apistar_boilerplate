import functools

from apistar.exceptions import HTTPException
from apistar import http, Component
from models.users import UserModel


def authenticate_user(authorization: http.Header):
    if authorization is None:
        raise HTTPException({'authorization': 'forbidden'}, 403)

    token = authorization.split()[1]
    try:
        return UserModel.objects.get(token=token)
    except:
        raise HTTPException({'authorization': 'forbidden'}, 403)

component_auth = Component(UserModel, init=authenticate_user)
