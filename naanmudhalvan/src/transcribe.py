from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import librosa

# Load the pre-trained model and processor
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# Transcription function
def transcribe(audio_path):
    speech, sr = librosa.load(audio_path, sr=16000)
    input_values = processor(speech, return_tensors="pt", sampling_rate=16000).input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]
    return transcription

# Save the transcription result to a text file
with open("transcription.txt", "w") as f:
    f.write(transcribe("audio_data/noisy/sample_noisy.wav"))
