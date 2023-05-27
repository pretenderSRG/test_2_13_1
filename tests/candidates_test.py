class TestCandidates:
    """тестування кандадатів"""
    def test_all_candidates_status(self, test_client):
        """перевірка статус коду всіх кандидатів"""
        response = test_client.get('/candidates', follow_redirect=True)
        assert response.status_code == 200, "Помилка в статус коді запиту всіх кандидатів"

    def test_single_candidate_status(self, test_client):
        """перевірка статус коду одного кандидата"""
        response = test_client.get('/candudates/1', follow_redirect=True)
        assert response.status_code == 200, "Помилка в статус коді запиту кандидата 1"

