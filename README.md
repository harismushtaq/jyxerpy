# jyxerpy

Python script to convert data between XML, JSON and YAML formats.

## Dependencies
- Python 3.6 or higher
- xml2dict

To install dependencies,
```sh
pip install -r requirements.txt
```

## Usage

```sh
python script.py <file_pattern> --type <conversion_type> [--out-path <output_directory>]
```

### Arguments:
- `<file_pattern>`: Pattern to match input files (supports wildcards, e.g., `*.xml`).
- `--type`: The type of conversion to perform. Choices are:
  - `xml2json`: Convert XML to JSON
  - `json2xml`: Convert JSON to XML
  - `xml2yaml`: Convert XML to YAML
  - `yaml2xml`: Convert YAML to XML
- `--out-path` (optional): Directory to save the converted files.

## Example

### Convert all XML files in the current directory to JSON:
```sh
python script.py "*.xml" --type xml2json --out-path converted_files
```

### To convert a single file to same directory
```sh
python .\jyxerpy.py --type xml2json test_xml.xml
```

## Notes
- Output files are saved in the same directory as the input files unless `--out-path` is specified.
- Output file has the same name as the input file. If input file has the standard extension of the input format than it is replaced with the output file extension (for example, .xml will be replaced by .json when converting from xml to json). If input file does not have the standard extension then output file extension will be added on top (for example input.xml2 will become input.xml2.json when converting from xml to json and a non standrad .xml2 extension is found on the input file).
- The script does not do any validation if source file is in the correct format. Whatever instruction is given it will try to do that conversion.
- No limits or logic is applied based on file extension, if a file with .xml extension has json data and it is converted using json2yaml option it will work fine.

## License
This project is open-source and available under the MIT License.

## Contributions
Are welcome,

- Create a ticket
- Make changes in a branch and create a PR to main branch.