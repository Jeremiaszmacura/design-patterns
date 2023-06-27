import json

from stock_data_provider import StockDataProvider
from analistycs_library import AnalitycsLibrary
from adapter import Adapter


RANDOM_JSON_DATA = json.dumps({"random_key": "random_value"})


if __name__ == "__main__":
    # Stock Data Provider - XML Data Format
    stock_data_provider = StockDataProvider()
    stock_data_path = stock_data_provider.get_stock_data()

    # Adapter
    adapter = Adapter()
    stock_data_dict = adapter.parse_xml_to_json(stock_data_path)
    
    # Analistycs Library - JSON Data Format
    analitycs_library = AnalitycsLibrary(stock_data_dict)
    print(analitycs_library)
