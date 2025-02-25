import os
import glob
import argparse
import importlib

def get_target_filename(filename, source_exts, target_ext, out_path=None):
    base, ext = os.path.splitext(os.path.basename(filename))
    target_filename = base + target_ext if ext.lower() in source_exts else filename + target_ext
    
    if out_path:
        os.makedirs(out_path, exist_ok=True)  # Ensure output directory exists
        return os.path.join(out_path, target_filename)
    
    return os.path.join(os.path.dirname(filename), target_filename)

def process_file(one_file, conversion_type, out_path=None):
    with open(one_file, 'r', encoding='utf-8') as file:
        source_content = file.read()

    try:
        module_name = f"conversions.{conversion_type}"
        conversion_module = importlib.import_module(module_name)
        target_data = conversion_module.convert(source_content)
        target_file = get_target_filename(one_file, conversion_module.get_source_exts(), conversion_module.get_target_ext(), out_path)
        
        with open(target_file, 'w', encoding='utf-8') as file:
            file.write(target_data)
    except ModuleNotFoundError:
        print(f"Error: Failed to process {one_file}, Conversion type '{conversion_type}' is not supported.")
        return
    
    print(f'Converted {one_file} to {target_file} successfully.')

def main():
    parser = argparse.ArgumentParser(description="Get the files to convert and what type of conversion to make")
    parser.add_argument("file_pattern", type=str, help="File pattern to match (supports wildcards).")
    parser.add_argument(
        "--type", type=str, required=True,
        choices=["xml2json", "json2xml", "xml2yaml", "yaml2xml"], 
        help="Type of conversion, for example xml2json for converting XML file(s) to JSON."
    )
    parser.add_argument("--out-path", type=str, help="Path where output file(s) should be created.")
    args = parser.parse_args()
    
    file_pattern = args.file_pattern
    out_path = args.out_path
    
    # If the pattern does not include a path, use the current directory
    directory, pattern = os.path.split(file_pattern)
    if not directory:
        directory = os.getcwd()
    
    # Find matching files
    matching_files = [f for f in glob.glob(os.path.join(directory, pattern)) if os.path.isfile(f)]
    
    if not matching_files:
        print("No files matched the pattern.")
        exit(1)
    
    conversion_type = args.type
    
    # Process each matching file
    for one_file in matching_files:
        process_file(one_file, conversion_type, out_path)

if __name__ == "__main__":
    main()