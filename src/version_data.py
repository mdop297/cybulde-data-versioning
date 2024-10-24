from src.config_schemas.config_schema import Config
from src.utils.config_utils import get_config
from src.utils.data_utils import initialize_dvc, initialize_dvc_storage


@get_config(config_path="../configs", config_name="config")
def version_data(config: Config) -> None:
    print(config)
    initialize_dvc()
    initialize_dvc_storage(dvc_remote_name=config.dvc_remote_name, dvc_remote_url=config.dvc_remote_url)


if __name__ == "__main__":
    version_data()
