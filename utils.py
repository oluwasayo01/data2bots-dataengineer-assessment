import json
import os

def load_json(path: str) -> dict:
    """Loads a json file specified by the `path` supplied

        Args:
            path(str): The path to json file
        Returns:
            dict
        Error:
            FileNotFoundError: If `path` does not point a file
    """
    content = dict()
    try:
        with open(path, "r") as f:
            content = json.load(f)
        return content
    except FileNotFoundError as e:
        print(e)


def write_json(obj, path, indent=4) -> None:
    """Writes object `obj` to a json file specified by `path`
        Args:
            obj(any): Any python object
            path(str): The path to json file
            indent(int): indentation to put in json file
        Returns:
            None
    """
    try:
        with open(path, "w") as f:
            json.dump(obj, f, indent=indent)
    except FileNotFoundError:
        os.makedirs(path.parent)
        write_json(obj, path, indent=indent)


def sniff_schema(obj: dict) -> dict:
    """Detects schema of a fields in python dictionary `obj`.
        It sniffs schema of nested dictionaries the same way they are nested in 
        the dictionary.
        Args:
            obj(dict): The path to json file
        Returns:
            dict
    """
    schema = dict()
    for key, value in obj.items():
        schema[key] = {"tag": "", "description": "", "required": False}
        if isinstance(value, int):
            schema[key].update({"type": "integer"})
        if isinstance(value, str):
            schema[key].update({"type": "string"})
        if isinstance(value, list):
            try:
                sample = value[0]
                if isinstance(sample, str):
                    schema[key].update({"type": "ENUM"})
                elif isinstance(sample, list) or isinstance(sample, dict):
                    schema[key].update({"type": "ARRAY"})
            except IndexError:
                schema[key].update({"type": "ENUM"})
        if isinstance(value, dict):
            schema[key] = sniff_schema(value)
    return schema
