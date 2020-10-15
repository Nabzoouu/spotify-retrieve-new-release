class Config(object):
    DEBUG = False
    TYPE_OF_DATABASE = "postgresql"
    DELTA_JOURS = 30 #Sort tout les album étant sortis depuis la veille. Si il était indéxé à 2, se serait le nombre de jours depuis l'avant veille, etc...

class ProductionConfig(Config):
    APP_HOST="0.0.0.0"
    APP_PORT="3000"
    DATABASE_HOST="172.17.0.4"
    DATABASE_PORT="5432"
    DATABASE_NAME="new-release-prod"
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_HOST="172.17.0.3"
    DATABASE_PORT="5432"
    DATABASE_NAME="new-release"
    APP_HOST="0.0.0.0"
    APP_PORT="3000"