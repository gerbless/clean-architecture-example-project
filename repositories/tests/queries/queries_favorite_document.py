from entities.favorite_document import FavoriteDocument
from repositories.sql_alchemy.favorite_document_repository_sql_alchemy import FavoriteDocumentRepositorySqlAlchemy


def get_favorite_document_all(db):
    favorite_document_repository = FavoriteDocumentRepositorySqlAlchemy(db)
    return favorite_document_repository.get_all()


def get_favorite_document_by_id(db, uid: int):
    favorite_document_repository = FavoriteDocumentRepositorySqlAlchemy(db)
    return favorite_document_repository.get_id(uid=uid)


def create_favorite_document(db, user_id: int):
    favorite_document_repository = FavoriteDocumentRepositorySqlAlchemy(db)
    favorite_document_initial = FavoriteDocument("Top musical", "Martin Stein",
                                                 "Lorem Ipsum is simply dummy text of the printing and typesetting industry.", user_id)
    favorite_document_repository.add(favorite_document_initial)
    return get_favorite_document_all(db)


def delete_favorite_document(db, uid: int):
    favorite_document_repository = FavoriteDocumentRepositorySqlAlchemy(db)
    return favorite_document_repository.delete(uid=uid)
