import numpy as np
from scipy.fft import fft
import pandas as pd


#determines EEG wave type by frequency (Hz)
def classify_wave_type(freq):
    if freq >= 0.5 and freq <= 4:
        return "Δ - Delta"
    elif freq > 4 and freq <= 8:
        return "Θ - Theta"
    elif freq > 8 and freq <= 12:
        return "Α - Alpha"
    elif freq > 12 and freq <= 30:
        return "Β - Beta"
    elif freq > 30 and freq <=100:
        return "Γ - Gamma"
    else:
        return "Ambiguous"
    

#Fourier transformation on EEG data to extract essential components from freq
#returns each channel's dominant frequency   

def freq_analysis(eeg_data, sample_rate):

    dominant_freqs = {}

    for channel_name in eeg_data.columns:
        channel = eeg_data[channel_name].dropna().astype(float).values

        if len(channel) == 0:
            print(f"Channel {channel_name} has no valid data")
            continue

        N = len(channel)
        yf = fft(channel)
        xf = np.fft.fftfreq(N, 1/sample_rate)

        #find dom freq
        idx = np.argmax(np.abs(yf))
        freq = np.abs(xf[idx])
        wave_type = classify_wave_type(freq)

        dominant_freqs[channel_name] = (freq, wave_type)


    return dominant_freqs
    