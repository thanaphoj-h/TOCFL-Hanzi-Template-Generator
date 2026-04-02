import yaml
import os

class Config:
    def __init__(self, data: dict, root_dir: str):
        self._data = data
        self._root_dir = root_dir
    
    @classmethod
    def load_yml(cls, path: str):
        root_dir = os.path.dirname(os.path.abspath(path))
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        config = cls(data, root_dir)
        return config
    
    def get(self, key: str, default=None):
        keys = key.split(".")
        value = self._data

        for k in keys:
            if not isinstance(value, dict) or k not in value:
                return default
            value = value[k]

        return value
            