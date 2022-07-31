import json
import os
import sqlite3
from utils.logger.logger import Logger


class SQLiteManager:
    checkout_dir = os.environ.get("checkout_dir", "/Users/mac/projects")
    __DB_path = os.environ.get("SQLITE_DB_PATH", f"{checkout_dir}/brew/brew.db")
    __create_table_query = "CREATE TABLE IF NOT EXISTS tests_results (Run_Number INT PRIMARY KEY AUTOINCREMENT, " \
                           "Passed INT, Failed INT, Skipped INT);"
    __tests_results_dir = f"{checkout_dir}/brew/tests/allure_reports"

    @staticmethod
    def __get_connection():
        """it will connect to existing database or will create the new one if not exist"""
        try:
            conn = sqlite3.connect(SQLiteManager.__DB_path)
            return conn
        except TypeError as ex:
            Logger.utils_logger.critical("Exception while open SqliteDB connect", ex)
            conn.close()
            raise ex

    @staticmethod
    def __execute_returning_query(query: str) -> list:
        """each row from received table writing in a list"""
        row_list = []
        try:
            cursor = None
            conn = SQLiteManager.__get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            for row in cursor.fetchall():
                row_list.append(row)
        except TypeError as ex:
            Logger.utils_logger.error("Exception while execute Sqlite query", ex)
        finally:
            if cursor is not None:
                cursor.close()
            conn.close()
            return row_list

    @staticmethod
    def create_table_if_not_exist():
        """Creating table with results if not exist"""
        SQLiteManager.__execute_returning_query(SQLiteManager.__create_table_query)

    @staticmethod
    def get_tests_results_files():
        """Go to allure_results directory and get files with tests results (which contains result.json)"""
        _files = []
        for r, d, f in os.walk(SQLiteManager.__tests_results_dir):
            for _file in f:
                if "result.json" in _file:
                    _files.append(os.path.join(r, _file))
        return _files

    @staticmethod
    def parse_test_results_and_insert():
        """parsing results files and counting passed, failed and skipped tests"""
        try:
            _passed = 0
            _failed = 0
            _skipped = 0
            result_files = SQLiteManager.get_tests_results_files()
            for _file in result_files:
                with open(_file) as f:
                    _result = json.load(f)
                    if _result["status"] == "passed":
                        _passed += 1
                    elif _result["status"] == "failed":
                        _failed += 1
                    elif _result["status"] == "skipped":
                        _skipped += 1
            insert_query = f"INSERT INTO tests_results (Passed, Failed, Skipped) VALUES({_passed}, {_failed}, " \
                           f"{_skipped});"
            SQLiteManager.__execute_returning_query(insert_query)
        except Exception:
            Logger.utils_logger.exception("Exception")


if __name__ == "__main__":
    SQLiteManager.create_table_if_not_exist()
    SQLiteManager.parse_test_results_and_insert()
