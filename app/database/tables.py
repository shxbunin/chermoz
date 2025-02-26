import datetime
from sqlalchemy import String, func, create_engine, MetaData
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from config import settings


engine = create_engine(url=settings.DATABASE_URL, echo=True)
local_session = sessionmaker(engine)
metadata = MetaData()


class Base(DeclarativeBase):
    pass

def create_tables():
    metadata.create_all(engine)


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