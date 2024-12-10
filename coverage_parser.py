# coverage_parser.py - Parses coverage reports to identify untested code

import xml.etree.ElementTree as ET

def parse_coverage(file_path):
    """Parse the coverage XML file to extract uncovered lines."""
    tree = ET.parse(file_path)
    root = tree.getroot()
    uncovered = []
    for class_elem in root.findall(".//class"):
        class_name = class_elem.attrib['name']
        for line in class_elem.findall(".//line[@hits='0']"):
            uncovered.append(f"Class: {class_name}, Line: {line.attrib['number']}")
    return uncovered

if _name_ == "_main_":
    uncovered_lines = parse_coverage("coverage.xml")
    for line in uncovered_lines:
        print(line)

