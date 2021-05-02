from threading import Thread

from app.extensions import mail
from flask import current_app
from flask import render_template
from flask_mailman import EmailMessage


def _send_mail_async(app, message):
    with app.app_context():
        message.send()


def _send_batch_mail_async(app, params):
    with app.app_context(), mail.get_connection() as connection:
        messages = [
            EmailMessage(
                param["subject"],
                render_template(
                    f"email/{param['template_id']}.txt", **param["template_params"]
                ),
                param["sender"],
                [param["receiver"]],
                connection=connection,
            )
            for param in params
        ]
        connection.send_messages(messages)


def send_mail_async(param):
    message = EmailMessage(
        param["subject"],
        render_template(
            f"email/{param['template_id']}.txt", **param["template_params"]
        ),
        param["sender"],
        [param["receiver"]],
    )

    Thread(
        target=_send_mail_async, args=(current_app._get_current_object(), message)
    ).start()


def send_batch_mail_async(params):
    Thread(
        target=_send_batch_mail_async, args=(current_app._get_current_object(), params)
    ).start()
