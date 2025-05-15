import webrtcvad
import wave

def read_wave(path):
    with wave.open(path, "rb") as wf:
        return wf.readframes(wf.getnframes()), wf.getframerate()

def detect_speech(file_path):
    vad = webrtcvad.Vad(3)
    audio, rate = read_wave(file_path)
    frame_duration = 30  # ms
    frame_size = int(rate * frame_duration / 1000) * 2  # bytes per frame (16-bit samples)
    
    for i in range(0, len(audio), frame_size):
        frame = audio[i:i+frame_size]
        if len(frame) < frame_size:
            break
        if vad.is_speech(frame, rate):
            return True
    return False

print(detect_speech("audio_data/noisy/fixed.wav"))
