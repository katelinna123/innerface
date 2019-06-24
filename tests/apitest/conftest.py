import pytest

from utils.db import LongTengServer

@pytest.fixture(scope="session")
def db():
    db = LongTengServer()
    yield db
    db.close()