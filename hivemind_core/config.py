"""Configuration file for the application behavior
"""

from functools import lru_cache
from ovos_config import Configuration


class Settings:
    """Class that host the application options.
    All the variables ara casted by Pydantic.
    """

    config = Configuration()
    config_db = config["hivemind_database_config"]

    database_backend: str = config_db.get("backend", "redis")
    database_host: str = config_db.get("host", "127.0.0.1")
    database_port: int = config_db.get("port", 6379)


@lru_cache()
def get_settings():
    """Expose the settings

    :return: Return the settings
    :rtype: Settings
    """
    return Settings()
