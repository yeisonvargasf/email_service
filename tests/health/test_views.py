from flask import url_for


def test_health_check_passes(test_client):
    response = test_client.get(url_for("health.health_check"))

    assert response.status_code == 200
    assert response.json.get("status") == "ok"
