from os import environ


MONGODB = {'host': environ.get('MONGODB',
                                'localhost').split(','),
           'db': 'pruebitas'}
