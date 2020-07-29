from flask_sqlalchemy import SQLAlchemy
from injector import inject
from sqlalchemy.exc import IntegrityError

from entities.favorite_document.favorite_document import FavoriteDocument
from repositories.I_favorite_document_repository import IFavoriteDocumentRepository
from use_cases.exceptions import InvalidFavoriteDocumentException


class FavoriteDocumentRepositorySqlAlchemy(IFavoriteDocumentRepository):

    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def add(self, document: FavoriteDocument):
        try:
            self.db.session.add(document)
            self.db.session.commit()
        except IntegrityError:
            self.db.session.rollback()
            raise InvalidFavoriteDocumentException

    def get_id(self, uid: int):
        favorite_document = self.db.session.query(FavoriteDocument).get(uid)

        if favorite_document:
            return favorite_document

        raise InvalidFavoriteDocumentException

    def delete(self, uid: int):
        favorite_document = self.db.session.query(FavoriteDocument).get(uid)
        if favorite_document:
            self.db.session.delete(favorite_document)
            self.db.session.commit()
        else:
            raise InvalidFavoriteDocumentException

    def get_all(self):
        return self.db.session.query(FavoriteDocument).all()
