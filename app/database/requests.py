from database.tables import local_session, Users
from sqlalchemy import select

def get_user_by_id(user_id):
    with local_session() as session:
        user = session.scalar(select(Users).where(Users.id == user_id))
        if user:
            return user
        else:
            print("Пользователь не найден")
            return False

def get_user_by_email(email):
    with local_session() as session:
        user = session.scalar(select(Users).where(Users.mail == email))
        if user:
            return user
        else:
            print("Пользователь не найден")
            return False