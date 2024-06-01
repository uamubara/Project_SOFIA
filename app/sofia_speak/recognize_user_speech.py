import os

import assemblyai as aai

class AssemblyAIIntegration:
    def __init__(self, on_final_transcription):
        aai.settings.api_key = os.environ.get("ASSEMBLYAI_API_KEY")
        self.transcriber = None
        self.on_final_transcription = on_final_transcription

    def start_transcription(self):
        self.transcriber = aai.RealtimeTranscriber(
            sample_rate=16000,
            on_data=self.on_data,
            on_error=self.on_error,
            on_open=self.on_open,
            on_close=self.on_close,
            end_utterance_silence_threshold=1000
        )
        self.transcriber.connect()
        microphone_stream = aai.extras.MicrophoneStream(sample_rate=16000)
        self.transcriber.stream(microphone_stream)

    def stop_transcription(self):
        if self.transcriber:
            self.transcriber.close()
            self.transcriber = None

    def on_open(self, session_opened: aai.RealtimeSessionOpened):
        print("Session ID:", session_opened.session_id)

    def on_data(self, transcript: aai.RealtimeTranscript):
        if not transcript.text:
            return
        if isinstance(transcript, aai.RealtimeFinalTranscript):
            print(f"Final Transcript: {transcript.text}")
            self.on_final_transcription(transcript.text)
        else:
            print(f"Interim Transcript: {transcript.text}", end="\r")

    def on_error(self, error: aai.RealtimeError):
        print("An error occurred:", error)

    def on_close(self):
        print("Transcription session closed.")
