import json
import xmltodict

def convert(json_data):
  return xmltodict.unparse(json.loads(json_data), pretty=True)

def get_source_exts():
  return [".json"]

def get_target_ext():
  return ".xml"
