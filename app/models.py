from peewee import *
from app.config import MAIN_DIR
from datetime import datetime

db = SqliteDatabase(f"{MAIN_DIR}/db.sqlite3")


class User(Model):
    id = PrimaryKeyField(unique=True, null=False)
    user_id = IntegerField(null=False)
    first_name = CharField(null=False, max_length=64)
    username = CharField(null=True, max_length=64)
    is_admin = BooleanField(default=False)
    created = DateTimeField(default=datetime.now())

    class Meta:
        database = db

    def add_user(self, user_id, username, first_name):
        """
        Функция для добавления пользователя в Базу данных
        :param first_name:
        :param user_id:
        :param username:
        :return:
        """
        self.create(user_id=user_id, username=username,
                    first_name=first_name)
        return True

    def check_user(self, user_id):
        """
        Функция для проверки наличия пользователя в Базе Данных
        :param user_id:
        :return: Булевое значения True если пользователь найден
        """
        res = self.get_or_none(User.user_id == user_id)
        if res:
            return True
        return False


User.create_table()
