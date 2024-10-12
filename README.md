# EEG Wave Classification

This project analyzes EEG (electroencephalogram) data to identify the dominant wave type (Delta, Theta, Alpha, Beta, Gamma) for different channels. It provides a visual representation of the EEG signals and their corresponding dominant frequencies, allowing for an intuitive understanding of the data.

## Features

- Load EEG data from a CSV file.
- Select from available EEG channels for analysis.
- Display the EEG signal waveform for the selected channel.
- Calculate and display the dominant frequency and corresponding wave type.

## Requirements

- Python 3.x
- pandas
- numpy
- scipy
- matplotlib

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/eeg-wave-classification.git
   cd eeg-wave-classification

2. Create virtual environment (optional, but reccommended):

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. Install required packages:
    pip install pandas numpy scipy matplotlib


## Usage
1. Prepare your EEG data in CSV format with columns representing channels and a 'Time' column.

2. Place your CSV file in the appropriate directory (e.g., /data/).

3. Run the plotting script:

python src/plot.py

4. Follow the prompts to select a channel for analysis.

