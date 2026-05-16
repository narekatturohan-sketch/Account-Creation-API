import oracledb
from threading import Lock

class ConnectionPool:
    pool = None
    lock = Lock()

    @classmethod
    def initialize(cls):
        with cls.lock:
            if cls.pool is None:
                cls.pool  = oracledb.create_pool(
                    user="Prodn",
                    password="Prodn0123#",
                    dsn = "localhost:1521/FREEPDB1",
                    min = 5,
                    max = 20,
                    increment = 5,
                    threaded = True
                )

                print("Connection pool created successfully.")
    
    @classmethod
    def get_connection(cls):
        if cls.pool is None:
            cls.initialize()
        return cls.pool.acquire()
    
    @classmethod
    def release_connection(cls, connection):
        if cls.pool is not None:
            cls.pool.release(connection)