from http import HTTPStatus

from fastapi.testclient import TestClient

from learn_fastapi.app import app


def test_root_must_return_ok_and_ola_lucasschilin():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá @lucasschilin, olá Mundo! 🌎'}
