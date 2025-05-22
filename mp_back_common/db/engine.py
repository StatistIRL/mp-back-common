from settings import DatabaseSettings, get_settings
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

settings: DatabaseSettings = get_settings(DatabaseSettings)

engine = create_async_engine(url=settings.url)

async_session_factory = async_sessionmaker(bind=engine)
