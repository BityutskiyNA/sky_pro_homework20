from unittest.mock import MagicMock

import pytest as pytest
from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    Dir1 = Director(id=1, name="Тейлор Шеридан")
    Dir2 = Director(id=2, name="Квентин Тарантино")
    Dir3 = Director(id=3, name="Владимир Вайншток")
    Dir4 = Director(id=4, name="Декстер Флетчер")


    director_dao.get_one = MagicMock(return_value=Dir1)
    director_dao.get_all = MagicMock(return_value=[Dir1, Dir2, Dir3, Dir4])
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    director_dao.create = MagicMock(return_value=Director(id=5))

    return director_dao


class TestDirectorServise:
    @pytest.fixture(autouse=True)
    def director_service(self,director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        director = self.director_service.get_all()

        assert len(director) > 0

    def test_create(self):
        director_d = {"id": "9",
                      "name": "Тейлор Шеридан",
                      }

        director = self.director_service.create(director_d)

        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_d = {"id": "9",
                      "name": "Тейлор Шеридан",
                      }
        self.director_service.update(director_d)