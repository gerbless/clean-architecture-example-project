import pytest
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import clear_mappers


from app import create_app
from repositories.sql_alchemy.mapping.user_mapping import user_mapping
from repositories.sql_alchemy.mapping.favorite_document_mapping import favorite_document_mapping

@pytest.fixture
def db():
    db, metadata = init()
    mapping_tables(metadata=metadata)
    metadata.create_all()
    yield db
    db.session.commit()
    destroy_tables(metadata=metadata)

@pytest.fixture(scope="session")
def db_session():
    db, metadata = init()
    mapping_tables(metadata=metadata)
    metadata.create_all()
    yield db
    truncate_tables(metadata=metadata, connection=db.engine.connect())
    db.session.commit()
    destroy_tables(metadata=metadata)

def init():
    app = create_app(modules=[])
    app.config['TESTING'] = True
    db = SQLAlchemy(app)
    metadata = MetaData(db.engine)
    return db, metadata

def mapping_tables(metadata: MetaData):
    try:
        clear_mappers()
        user_mapping(metadata)
    except Exception as e:
        print(e)

def truncate_tables(metadata, connection):
    for table in reversed(metadata.sorted_tables):
        connection.execute(table.delete())

def destroy_tables(metadata):
    metadata.reflect()
    metadata.drop_all()