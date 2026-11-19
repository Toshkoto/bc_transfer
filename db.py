from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from collections.abc import Iterator

from .config import get_db_url

engine = create_engine(
    get_db_url(),
    pool_pre_ping=True,
    pool_recycle=1800,
    pool_size=5,
    max_overflow=5,
)

SessionFactory = sessionmaker(bind=engine, expire_on_commit=False)

@contextmanager
def session_scope() -> Iterator[Session]:
    session = SessionFactory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


"""
    contextmanager + func essence and purpose
    Generator Iterator, why replace Iterator
"""
