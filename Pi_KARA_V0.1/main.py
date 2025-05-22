# main.py

import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading
import pyttsx3
import queue
import time
import os
import sys
from vosk import Model, KaldiRecognizer
import pyaudio
from utils.sarcasm_engine import sarcastic_response

# Initialize TTS engine
tts = pyttsx3.init()
tts.setProperty('rate', 160)

# Queue for voice commands
q = queue.Queue()

# Load Vosk model
model_path = "models/model"
if not os.path.exists(model_path):
    print("Vosk model not found. Please download and place in 'models/model'")
    sys.exit(1)

model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

# Setup PyAudio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                input=True, frames_per_buffer=8000)
stream.start_stream()

# Tkinter GUI Setup
class AvatarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("K.A.R.A. 2.0")
        self.root.geometry("600x400")
        self.root.configure(bg="black")

        # Load animated GIF
        self.label = tk.Label(root, bg="black")
        self.label.pack(pady=10)
        self.avatar = Image.open("assets/avatar.gif")
        self.frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(self.avatar)]
        self.frame_index = 0
        self.animate()

        # Conversation display
        self.text_display = tk.Text(root, height=10, bg="black", fg="lime", font=("Courier", 12))
        self.text_display.pack(padx=10, pady=10)
        self.text_display.insert(tk.END, "K.A.R.A. is online...\n")

        # Start voice recognition in thread
        self.voice_thread = threading.Thread(target=self.listen_voice)
        self.voice_thread.daemon = True
        self.voice_thread.start()

        # Poll queue
        self.root.after(100, self.process_queue)

    def animate(self):
        self.label.config(image=self.frames[self.frame_index])
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.root.after(100, self.animate)

    def listen_voice(self):
        while True:
            data = stream.read(4000, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                import json
                text = json.loads(result).get("text", "")
                if text:
                    q.put(text)

    def process_queue(self):
        try:
            while True:
                user_input = q.get_nowait()
                self.text_display.insert(tk.END, f"You: {user_input}\n")
                reply = sarcastic_response(user_input)
                self.text_display.insert(tk.END, f"K.A.R.A.: {reply}\n")
                tts.say(reply)
                tts.runAndWait()
        except queue.Empty:
            pass
        self.root.after(100, self.process_queue)

# Start the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = AvatarGUI(root)
    root.mainloop()
