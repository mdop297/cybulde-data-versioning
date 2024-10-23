from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass


@dataclass
class Config:
    key: str = "value"


def setup_config():
    cs = ConfigStore.instance()
    cs.store(name="config_schema", node=Config)
