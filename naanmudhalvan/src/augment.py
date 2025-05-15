from pydub import AudioSegment
import random

def add_noise(audio_file, noise_file, output_file, snr_db=10):
    speech = AudioSegment.from_wav(audio_file)
    noise = AudioSegment.from_wav(noise_file).apply_gain(-snr_db)
    combined = speech.overlay(noise)
    combined.export(output_file, format="wav")

add_noise("audio_data/cleaned/sample.wav",
          "noises/crowd.wav",
          "audio_data/noisy/sample_noisy.wav")
