import pytest

from app.app import app


@pytest.fixture()
def client():
    app.config.update(TESTING=True)

    with app.test_client() as test_client:
        yield test_client


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_greet_valid_name(client):
    response = client.post(
        "/greet",
        json={"name": "Tanvir"},
    )

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Tanvir!"}


def test_greet_rejects_non_json(client):
    response = client.post(
        "/greet",
        data="name=Tanvir",
    )

    assert response.status_code == 415


def test_greet_rejects_non_object_json(client):
    response = client.post(
        "/greet",
        json=["wrong", "shape"],
    )

    assert response.status_code == 400


@pytest.mark.parametrize(
    "name",
    ["", "   ", "x" * 81, None, 123],
)
def test_greet_rejects_bad_name(client, name):
    response = client.post("/greet", json={"name": name})

    assert response.status_code == 400
