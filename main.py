from lxml import etree
import sys
import os
from pathlib import Path
from typing import Tuple, Optional


class XMLValidator:
    def __init__(self, xml_path: str, xsd_path: str):
        self.xml_path = xml_path
        self.xsd_path = xsd_path
        
    def _load_schema(self) -> Optional[etree.XMLSchema]:
        """Load and parse XSD schema with error handling"""
        try:
            xsd_doc = etree.parse(self.xsd_path)
            return etree.XMLSchema(xsd_doc)
        except (etree.XMLSyntaxError, etree.ParseError) as e:
            raise ValueError(f"Invalid XSD Schema: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error loading schema: {str(e)}")

    def _load_xml(self) -> Optional[etree.ElementTree]:
        """Load and parse XML with error handling"""
        try:
            return etree.parse(self.xml_path)
        except (etree.XMLSyntaxError, etree.ParseError) as e:
            raise ValueError(f"Invalid XML: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error loading XML: {str(e)}")

    def validate(self) -> Tuple[bool, str]:
        """
        Validate XML against XSD schema with comprehensive error handling
        
        Returns:
            Tuple[bool, str]: (is_valid, message)
        """
        try:
            if not os.path.exists(self.xml_path):
                return False, f"XML file not found: {self.xml_path}"
            if not os.path.exists(self.xsd_path):
                return False, f"XSD file not found: {self.xsd_path}"

            schema = self._load_schema()
            xml_doc = self._load_xml()

            try:
                schema.assertValid(xml_doc)
                return True, "XML is valid against the XSD schema."
            except etree.DocumentInvalid as e:
                # Collect all validation errors
                errors = []
                for error in schema.error_log:
                    errors.append(f"Line {error.line}, Column {error.column}: {error.message}")
                return False, "\n".join(errors)

        except ValueError as e:
            return False, str(e)
        except Exception as e:
            return False, f"Unexpected error during validation: {str(e)}"

def main():
    if len(sys.argv) >= 3:
        xml_file = sys.argv[1]
        xsd_file = sys.argv[2]
    else:
        xml_file = ""  # Default XML
        xsd_file = ""  # Default XSD

    # Create validator and run validation
    validator = XMLValidator(xml_file, xsd_file)
    is_valid, message = validator.validate()

    print("\nValidation Results:")
    print("-" * 50)
    if is_valid:
        print("✓ XML is valid!")
    else:
        print("✗ Validation failed!")
        print("\nError details:")
        print(message)
    print("-" * 50)

if __name__ == "__main__":
    main()