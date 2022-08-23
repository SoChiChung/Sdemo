import mongo_config as config
import pymongo


mongo_url = "mongodb://{0}:{1}@{2}:{3}/".format(
    config.DB_TEST_USER,
    config.DB_TEST_PASSWORD,
    config.DB_TEST_HOST,
    config.DB_TEST_PORT,
)


class Myconnection:
    def __init__(self):
        global mongo_url
        self.client = pymongo.MongoClient(mongo_url)

    def getClient(self):
        return self.client
