# why db ? 
    # when you reload the page the data that we created will be vanished so we need to store our data
# creating a DataBase allows user to save their data
# ORM - OBJECT RELATIONAL MAPPING(sqlalchemy)
# allows you to write sql,nosql queries in python itself
# so we can write create data,retrive data,define data

# so ORM we are going to use sqlalchemy 

from collections.abc import AsyncGenerator
import uuid

from sqlalchemy import create_engine
from sqlalchemy import Column,Text,String,DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime


DATABSE_URL =  "sqlite+aiosqlite:///./test.db"

# creating a structure of a DATA or creating a DATAMODEL


class Base(DeclarativeBase):
    pass
class Post(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    caption = Column(Text)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


engine = create_async_engine(DATABSE_URL)
async_session_maker = async_sessionmaker(engine,expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session