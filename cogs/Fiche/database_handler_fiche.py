import os
import sqlite3


class db_handler_fiche:
    def __init__(self, database_name: str):
        self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
        self.con.row_factory = sqlite3.Row

    def create(self, member_name, member_id, nom, nbr_lunes, clan, grade, pere, mere, freres, soeurs, partenaire,
               chatons, fourrure, yeux, carrure, aime, deteste, qualites, defauts, histoire, image_credit):
        cursor = self.con.cursor()
        query = "INSERT INTO Fiches (member_name, member_id, nom, nbr_lunes, clan, grade, pere, mere, freres, " \
                "soeurs, partenaire, chatons, fourrure, yeux, carrure, aime, deteste, qualites, defauts, " \
                "histoire, image_credit) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(query, (member_name, member_id, nom, nbr_lunes, clan, grade, pere, mere, freres, soeurs,
                               partenaire, chatons, fourrure, yeux, carrure, aime, deteste, qualites, defauts,
                               histoire, image_credit))
        cursor.close()
        self.con.commit()
