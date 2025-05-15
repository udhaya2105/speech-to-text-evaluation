import os
import librosa
import soundfile as sf

def preprocess_audio(file_path, output_path, sr=16000):
    audio, _ = librosa.load(file_path, sr=sr)
    trimmed_audio, _ = librosa.effects.trim(audio)  # Remove silence
    sf.write(output_path, trimmed_audio, sr)

# Example usage
input_dir = "audio_data/raw"
output_dir = "audio_data/cleaned"
os.makedirs(output_dir, exist_ok=True)

for fname in os.listdir(input_dir):
    if fname.endswith(".wav"):
        preprocess_audio(os.path.join(input_dir, fname),
                         os.path.join(output_dir, fname))
