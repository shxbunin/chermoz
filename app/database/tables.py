import datetime

from sqlalchemy import String, func, create_engine, MetaData, event, select, ForeignKey
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
    username: Mapped[str] = mapped_column(String(255), unique=True)
    mail: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str]
    admin: Mapped[bool]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), onupdate=datetime.datetime.now)

class Photos(Base):
    __tablename__ = 'photos'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    album_id: Mapped[int] = mapped_column(ForeignKey('albums.id'))
    section_id: Mapped[int] = mapped_column(ForeignKey('sections.id'))
    path: Mapped[str] = mapped_column(String(255), unique=True)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

class Sections(Base):
    __tablename__ = 'sections'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    description: Mapped[str] = mapped_column(String(255))
    cover_path: Mapped[str] = mapped_column(String(255), default="https://chermoz.storage.yandexcloud.net/gallery/cover.jpg")
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), onupdate=datetime.datetime.now)

class Albums(Base):
    __tablename__ = 'albums'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    number: Mapped[int]
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    section_id: Mapped[int] = mapped_column(ForeignKey('sections.id'))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), onupdate=datetime.datetime.now)


@event.listens_for(Albums, 'before_insert')
def set_album_number(mapper, connection, target):
    stmt = select(func.count(Albums.id)).where(Albums.section_id == target.section_id)
    count = connection.execute(stmt).scalar()
    target.number = count + 1