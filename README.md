# 🎙️ Voice Recorder App

A simple voice recording desktop app built with Python and Tkinter. It allows you to record your voice with a GUI interface and saves the recording as a `.wav` file with a timestamped filename.

---

## 📌 Features

- 🟢 Start/Stop voice recording with a clean GUI
- 💾 Saves audio as `recording_YYYY-MM-DD_HH-MM.wav`
- 🎛️ Uses `sounddevice` for real-time audio capture
- 🧠 Multithreading ensures the app stays responsive
- ✅ Cross-platform compatibility (Windows, Mac, Linux)

---

## 💻 Requirements

Install the required Python libraries:

```bash
pip install sounddevice scipy numpy
