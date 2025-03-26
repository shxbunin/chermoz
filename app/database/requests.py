from collections import defaultdict

from database.tables import local_session, Users, Photos, Sections, Albums, Essays
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

def add_photo(path, album_id, section_id, description):
    with local_session() as session:
        if session.query(Photos).filter_by(section_id=section_id).count() == 0:
            section = session.query(Sections).filter_by(id=section_id).first()
            section.cover_path = path
        session.add(Photos(path=path, album_id=album_id, section_id=section_id, description=description))
        session.commit()

def add_section(name, description):
    with local_session() as session:
        session.add(Sections(name=name, description=description))
        session.commit()

def get_sections():
    with local_session() as session:
        return session.query(Sections).all()

def add_album(section_id, name, description):
    with local_session() as session:
        session.add(Albums(section_id=section_id, name=name, description=description))
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

def get_photos_by_section(section_id):
    with local_session() as session:
        photos = session.query(Photos).filter_by(section_id=section_id).all()
        album_dict = defaultdict(list)
        for photo in photos:
            print(photo)
            album_dict[photo.album_id].append(photo)
        return album_dict

def get_recent_photos():
    with local_session() as session:
        return session.query(Photos).order_by(Photos.created_at.desc()).limit(10).all()

def get_photo_by_id(id):
    with local_session() as session:
        return session.query(Photos).filter_by(id=id).first()

def change_album_cover(photo_id):
    with local_session() as session:
        photo = session.query(Photos).filter_by(id=photo_id).first()
        section = session.query(Sections).filter_by(id=photo.section_id).first()
        section.cover_path = photo.path
        session.commit()

def delete_photo_db(photo_id):
    with local_session() as session:
        photo = session.query(Photos).filter_by(id=photo_id).first()
        section = session.query(Sections).filter_by(id=photo.section_id).first()
        if photo:
            if section.cover_path == photo.path:
                section.cover_path = "https://chermoz.storage.yandexcloud.net/gallery/cover.jpg"
            session.delete(photo)
            session.commit()

def edit_photo_desc(photo_id, description):
    with local_session() as session:
        photo = session.query(Photos).filter_by(id=photo_id).first()
        photo.description = description
        session.commit()

def add_essay(path, name, description):
    with local_session() as session:
        session.add(Essays(path=path, name=name, description=description))
        session.commit()

def get_essays():
    with local_session() as session:
        return session.query(Essays).all()