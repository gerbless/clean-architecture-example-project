from sqlalchemy import Table, MetaData, Column, Integer, String, LargeBinary, Sequence, Boolean
from sqlalchemy.orm import mapper, relationship

from entities.user.user import User
#from entities.favorite_document import FavoriteDocument

def user_mapping(metadata: MetaData):
    user = Table(
        'users',
        metadata,
        Column('id', Integer, Sequence('users_id_seq'), nullable=False, primary_key=True),
        Column('first_name', String(50)),
        Column('last_name', String(50)),
        Column('email', String(50), unique=True)
    )
    mapper(User, user)
    #mapper(User, user, properties={
    #    'favorite_document': relationship(FavoriteDocument, backref='user', order_by=user.c.id),
    #})
    return user
