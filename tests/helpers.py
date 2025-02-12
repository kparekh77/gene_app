import json


def write_jsonl(file_path, records):
    with open(file_path, "w") as f:
        for rec in records:
            f.write(json.dumps(rec) + "\n")