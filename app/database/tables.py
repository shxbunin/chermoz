import datetime

from sqlalchemy import String, func, create_engine, MetaData, event, select, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from config import settings


engine = create_engine(url=settings.DATABASE_URL, echo=True, pool_pre_ping=True)
local_session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass

def create_tables():
    Base.metadata.create_all(engine)

#-------------------------------------------Таблицы-------------------------------------------
class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    mail: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    admin: Mapped[bool] = mapped_column(default=False, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), onupdate=datetime.datetime.now, nullable=False)

class Photos(Base):
    __tablename__ = 'photos'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    album_id: Mapped[int] = mapped_column(ForeignKey('albums.id'), nullable=False)
    section_id: Mapped[int] = mapped_column(ForeignKey('sections.id'), nullable=False)
    path: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), nullable=False)


class Essays(Base):
    __tablename__ = 'essays'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    path: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), nullable=False)


class Comments(Base):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey('comments.id'))
    photo_id: Mapped[int] = mapped_column(ForeignKey('photos.id'), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), nullable=False)

class Sections(Base):
    __tablename__ = 'sections'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    cover_path: Mapped[str] = mapped_column(String(255), default="https://chermoz.storage.yandexcloud.net/gallery/cover.jpg", nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), onupdate=datetime.datetime.now, nullable=False)

class Albums(Base):
    __tablename__ = 'albums'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    number: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    section_id: Mapped[int] = mapped_column(ForeignKey('sections.id'), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), onupdate=datetime.datetime.now, nullable=False)


@event.listens_for(Albums, 'before_insert')
def set_album_number(mapper, connection, target):
    stmt = select(func.count(Albums.id)).where(Albums.section_id == target.section_id)
    count = connection.execute(stmt).scalar()
    target.number = count + 1