from typing import Any
import json
from pathlib import Path

class DataTemplateManager:
    
    def __init__(self, json_filename:str) -> None:
        self.json_filename = json_filename
        self._template = self._load_json_templates()
    
    def _load_json_templat(self) -> dict:
        static_json_path = Path(__file__).parents[1] / "static" / "json" / self.json_filename
        
        if not static_json_path.exists():
            raise FileNotFoundError(f"JSON file {self.json_filename} not found.")
        
        with open(static_json_path, 'r') as file:
            return json.load(file)
    
    def set_value(self, key:str, value:Any) -> None:
        if key in self._template:
            self._template[key] = value
        else:
            raise KeyError(f"Key {key} not found in template {self.json_filename}.")
        
    def get_value(self, key: str) -> Any:
        if key in self._template:
            return self._template[key]
        else:
            raise KeyError(f"Key {key} not found in template {self.json_filename}.")
    
    def to_json(self) -> str:
        return json.dumps(self._templates)
    
    def from_json(self, json_string: str) -> None:
        try:
            data = json.loads(json_string)
            for key, value in data.items():
                if key in self._template:
                    self._template[key] = value
                else:
                    raise KeyError(f"Key {key} not found in template {self.json_filename}.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON string provided.")