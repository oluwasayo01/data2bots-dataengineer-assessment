import json
import os
import argparse
from utils import load_json, sniff_schema, write_json
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument('--data-dir', default="data", type=str, required=False)
parser.add_argument('--schema-dir', default="schema", type=str, required=False)

if __name__ == '__main__':
    args, _ = parser.parse_known_args()
    # print(dir(args))
    # print(args._get_kwargs())
    data_directory = Path(args.data_dir)
    schema_directory = Path(args.schema_dir)
    files = os.listdir(data_directory)
    files = list(filter(lambda x: x.split(".")[-1] == "json", files))
    for file in files:
        try:
            content = load_json(data_directory/file)
            schema = sniff_schema(content["message"])
            index = files.index(file)+1
            output_filepath = schema_directory/f"{schema_directory}_{index}.json"
            write_json(schema, output_filepath, indent=2)
        except KeyError:
            print(f"{file} does not contain the key 'message' ")
        except Exception as e:
            print(f"An error occured while reading {file} \n{e.with_traceback()}")
