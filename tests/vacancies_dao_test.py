import pytest
from app.vacancies.dao.vacancies_dao import VacanciesDAO


key_should_be = {"pk", "company", "position", "salary"}

@pytest.fixture()
def vacancies_dao():
    vacancies_dao_instance = VacanciesDAO("./data/vacancies.json")
    return vacancies_dao_instance


class TestVacanciesDAO:
    def test_get_all(self, vacancies_dao):
        vacancies = vacancies_dao.get_all()
        assert type(vacancies) == list, "Повертає неправильний тип даних"
        assert len(vacancies) > 0, "Помилка в кідькості кандадатів"
        assert set(vacancies[0].keys()) == key_should_be, "помилка в ключах"

    def test_get_by_pk(self, vacancies_dao):
        vacancy = vacancies_dao.get_by_pk(1)
        assert vacancy["pk"] == 1
        assert type(vacancy) == dict
        assert set(vacancy.keys()) == key_should_be

    