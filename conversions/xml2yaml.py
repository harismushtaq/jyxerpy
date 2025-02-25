import xml.etree.ElementTree as ET
import yaml

def xml_to_dict(element):
    node = {}
    
    # Include attributes if present
    if element.attrib:
        node['@attributes'] = element.attrib
    
    # Process child elements recursively
    children = list(element)
    if children:
        child_dict = {}
        for child in children:
            child_name = child.tag
            child_data = xml_to_dict(child)
            
            if child_name in child_dict:
                if isinstance(child_dict[child_name], list):
                    child_dict[child_name].append(child_data)
                else:
                    child_dict[child_name] = [child_dict[child_name], child_data]
            else:
                child_dict[child_name] = child_data
        
        node.update(child_dict)
    else:
        # Assign text content if no children are present
        text = element.text.strip() if element.text else ''
        if text:
            node['#text'] = text
    
    return node

def convert(xml_data):
    root = ET.fromstring(xml_data)
    xml_dict = {root.tag: xml_to_dict(root)}
    return yaml.dump(xml_dict, default_flow_style=False, allow_unicode=True)

def get_source_exts():
  return [".xml"]

def get_target_ext():
  return ".yml"