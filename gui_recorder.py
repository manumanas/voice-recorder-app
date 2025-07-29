import tkinter as tk
from tkinter import messagebox
import sounddevice as sd
from scipy.io.wavfile import write
import datetime
import numpy as np
import threading

# Global variables
recording = False
frames = []
fs = 44100  # Sample rate

def start_recording():
    global recording, frames
    recording = True
    frames = []

    status_label.config(text="🔴 Recording...")
    record_thread = threading.Thread(target=record)
    record_thread.start()

def record():
    global frames
    while recording:
        data = sd.rec(int(0.5 * fs), samplerate=fs, channels=1)
        sd.wait()
        frames.append(data)

def stop_recording():
    global recording, frames

    if not recording:
        return

    recording = False
    status_label.config(text="✅ Recording Stopped")

    audio = np.concatenate(frames)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"recording_{timestamp}.wav"
    write(filename, fs, audio)
    messagebox.showinfo("Saved", f"Recording saved as {filename}")

# --- GUI SETUP ---
root = tk.Tk()
root.title("🎙 Voice Recorder")
root.geometry("300x200")
root.resizable(False, False)

# Buttons
start_button = tk.Button(root, text="Start Recording", command=start_recording, bg="green", fg="white", font=("Arial", 12))
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Recording", command=stop_recording, bg="red", fg="white", font=("Arial", 12))
stop_button.pack(pady=10)

status_label = tk.Label(root, text="Press Start to begin recording", font=("Arial", 10))
status_label.pack(pady=10)

# Run the GUI loop
root.mainloop()


