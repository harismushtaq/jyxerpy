import yaml
import xml.etree.ElementTree as ET

def dict_to_xml(tag, d):
    element = ET.Element(tag)
    
    if isinstance(d, dict):
        for key, val in d.items():
            if key == '@attributes':
                for attr_name, attr_value in val.items():
                    element.set(attr_name, attr_value)
            elif key == '#text':
                element.text = str(val)
            elif isinstance(val, list):
                for sub_item in val:
                    element.append(dict_to_xml(key, sub_item))
            else:
                element.append(dict_to_xml(key, val))
    else:
        element.text = str(d)
    
    return element

def convert(yaml_data):
    yaml_content = yaml.safe_load(yaml_data)
    root_tag = list(yaml_data.keys())[0]  # Get root tag
    root_element = dict_to_xml(root_tag, yaml_content[root_tag])
    return ET.tostring(root_element, encoding='utf-8').decode('utf-8')

def get_source_exts():
  return [".yml", ".yaml"]

def get_target_ext():
  return ".xml"