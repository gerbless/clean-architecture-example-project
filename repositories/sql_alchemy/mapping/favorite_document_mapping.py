from sqlalchemy import Table, MetaData, Column, Integer, String, Text, Float, ForeignKey, Sequence
from sqlalchemy.orm import mapper

from entities.favorite_document.favorite_document import FavoriteDocument


def favorite_document_mapping(metadata: MetaData):
    favorite_document = Table(
        'favorites_document',
        metadata,
        Column('id', Integer, Sequence('favorites_document_id_seq'), primary_key=True, nullable=False),
        Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
        Column('title', String(150)),
        Column('author', String(120)),
        Column('description', Text),
    )

    mapper(FavoriteDocument, favorite_document)

    return favorite_document
