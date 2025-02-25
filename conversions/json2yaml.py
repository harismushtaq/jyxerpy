import json
import yaml

def convert(json_data):
    json_content = json.loads(json_data)
    yaml_string = yaml.dump(json_content, default_flow_style=False, allow_unicode=True)
    return yaml_string

def get_source_exts():
  return [".json"]

def get_target_ext():
  return ".yml"