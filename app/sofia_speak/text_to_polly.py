import boto3
import os


class AmazonPollyIntegration:
    def __init__(self):
        self.polly_client = boto3.client(
            'polly',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            region_name=os.environ.get('AWS_REGION_NAME', 'us-east-1')
        )

    def generate_audio(self, text):
        response = self.polly_client.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId="Ruth",
            Engine='neural'
        )
        audio_stream = response.get('AudioStream')
        with open("response.mp3", "wb") as file:
            file.write(audio_stream.read())
        print("Audio generated and saved as response.mp3")
