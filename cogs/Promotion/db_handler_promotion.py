import os
import sqlite3


class db_handler_promote:
    def __init__(self, database_name: str):
        self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
        self.con.row_factory = sqlite3.Row

    def promote(self, grade: str, member_name, member_id: int):
        cursor = self.con.cursor()
        query = "UPDATE Fiches SET grade = ? WHERE member_name = ? and member_id = ?;"
        cursor.execute(query, (grade, member_name, member_id))
        cursor.close()
        self.con.commit()
