import os
os.environ["LIBROSA_RESAMPLER"] = "resampy"

import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    pitch = librosa.yin(y, fmin=50, fmax=300)
    energy = np.sum(librosa.feature.rms(y=y), axis=0)
    return mfcc, pitch, energy



# Plot MFCC
mfcc, pitch, energy = extract_features("audio_data/cleaned/sample.wav")
librosa.display.specshow(mfcc, x_axis='time')
plt.title("MFCC")
plt.colorbar()
plt.show()
