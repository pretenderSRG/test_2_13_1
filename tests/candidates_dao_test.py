import pytest
from app.candidates.dao.candidate_dao import CandidateDAO


@pytest.fixture()
def candidates_dao():
    candidates_dao_instance = CandidateDAO("./data/candidates.json")
    return candidates_dao_instance


keys_should_be = {"pk", "name", "position"}


class TestCandidateDAO:
    def test_get_all(self, candidates_dao):
        """Перевірка чи правильний список повертає"""
        candidates = candidates_dao.get_all()
        assert type(candidates) == list, "Не повертає список"
        assert len(candidates) > 0, "Порожній список кандидатів"
        assert set(candidates[0].keys) == keys_should_be

    def test_get_by_pk(self, candidates_dao):
        """Пкревіряємо чи повертає правильного кандидата"""
        candidates = candidates_dao.get_by_pk(1)
        assert candidates["pk"] == 1, "повертає неправильного кандидата"
        assert set(candidates[0].keys) == keys_should_be

