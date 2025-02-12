import json
import os
from typing import Dict, Any


class MappingLoader:
    @staticmethod
    def load_mapping(file_path: str, key_field: str, value_field: str) -> Dict[int, Any]:
        """
        Reads a JSONL file and builds a mapping from the key_field (converted to int)
        to the value found under value_field.

        If the file is not found, returns an empty dictionary.
        """
        mapping: Dict[int, Any] = {}
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    record = json.loads(line)
                    key = record.get(key_field)
                    if key is not None:
                        mapping[int(key)] = record.get(value_field)
        except FileNotFoundError:
            pass
        return mapping
