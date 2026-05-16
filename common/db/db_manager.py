from common.db.connection_pool import ConnectionPool 

class DBManager:
    @staticmethod
    def get_connection():
        return ConnectionPool.get_connection()
    
    @staticmethod
    def close_connection(connection):
        ConnectionPool.release_connection(connection)