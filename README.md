# XML and XSD Validation Tool

This project provides a tool for validating XML files against XSD schemas using Python and the `lxml` library.

## Features

- Load and parse XML files
- Load and parse XSD schemas
- Validate XML files against XSD schemas
- Comprehensive error handling

## Requirements

- Python 3.6+
- `lxml` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/amirmohammadraei/xml-xsd-validator.git
    cd xml-xsd-validator
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

```python
from xml_validator import XMLValidator

xml_path = 'path/to/your/xmlfile.xml'
xsd_path = 'path/to/your/schemafile.xsd'

validator = XMLValidator(xml_path, xsd_path)
is_valid, message = validator.validate()

if is_valid:
    print("XML is valid.")
else:
    print(f"XML is invalid: {message}")
