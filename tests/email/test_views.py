from flask import url_for
from pytest import mark
from tests.conftest import test_data_correct
from tests.conftest import test_data_empty_body
from tests.conftest import test_data_incorrect_headers
from tests.conftest import test_data_invalid_body


@mark.parametrize("headers,request_body,response_code", test_data_incorrect_headers)
def test_email_api_fails_incorrect_headers(
    test_client, headers, request_body, response_code
):
    response = test_client.post(
        url_for("email.send_new_mail"), data=request_body, headers=headers
    )

    assert response.status_code == response_code


@mark.parametrize("request_body,url_key,response_code", test_data_empty_body)
def test_send_email_fails_empty_body(
    test_client, test_url_map, request_body, url_key, response_code
):
    response = test_client.post(
        test_url_map[url_key], json=request_body, headers={"Accept": "application/json"}
    )

    assert response.status_code == response_code
    assert response.json["status"] == "error"


@mark.parametrize("request_body,url_key,response_code", test_data_invalid_body)
def test_send_email_fails_validation_error(
    test_client, test_url_map, request_body, url_key, response_code
):
    response = test_client.post(
        test_url_map[url_key], json=request_body, headers={"Accept": "application/json"}
    )

    assert response.status_code == response_code
    assert response.json["status"] == "error"


@mark.parametrize("request_body,url_key,response_code", test_data_correct)
def test_send_email_works_correctly(
    test_client, test_url_map, test_mock_utils, request_body, url_key, response_code
):
    response = test_client.post(
        test_url_map[url_key], json=request_body, headers={"Accept": "application/json"}
    )

    assert response.status_code == response_code
    assert response.json["status"] == "ok"
