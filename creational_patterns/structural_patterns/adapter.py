import json
import xmltodict


class Adapter():
    def parse_xml_to_json(self, xml_data_path: str) -> str:
        with open(xml_data_path) as fd:
            dict_data = xmltodict.parse(fd.read())
        dict_data = json.dumps(dict_data)
        return dict_data