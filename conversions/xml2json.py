import json
import xmltodict

def convert(xml_data):
  return json.dumps(xmltodict.parse(xml_data), indent=2)

def get_source_exts():
  return [".xml"]

def get_target_ext():
  return ".json"
