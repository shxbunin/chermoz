from database.requests import *
from flask_login import UserMixin

class UserLogin(UserMixin):
    def __init__(self):
        self.admin = False
        self.username = None

    def fromDB(self, user_id):
        self.__user = get_user_by_id(user_id)
        self.admin = self.__user.admin
        self.username = self.__user.username
        return self

    def create(self, user):
        self.__user = user
        return self

    def get_username(self):
        return self.__user.username
    def get_id(self):
        return str(self.__user.id)

    def get_user(self):
        return self.__user

