from dependency_injector import containers, providers
import os

from src.settings import settings

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5000

ENV_VAR_NAMES = [
    "HOST",
    "PORT",
    "GRAFANA_BASE_URL",
    "KIBANA_BASE_URL",
    "MYSQL_HOST",
    "MYSQL_PORT",
]

config_bag = {}


class _Config(object):
    def __init__(self, testing=False):
        if not testing:
            # Load settings from settings.py
            for key, value in settings.items():
                config_bag[key] = value
        # Load settings from environment variables. Overwrites settings from settings.py
        # if the same key is found in the environment variables
        self.__read_envs()

    def __getattr__(self, item):
        return config_bag.get(item)

    def __read_envs(self):
        for key in ENV_VAR_NAMES:
            if os.environ.get(key):
                config_bag[key] = os.environ.get(key)
        return config_bag

    def host(self) -> str:
        if self.__getattr__("HOST"):
            return self.__getattr__("HOST")
        else:
            return DEFAULT_HOST

    def port(self) -> int:
        if self.__getattr__("PORT"):
            return int(self.__getattr__("PORT"))
        else:
            return DEFAULT_PORT


class DI(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["src"],
    )
    config = providers.Singleton(_Config)
    # devopsPortal = providers.Factory(
    #     DevOpsPortalClient,
    #     base_url=config().DEVOPS_PORTAL_BASE_URL,
    #     headers={
    #         "Content-Type": "application/json",
    #     },
    # )
    # grafanaClient = providers.Factory(
    #     GrafanaClient,
    #     base_url=config().GRAFANA_BASE_URL,
    #     headers={
    #         "Content-Type": "application/json",
    #     },
    # )
