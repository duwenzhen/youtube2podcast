from google import genai
from google.genai import types
import wave
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.environ["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

async def get_response_from_flash_model(prompt : str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0,
        ),
    )
    return response.text


async def get_response_from_gemini_youtube(prompt : str, YOUTUBE_VIDEO_URL :str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
        types.Part.from_uri(
            file_uri=YOUTUBE_VIDEO_URL,
            mime_type="video/webm",
        ),
        prompt,
    ],
    )
    return response.text

async def get_response_from_pro_model(prompt : str):
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0,
        ),
    )
    return response.text

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

async def get_response_from_text_to_sppech_model(prompt : str):
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                    speaker_voice_configs=[
                        types.SpeakerVoiceConfig(
                            speaker='Joe',
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                    voice_name='Kore',
                                )
                            )
                        ),
                        types.SpeakerVoiceConfig(
                            speaker='Jane',
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                    voice_name='Puck',
                                )
                            )
                        ),
                    ]
                )
            )
        )
    )
    data = response.candidates[0].content.parts[0].inline_data.data
    filename = "out.wav"
    wave_file(filename, data)
    return filename