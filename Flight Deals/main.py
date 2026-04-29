from pprint import pprint
from data_manager import DataManager


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)

pprint(sheet_data)
