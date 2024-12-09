
import xml.etree.ElementTree as ET

def parse_coverage(file_path):
    """Parse the coverage XML file to extract uncovered lines."""
    tree = ET.parse(file_path)
    root = tree.getroot()
    uncovered = []
    # Print the structure of the XML to verify parsing
    print("Parsing XML file...")
    
    for class_elem in root.findall(".//class"):
        class_name = class_elem.attrib['name']
        print(f"Parsing class: {class_name}")  # Debug print
        for line in class_elem.findall(".//line[@hits='0']"):
            line_number = line.attrib['number']
            print(f"Found uncovered line: {class_name}, Line: {line_number}")  # Debug print
            uncovered.append(f"Class: {class_name}, Line: {line_number}")
    
    if not uncovered:
        print("No uncovered lines found.")
    
    return uncovered

if __name__ == "__main__":
    uncovered_lines = parse_coverage("coverage.xml")
    for line in uncovered_lines:
        print(line)

