from os import getenv


wsgi_app = "app.app:create_app()"
reload = getenv("FLASK_ENV", "development") == "development"
accesslog = "-"
access_log_format = (
    "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)sµs"
)
loglevel = "debug" if getenv("FLASK_ENV", "development") == "development" else "info"
capture_output = True
bind = f"0.0.0.0:{getenv('PORT', '8000')}"
workers = 2
worker_class = "eventlet"
