from app.app import create_app
from app.blueprints.email import utils
from app.blueprints.email.models import EmailModel
from flask import url_for
from mock import Mock
from pytest import fixture


test_data_incorrect_headers = [
    ({}, {}, 406),
    ({}, {"key": "value"}, 406),
    ({"Accept": "application/json"}, {}, 406),
    ({"Accept": "application/json"}, {"key": "value"}, 406),
    ({"Content-Type": "application/json"}, {}, 406),
    ({"Content-Type": "application/json"}, {"key": "value"}, 406),
]
test_data_empty_body = [
    ({}, "mail", 400),
    ([{}, {}], "batch", 400),
]
test_data_invalid_body = [
    (
        {
            "sender": "test@example.com",
            "receiver": "test@example.com",
            "template_id": 1,
            "request_id": "1",
            "template_params": {"arg1": "Hello", "arg2": "World!"},
        },
        "mail",
        400,
    ),
    (
        [
            {
                "sender": "test@example.com",
                "receiver": "test@example.com",
                "subject": "Test",
                "request_id": "1",
                "template_params": {"arg1": "Hello", "arg2": "World!"},
            },
            {
                "sender": "test@example.com",
                "receiver": "test@example.com",
                "template_id": 1,
                "request_id": "1",
                "template_params": {"arg1": "Hello", "arg2": "World!"},
            },
        ],
        "batch",
        400,
    ),
]
test_data_correct = [
    (
        {
            "sender": "test@example.com",
            "receiver": "test@example.com",
            "subject": "Test",
            "template_id": 1,
            "request_id": "1",
            "template_params": {"arg1": "Hello", "arg2": "World!"},
        },
        "mail",
        201,
    ),
    (
        [
            {
                "sender": "test@example.com",
                "receiver": "test@example.com",
                "subject": "Test",
                "template_id": 1,
                "request_id": "1",
                "template_params": {"arg1": "Hello", "arg2": "World!"},
            },
            {
                "sender": "test@example.com",
                "receiver": "test@example.com",
                "subject": "Test",
                "template_id": 1,
                "request_id": "1",
                "template_params": {"arg1": "Hello", "arg2": "World!"},
            },
        ],
        "batch",
        201,
    ),
]


@fixture(scope="session")
def test_app():
    params = {
        "DEBUG": False,
        "TESTING": True,
        "SERVER_NAME": "localhost:8000",
    }
    app = create_app(test_settings=params)

    with app.app_context():
        yield app


@fixture(scope="session")
def test_client(test_app):
    yield test_app.test_client()


@fixture(scope="session")
def test_url_map(test_app):
    yield {
        "mail": url_for("email.send_new_mail"),
        "batch": url_for("email.send_batch_mail"),
    }


@fixture(scope="session")
def test_mock_utils():
    utils.send_mail_async = Mock(return_value=None)
    utils.send_batch_mail_async = Mock(return_value=None)
    EmailModel.insert = Mock(return_value=None)
    EmailModel.bulk_insert = Mock(return_value=None)
