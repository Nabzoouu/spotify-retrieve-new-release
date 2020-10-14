class Config(object):
    DEBUG = False
    TESTING = False
    TYPE_OF_DATABASE = "postgresql" 

class ProductionConfig(Config):
    APP_HOST="0.0.0.0"
    APP_PORT="3000"
    DATABASE_HOST="172.17.0.2"
    DATABASE_PORT="5432"
    DATABASE_NAME="new-release-prod"
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_HOST="172.17.0.5"
    DATABASE_PORT="5432"
    DATABASE_NAME="new-release"
    APP_HOST="127.0.0.1"
    APP_PORT="3000"