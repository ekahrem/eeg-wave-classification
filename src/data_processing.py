import pandas as pd

def load_csv_eeg(file_path):

    #load file in
    df = pd.read_csv(file_path)

    #extract time
    time = df['Time']

    #drop and seperate time
    eeg_data = df.drop(columns='Time')


    #calc sample rate
    time_diff = time.diff().dropna().mean() #avg time int
    sample_rate = 1 / time_diff # rate in Hz

    print(f"Sample rate: {sample_rate:.2f} Hz")

    return eeg_data, sample_rate, time


    
