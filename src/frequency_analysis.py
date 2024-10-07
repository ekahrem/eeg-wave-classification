import numpy as np
from scipy.fft import fft

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
    #empty list to store data per channel
    fft_results = []
    for channel in eeg_data:
        N = len(channel) #N= number of samples
        yf = fft(channel) #stores fft results for current channel, converting time-domain signal into freq domain
        xf = np.fft.fftfreq(N, 1/sample_rate) #computes freq values using sample rate. 1/samp_rate reps time int btwn samples
        #find dominant freq
        idx = np.argmax(np.abs(yf)) #np.abs computes magnitude of fft output, np.argmax finds index of maximum value -- dominant freq
        freq = np.abs(xf[idx]) #extracts dom freq from xf
        wave_type = classify_wave_type(freq)
        fft_results.append((freq, wave_type)) #appends tuple of dominant frequency and wave type to results
    return fft_results
