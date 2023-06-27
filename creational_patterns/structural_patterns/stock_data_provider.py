import os
import xml.etree.cElementTree as ET


class StockDataProvider():
    
    def get_stock_data(self, data_path: str = "stock_data", file_name: str = "stock_data") -> str:
        """Create xml file"""
        root = ET.Element("root")
        doc = ET.SubElement(root, "doc")
        ET.SubElement(doc, "field1", name="blah").text = "some value1"
        ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"
        tree = ET.ElementTree(root)

        current_path = os.path.dirname(os.path.abspath(__file__))
        directory_path = os.path.join(current_path, data_path)
        file_path = os.path.join(directory_path, f"{file_name}.xml")
        if not os.path.isdir(directory_path):
            os.makedirs(directory_path)
        tree.write(file_path)

        return file_path