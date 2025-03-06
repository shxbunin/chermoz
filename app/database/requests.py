from database.tables import local_session, Users, Photos, Sections, Albums
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

def add_photo(path):
    with local_session() as session:
        session.add(Photos(path=path))
        session.commit()

def add_section(name, description):
    with local_session() as session:
        session.add(Sections(name=name, description=description))
        session.commit()

def get_sections():
    with local_session() as session:
        return session.query(Sections).all()

def add_album(section_id):
    with local_session() as session:
        session.add(Albums(section_id=section_id))
        session.commit()
def get_albums_by_section(section_id):
    with local_session() as session:
        return session.query(Albums).filter_by(section_id=section_id).all()

def add_photo_in_album(album_id, path):
    with local_session() as session:
        session.add(Photos(album_id=album_id, path=path))
        session.commit()
def get_photos_by_albums(album_id):
    with local_session() as session:
        return session.query(Photos).filter_by(album_id=album_id).all()