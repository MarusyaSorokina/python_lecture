import sqlite3
import time
import math
from flask import url_for


class FDataB:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM menu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка при чтении БД")
        return []

    def add_post(self, title, text, url, tims):
        try:
            self.__cur.execute("SELECT COUNT() as 'count' "
                               "FROM posts WHERE url LIKE ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Такой url уже существует")
                return False
            tim = math.floor(tims.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?,?,?,?)",
                               (title, text, url, tim))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка при добавлении статьи в БД"+str(e))
            return False
        return True

    def get_post_anonce(self):
        try:
            self.__cur.execute("SELECT id, title, text, url"
                               "FROM posts ORDER BY tims DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД" + str(e))

        return []


