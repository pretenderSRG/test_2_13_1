class VacanciesTest:
    def test_all_status(self, test_client):
        """перевіряєм чи повертає статус 200 при виборі всіх вакансій"""
        response = test_client.get('/vacancies', follow_redirect=True)
        assert response.status_code == 200, "Статус код всіх вакансій неправильний"

    def test_single_status(self, test_client):
        response = test_client.get('vacancies/1', follow_redirect=True)
        assert response.status_code == 200, "Статус код ля вакансії 1 непраильний"