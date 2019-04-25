import os
import pandas as pd

# Requires cleaned data to be available at data/processed/Health-Tweets/
# To generate this data, run 'code/data_prep/clean.py'
def load_data():
    file_location = "../../data/processed/Health-Tweets/"
    data = dict()
    for data_file in os.listdir(file_location):
        print("loading " + data_file + "...", end='')
        table_name = data_file.split(".")[0]
        data[table_name] = pd.read_csv(file_location + data_file, sep="|", header=None, encoding='cp1252')
        data[table_name].columns = ["id", "timestamp", "tweet"]
        print("\rloaded " + data_file + "    ")

    return data