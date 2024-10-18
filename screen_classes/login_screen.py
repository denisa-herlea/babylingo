import threading
import keras
import librosa
import numpy as np
import pyaudio
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(255 / 255.0, 255 / 255.0, 255 / 255.0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = self.size
        self.rect.pos = self.pos


class IntroScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(255 / 255.0, 255 / 255.0, 255 / 255.0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = self.size
        self.rect.pos = self.pos


class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(255 / 255.0, 255 / 255.0, 255 / 255.0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = self.size
        self.rect.pos = self.pos


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_recording = False
        self.frames = []
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.model = keras.models.load_model('babylingo_model_waveform.keras')
        self.class_names = ['ambient_noise', 'belly_pain', 'burping', 'discomfort', 'hungry', 'tired']

    def start_recording(self):
        if self.is_recording:
            print("Recording is already in progress.")
            return

        self.is_recording = True
        self.frames = []

        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        CHUNK = 1024

        self.stream = self.audio.open(format=FORMAT, channels=CHANNELS,
                                      rate=RATE, input=True,
                                      frames_per_buffer=CHUNK)

        print("Recording started...")
        threading.Thread(target=self._record_and_predict).start()

    def _record_and_predict(self):
        CHUNK = 1024
        RATE = 44100
        TARGET_SR = 16000
        RECORD_SECONDS = 1

        while self.is_recording:
            frames = []
            for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = self.stream.read(CHUNK)
                frames.append(data)

            audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

            audio_data_resampled = librosa.resample(audio_data.astype(float), orig_sr=RATE, target_sr=TARGET_SR)
            audio_data_processed = self._process_audio(audio_data_resampled)

            prediction = self.model.predict(audio_data_processed)
            predicted_class = np.argmax(prediction, axis=1)

            predicted_category = self.class_names[predicted_class[0]]

            if predicted_category != 'ambient_noise':
                if predicted_category == 'tired' or predicted_category == 'hungry':
                    self.show_notification(f"Baby may cry because it's {predicted_category}")
                if predicted_category == 'belly' or predicted_category == 'burping' or predicted_category == 'discomfort':
                    self.show_notification(f"Baby may cry because of {predicted_category}")
            else:
                print(f"Predicted category is 'ambient_noise', notification will not be shown.")

    def _process_audio(self, audio_data, target_len=16000):
        audio_data_fixed_length = librosa.util.fix_length(audio_data, size=target_len)
        return np.expand_dims(audio_data_fixed_length, axis=0)

    def stop_recording(self):
        if not self.is_recording:
            print("No recording in progress.")
            return

        self.is_recording = False
        print("Recording stopped.")

        if self.stream:
            self.stream.stop_stream()
            self.stream.close()

    def show_notification(self, message):
        notification_bar = self.ids.notification_bar
        label = notification_bar.children[0]

        label.text = message
        notification_bar.height = 200

        threading.Timer(7.0, self.hide_notification).start()

    def hide_notification(self):
        notification_bar = self.ids.notification_bar
        notification_bar.height = 0
