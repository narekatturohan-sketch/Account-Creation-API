import logging
from common.db.db_manager import DBManager

logger = logging.getLogger(__name__)

class TransactionManager:
    """
    Enterprise Transaction Manager
    Handles:
    - Connection acquisition
    - Commit / rollback
    - Safe cleanup
    - Transaction lifecycle management
    """

    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = DBManager.get_connection()
        logger.info("Database transaction started")
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            if exc_type is None:
                self.connection.commit()
                logger.info("Transaction committed successfully")
            else:
                self.connection.rollback()
                logger.error(
                    f"Transaction rolled back due to error: {exc_value}"
                )
        except Exception as transaction_error:
            logger.exception(
                f"Transaction handling failed: {transaction_error}"
            )
        finally:
            if self.connection:
                DBManager.close_connection(self.connection)
                logger.info("Database connection released")


class TransactionService:
    """
    Optional Helper Service
    Useful for manual transaction handling
    without context manager syntax.
    """

    @staticmethod
    def begin():
        connection = DBManager.get_connection()
        logger.info("Manual transaction started")
        return connection
    
    @staticmethod
    def commit(connection):
        try:
            connection.commit()
            logger.info("Manual transaction committed")
        except Exception as e:
            logger.exception(f"Commit failed: {e}")
            raise
        finally:
            DBManager.close_connection(connection)

    @staticmethod
    def rollback(connection):
        try:
            connection.rollback()
            logger.warning("Manual transaction rolled back")
        except Exception as e:
            logger.exception(f"Rollback failed: {e}")
            raise
        finally:
            DBManager.close_connection(connection)