class Config:
    TESTING = False

class TestConfig(Config):
    TESTING=True

class DevConfig(Config):
    DEBUG=True
    MYSQL_CURSORCLASS= "DictCursor"
    MYSQL_USER="root"
    MYSQL_PASSWORD=	"root"
    MYSQL_DB="db24centromedico"


class ProdConfig(Config):
    DEBUG=False
    MYSQL_CURSORCLASS= "DictCursor"
    MYSQL_USER="root"
    MYSQL_PASSWORD=	"root"
    MYSQL_DB="db24centromedico"


class configDict :{
    'development': DevConfig
    'testing' : TestConfig
    'production' : ProdConfig
    'default' : DevConfig
}