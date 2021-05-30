import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '2001'
    SQLALCHEMY_DATABASE_URI = 'postgres://lptzfenupmbzuj:33302222e95e7355014d650f5a4e264a4c2431fe668d7a33842539a4f081f209@ec2-35-174-35-242.compute-1.amazonaws.com:5432/dcvic7e9ur27ku'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True