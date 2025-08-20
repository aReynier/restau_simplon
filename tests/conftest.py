#Simuler un client d'API
import pytest
from app.schemas.categorie import CategorieCreate
from sqlmodel import Session, SQLModel, create_engine

@pytest.fixture(scope="session")
def engine():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    return engine

@pytest.fixture
def session(engine):
    with Session(engine) as session:
        yield session

@pytest.fixture
def categorie_fixture_create():
    return CategorieCreate(nom="test", description="ceci est un test")



