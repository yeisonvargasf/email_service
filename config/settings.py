from os import getenv


LOG_LEVEL = "DEBUG" if bool(getenv("FLASK_DEBUG", "True")) else "INFO"
