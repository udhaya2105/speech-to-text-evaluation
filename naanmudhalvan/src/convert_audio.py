from pydub import AudioSegment

def convert_to_pcm(input_path, output_path):
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1)         # Mono
    audio = audio.set_frame_rate(16000)   # 16000 Hz
    audio = audio.set_sample_width(2)     # 16-bit PCM
    audio.export(output_path, format="wav")
    print(f"Converted and saved to {output_path}")

convert_to_pcm("audio_data/noisy/sample_noisy.wav", "audio_data/noisy/sample_noisy_fixed.wav")
