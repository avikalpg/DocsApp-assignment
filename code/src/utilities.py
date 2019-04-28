import os
import sys
import pandas as pd
from tqdm import tqdm, tqdm_notebook
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

processed_files_location = "../../data/processed/"

# Requires cleaned data to be available at data/processed/Health-Tweets/
# To generate this data, run 'code/data_prep/clean.py'
def load_data():
    file_location = processed_files_location + "Health-Tweets/"
    data = dict()
    for data_file in os.listdir(file_location):
        print("loading " + data_file + "...", end='')
        table_name = data_file.split(".")[0]
        data[table_name] = pd.read_csv(file_location + data_file, sep="|", header=None, encoding='cp1252')
        data[table_name].columns = ["id", "timestamp", "tweet"]
        print("\rloaded " + data_file + "    ")

    return data

# Requires all pre-requisites of load_data()
def save_processed_data():
    data = load_data()
    for source in data:
        data[source]['source'] = source

    # pouring all the data into a single table
    table = pd.concat(data.values())

    # dropping empty tweet strings
    table.dropna(axis=0, subset=['tweet'], inplace=True)

    # Getting rid of stop-words and adding that as a column
    table = extract_relevant_words(table)

    table.to_csv(processed_files_location + "tweets.csv", sep="|", index=False)
    
def extract_relevant_words(table):
    stop_words = stopwords.words('english')
    def relevant_words(sentence):
        try:
            word_tokens = word_tokenize(sentence.lower())
            filtered_sentence = [w for w in word_tokens if not w in stop_words]
            return ' '.join(filtered_sentence)
        except:
            sys.stderr.write(str(sentence) + "\t")
            return ""
    
    if 'ipykernel' in sys.modules:
        tqdm_notebook().pandas()
    else:
        tqdm().pandas()

    table['no_stop_words'] = table.tweet.progress_apply(lambda x: relevant_words(x))
    return table

def load_table(refresh = False):
    file_path = processed_files_location + "tweets.csv"
    if refresh or not os.path.exists(file_path):
        save_processed_data()
    return pd.read_csv(file_path, sep="|", encoding='cp1252')

if __name__ == '__main__':
    save_processed_data()