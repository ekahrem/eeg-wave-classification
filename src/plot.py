import matplotlib.pyplot as plt
import numpy as np
from frequency_analysis import freq_analysis
from data_processing import load_csv_eeg
import pandas as pd
from scipy.fft import fft
import seaborn as sns

plt.rcParams['font.family'] = 'Arial'

# Function to plot EEG data for a single channel
def plot_wave(channel_data, sample_rate, channel_name, wave_type):
    
    plt.figure(figsize=(10, 4))

    ax = plt.gca()  # Get current axes
    ax.set_facecolor('black')

    plt.style.use('dark_background')

    plt.plot(channel_data.index, channel_data.values, label = channel_name)

    plt.title(f"EEG Signal for {channel_name}\nDominant Wave Type: {wave_type}", fontsize=14, pad=20, color='white', weight='bold')
    plt.xlabel("Time (s)", fontsize=10, color='white', weight='light')
    plt.ylabel("Amplitude", fontsize=10, color='white', weight='light')

    plt.xticks(fontsize=8, color='white', weight='light')
    plt.yticks(fontsize=8, color='white', weight='light')

    plt.gcf().patch.set_color('black') 

    plt.grid(color='gray', alpha=0.5)  # Adjust grid transparency
    plt.grid(True)



    plt.tight_layout()


    plt.show()


    
if __name__ == "__main__":

    # Load the CSV file
    file_path = '/Users/evangeliakahremanis/eeg-wave-classification/data/bws-sample.csv'
    eeg_data, sample_rate, time = load_csv_eeg(file_path)

    #list avail channels
    print("Channels:")
    for idx, channel_name in enumerate(eeg_data.columns):
        print(f"{idx + 1}: {channel_name}")

    #user selects by entering num
    while True:
        try:
            selection = int(input("Select a channel by number (1-{}): ".format(len(eeg_data.columns))))
            if 1 <= selection <= len(eeg_data.columns):
                channel_name = eeg_data.columns[selection - 1]
                break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    #perfomr fa
    dominant_freqs = freq_analysis(eeg_data, sample_rate)

#DB!!!!!!!!
    print("Available dominant frequencies:")
    for key in dominant_freqs:
        print(f"{key}: {dominant_freqs[key]}")  # Print each channel and its corresponding frequency and wave type


    try:
    #get df and wave type
        freq, wave_type = dominant_freqs[channel_name]
        print(f"Dominant Frequency for {channel_name}: {freq:.2f} Hz, Wave Type: {wave_type}")
    except KeyError: 
        print(f"Error: Channel '{channel_name}' not found in dominant frequencies. Please check the channel name.")



    #plot wave
    plot_wave(eeg_data[channel_name], sample_rate, channel_name, wave_type)


    