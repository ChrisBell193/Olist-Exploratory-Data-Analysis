import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        path = os.path.dirname(os.path.dirname(__file__))
        csv_path = os.path.join(path, 'data', 'csv')
        file_names = [item for item in os.listdir(csv_path) if item.endswith('.csv')]
        new_file_names = []
        key_names = []
        #getting desired key names from file names
        for item in file_names:
            if item.endswith("_dataset.csv"):
                new_file_names.append(item.replace("_dataset.csv", ""))
            elif item.endswith(".csv"):
                new_file_names.append(item.replace(".csv", ""))
            else:
                new_file_names.append(item)
        for item in new_file_names:
            if item.startswith("olist_"):
                key_names.append(item.replace("olist_", ""))
            else:
                key_names.append(item)

        data = {}
        for (key, csv_file) in zip(key_names, file_names):
            data[key] = pd.read_csv(os.path.join(csv_path, csv_file))
        return data
