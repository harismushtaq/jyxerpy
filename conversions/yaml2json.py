import yaml
import json

def convert(yaml_data):
    yaml_content = yaml.safe_load(yaml_data)
    json_data = json.dumps(yaml_content, indent=2, ensure_ascii=False)
    return json_data

def get_source_exts():
  return [".yml", ".yaml"]

def get_target_ext():
  return ".json"