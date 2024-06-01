import os

from app.sofia_speak.open_ai import OpenAIIntegration
from app.sofia_speak.recognize_user_speech import AssemblyAIIntegration
from app.sofia_speak.text_to_polly import AmazonPollyIntegration

# Instantiate integration classes
openai_integration = OpenAIIntegration()
amazonpolly_integration = AmazonPollyIntegration()


def handle_final_transcription(transcript_text):
    # Generate AI response based on transcribed text
    ai_response_text = openai_integration.generate_ai_response(transcript_text)

    # Generate audio from AI response
    amazonpolly_integration.generate_audio(ai_response_text)

    # Play the generated audio
    os.system("start response.mp3")


def main():
    # Instantiate AssemblyAIIntegration with the callback function
    assemblyai_integration = AssemblyAIIntegration(on_final_transcription=handle_final_transcription)

    # Generate initial greeting using OpenAI and Polly
    greeting = "Hey, I'm Sofia....A Smart Operational Framework for Intelligent Assistance. how may I assist you today?"
    ai_response_text = openai_integration.generate_ai_response(greeting)
    amazonpolly_integration.generate_audio(ai_response_text)
    os.system("start response.mp3")

    # Start transcription to listen for user's voice input
    assemblyai_integration.start_transcription()


if __name__ == "__main__":
    main()
