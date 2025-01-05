import logging
import sys


from .settings import settings


def setup_logger():
    log_format = logging.Formatter(
        f"[%(levelname)s] %(asctime)s - {f'{settings.LOGGER_PREFIX}::' if settings.LOGGER_PREFIX else ''}%(name)s = %(message)s"
    )
    logger = logging.getLogger(settings.api_app_name)

    logger.setLevel(logging.DEBUG)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(log_format)
    logger.addHandler(stdout_handler)


    logger.debug("Logger setup complete.")

    fastapi_logger = logging.getLogger("fastapi")
    uvicorn_logger = logging.getLogger("uvicorn")
    uvicorn_access_logger = logging.getLogger("uvicorn.access")


    def uncaught_exception_handler(type, value, tb):
        logger.exception(f"Uncaught exception: {str(value)}")

    # Install exception handler
    sys.excepthook = uncaught_exception_handler

    return logger
