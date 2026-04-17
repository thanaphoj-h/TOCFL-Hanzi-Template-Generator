import yaml
import os

class Config:
    def __init__(self, data: dict, root_dir: str):
        self._data = data
        self._root_dir = root_dir
    
    @classmethod
    def load_yml(cls, path: str):
        root_dir = os.path.dirname(os.path.abspath(path))
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as ex:
            raise RuntimeError(f"Invalid YAML config: {ex}")

        return cls(data, root_dir)
    
    def get(self, key: str, default=None):
        
        # .env override
        env_key = key.upper().replace(".", "_")
        if env_key in os.environ:
            return os.environ[env_key]

        keys = key.split(".")
        value = self._data

        for k in keys:
            if not isinstance(value, dict) or k not in value:
                return default
            value = value[k]

        return value