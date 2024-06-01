import os

import openai


class OpenAIIntegration:
    def __init__(self):
        openai.api_key = os.environ.get('your_openai_api_key')
        self.full_transcript = [
            {"role": "system", "content": "You are a 24-year-old, female virtual assistant named Sofia. Sofia is an acronym for A Smart Operational Framework for Intelligent Assistance. You are to assist the user. Similar to Jarvis from iron man movie but female version.  Be kind, funny, and flirty. Don't use emojis in your response."},
        ]

    def generate_ai_response(self, transcript):
        self.full_transcript.append({"role": "user", "content": transcript})
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.full_transcript,
            temperature=0.7,
            max_tokens=150,
        )
        ai_response = response.choices[0].message.content
        self.full_transcript.append({"role": "assistant", "content": ai_response})
        print(f"AI Response: {ai_response}")
        return ai_response
