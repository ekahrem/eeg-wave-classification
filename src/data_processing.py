import pandas as pd

def read_csv_eeg(file_path):
    return pd.read_csv(file_path)

# Usage: data = read_csv_eeg('data/eeg-music.csv')
