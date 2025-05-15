


from jiwer import wer, cer
from transcribe import transcribe  # your transcribe function
import pandas as pd
import os

if __name__ == "__main__":
    ref = "the quick brown fox jumps over the lazy dog"
    hyp = transcribe("audio_data/noisy/sample_noisy.wav")

    print("WER:", wer(ref, hyp))
    print("CER:", cer(ref, hyp))

    # Make sure results folder exists
    os.makedirs("results", exist_ok=True)

    # Save results in a CSV file
    results = {
        "filename": ["sample_noisy.wav"],
        "wer": [wer(ref, hyp)],
        "cer": [cer(ref, hyp)],
        "transcription": [hyp],
        "reference": [ref]
    }

    df = pd.DataFrame(results)
    df.to_csv("results/metrics.csv", index=False)
