
from favorite_document import FavoriteDocument

def test_favorite_document_entity_init():
    favorite_document = FavoriteDocument("Top musical", "Martin Stein",
                                         "Lorem Ipsum is simply dummy text of the printing and typesetting industry.")

    assert favorite_document.title == "Top musical"
    assert favorite_document.author == "Martin Stein"
    assert favorite_document.description == "Lorem Ipsum is simply dummy text of the printing and typesetting industry."


def test_favorite_document_validate_type_data():
    favorite_document = FavoriteDocument("Top musical", "Martin Stein",
                                         "Lorem Ipsum is simply dummy text of the printing and typesetting industry.")

    assert type(favorite_document.title) is str
    assert type(favorite_document.author) is str
    assert type(favorite_document.description) is str