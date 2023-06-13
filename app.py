from IPython.display import Audio
import openai
import requests
import json
import os


# Set up OpenAI API credentials
openai.api_key = "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"

# Set up ElevenLabs API credentials
elevenlabs_api_key = "3ea525bd0795cc4367ca2016f0327d96"

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def text_to_speech(text):
    url = 'https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM/stream?optimize_streaming_latency=0'
    headers = {
        'accept': '*/*',
        'xi-api-key': elevenlabs_api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'text': text,
        'model_id': 'eleven_monolingual_v1',
        'voice_settings': {
            'stability': 0,
            'similarity_boost': 0
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.content

# Main conversation loop
while True:
    user_input = input('User: ')
    response = generate_response(user_input)
    print('ChatGPT: ' + response)
    speech = text_to_speech(response)
    audio = Audio(data=speech, autoplay=True)
    display(audio)
