import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '2001'
    SQLALCHEMY_DATABASE_URI = 'postgres://fdcdeuozoifpje:ebfab39c4ee0381543e77981369698f533e2607d322ee495a04a5c62ebe6abc8@ec2-35-174-35-242.compute-1.amazonaws.com:5432/d1ruejc17i3vba'


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
