import pytest
import run

# СТВОРЮЄМ ФІКСТУРУ ДЛЯ ТЕСТУВАННЯ ВСІХ В'ЮШОК
@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()


class TestMain:
    def test_root_status(self, test_client):
        """Перевіряєм статус код"""
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, 'Сттатус код всіх постів неправильний'


    def test_root_content(self, test_client):
        response = test_client.get('/', follow_redirects=True)
        assert "Головна сторінка" in response.data.decoe("utf-8"), "помика у контенті"

