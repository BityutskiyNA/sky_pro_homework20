from unittest.mock import MagicMock

import pytest as pytest
from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name="Комедия")
    genre_2 = Genre(id=2, name="Семейный")
    genre_3 = Genre(id=3, name="Фэнтези")
    genre_4 = Genre(id=4, name="Драма")


    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3, genre_4])
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    genre_dao.create = MagicMock(return_value=Genre(id=5))
    genre_dao.partially_update = MagicMock()

    return genre_dao


class TestGenreServise:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genre = self.genre_service.get_all()

        assert len(genre) == 4

    def test_create(self):
        genre_d = {"id": "9",
                      "name": "Драма",
                      }

        director = self.genre_service.create(genre_d)

        assert director.id is not None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_d = {"id": "9",
                      "name": "Драма",
                      }
        self.genre_service.update(genre_d)

    def test_partially_update(self):
        genre_d = {"id": "9",
                      "name": "Драма",
                      }
        self.genre_service.update(genre_d)