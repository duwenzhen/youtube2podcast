import asyncio
import os
# Add json import for formatting output
import json
from datetime import datetime
from google import genai
from google.genai import types
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from dotenv import load_dotenv
import markdown
from google import genai
from google.genai import types
import wave
import gemini_mcpclient

youtube_url = "https://www.youtube.com/watch?v=0lJKucu6HJc"

THEMES_EXPLAINED = """Entertainment & Comedy: This broad category encompasses a wide range of videos designed to amuse and entertain. It includes scripted sketches, stand-up comedy, pranks, viral challenges, and content centered around pop culture, celebrities, and movies.
Music: As one of YouTube's foundational pillars, this theme is dedicated to official music videos, live performances, cover songs, lyric videos, and music-related analysis or commentary.
Education & How-To: This theme is for content where the primary goal is to impart knowledge or teach a skill. It includes everything from academic subjects and complex scientific concepts to practical DIY projects, software tutorials, and life hacks.
Gaming: A massive and dedicated community on YouTube, this category covers all aspects of video games. This includes gameplay videos (let's plays), walkthroughs, reviews, esports coverage, and analysis of gaming trends.
News & Current Events: This category is for videos that report on and analyze recent events. It includes content from established news organizations, independent commentators, political analysis, and discussions of pressing social issues.
Lifestyle & Vlogging: This theme captures the wide world of personal-diary-style content. It includes daily vlogs, travel diaries, "a day in the life" videos, and content focused on personal routines, health, and wellness.
Sports: Dedicated to all forms of athletic activity, this category features game highlights, match analysis, athlete interviews, fitness training videos, and commentary on various sports leagues and events.
Science & Technology: This theme is for content that explores the worlds of scientific discovery and technological innovation. It includes product reviews, tech tutorials, scientific explanations, and discussions on future technology.
Travel & Events: This category encompasses videos that showcase destinations around the world and document various events. It includes travel guides, cultural explorations, festival coverage, and vlogs from specific trips.
Food & Cooking: A highly popular and engaging category, this theme is centered around the culinary arts. It includes recipe tutorials, cooking shows, restaurant reviews, food challenges, and explorations of different cuisines.
"""

THEMES = {
"Entertainment & Comedy" : "This broad category encompasses a wide range of videos designed to amuse and entertain. It includes scripted sketches, stand-up comedy, pranks, viral challenges, and content centered around pop culture, celebrities, and movies.",
"Music" : "As one of YouTube's foundational pillars, this theme is dedicated to official music videos, live performances, cover songs, lyric videos, and music-related analysis or commentary.",
"Education & How-To"  : "This theme is for content where the primary goal is to impart knowledge or teach a skill. It includes everything from academic subjects and complex scientific concepts to practical DIY projects, software tutorials, and life hacks.",
"Gaming"  : "A massive and dedicated community on YouTube, this category covers all aspects of video games. This includes gameplay videos (let's plays), walkthroughs, reviews, esports coverage, and analysis of gaming trends.",
"News & Current Events" : "This category is for videos that report on and analyze recent events. It includes content from established news organizations, independent commentators, political analysis, and discussions of pressing social issues.",
"Lifestyle & Vlogging" : "This theme captures the wide world of personal-diary-style content. It includes daily vlogs, travel diaries, 'a day in the life' videos, and content focused on personal routines, health, and wellness.",
"Sports" : "Dedicated to all forms of athletic activity, this category features game highlights, match analysis, athlete interviews, fitness training videos, and commentary on various sports leagues and events.",
"Science & Technology" : "This theme is for content that explores the worlds of scientific discovery and technological innovation. It includes product reviews, tech tutorials, scientific explanations, and discussions on future technology.",
"Travel & Events" : "This category encompasses videos that showcase destinations around the world and document various events. It includes travel guides, cultural explorations, festival coverage, and vlogs from specific trips.",
"Food & Cooking" : "A highly popular and engaging category, this theme is centered around the culinary arts. It includes recipe tutorials, cooking shows, restaurant reviews, food challenges, and explorations of different cuisines."
}


# prompt to generate prompt
# Act as an expert podcast producer, share your expertise by giving me just a prompt, no other word is necessary, just the prompt which will convert a YouTube video to a podcast transcript between 2 speakers, Jane and Joe, the theme : Education & How-To: This theme is for content where the primary goal is to impart knowledge or teach a skill. It includes everything from academic subjects and complex scientific concepts to practical DIY projects, software tutorials, and life hacks.


instructionByTheme = {
"Education & How-To"  :
"""
You are an expert podcast scriptwriter. Your task is to convert the following YouTube video transcript into a polished, two-person podcast transcript.

Theme: Education & How-To
Hosts:

Jane: The subject matter expert. She clearly and patiently explains the topic, breaking down complex information and providing step-by-step instructions.
Joe: The curious co-host and audience surrogate. He asks clarifying questions, voices common uncertainties, and helps guide the conversation from a learner's perspective.
Instructions:

Analyze the key educational points, concepts, and step-by-step instructions from the provided video content.
Restructure this information into a natural, engaging dialogue between Jane and Joe.
Jane should deliver the primary instructional content.
Joe should interject with questions that anticipate a listener's confusion, ask for examples, or prompt deeper explanations (e.g., "So, just to be clear...", "How would that work if...", "What's the most common mistake people make here?").
Ensure the transcript begins with a brief introduction by the hosts and concludes with a summary of the main takeaways.
Format the output strictly as a transcript, with each line preceded by 'Jane:' or 'Joe:'. Do not add any other narrative, commentary, or headers.
--- START of Transcript ---
{}
--- START of Transcript ---
"""

}



if __name__ == "__main__":

   prompt0 =  f"""
      Send the instruction below to gemini youtube model :
      -- START of INSTRUCTION --
      Give me the transcript of this youtube video {youtube_url} ,please
      -- END of INSTRUCTION --
      """
   results = asyncio.run(gemini_mcpclient.run(prompt0))

   transcript = results.content[0].text


   prompt1 =  f"""
      Send the instruction below to gemini flash model :
      -- START of INSTRUCTION --
      Read the themes 3 times, based on the transcript provided below, classify the video into one of the follow themes, just returns me the theme, no other word is necessary, again I just need the theme : {THEMES_EXPLAINED}
      ** START of SUMMARY **
      {transcript}
      ** END of SUMMARY **
      -- END of INSTRUCTION --
      """


   results = asyncio.run(gemini_mcpclient.run(prompt1))

   theme = results.content[0].text
   if theme not in THEMES:
      print("ERROR")


   podcastInstruction = instructionByTheme[theme].format(transcript)
   prompt2 = \
f"""
Send the instruction below to gemini flash model :
-- START of INSTRUCTION --

{podcastInstruction}

-- END of INSTRUCTION --
"""

   results = asyncio.run(gemini_mcpclient.run(prompt2))

   playbook = results.content[0].text

   prompt3 = \
f"""
Send the instruction below to gemini TTS model :
-- START of INSTRUCTION --
Below this the playbook and transcript for a podcast, generate a podcast from it :
{playbook}
-- END of INSTRUCTION --
"""
   results = asyncio.run(gemini_mcpclient.run(prompt3))
   print(results)




















#
# # Load environment variables from .env file
# load_dotenv()
#
# api_key = os.environ["GEMINI_API_KEY"]
# print(api_key)
# client = genai.Client(api_key=api_key)
#
# # Set up the wave file to save the output:
# def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
#    with wave.open(filename, "wb") as wf:
#       wf.setnchannels(channels)
#       wf.setsampwidth(sample_width)
#       wf.setframerate(rate)
#       wf.writeframes(pcm)
#
#
# prompt = """Act like experienced podcast producer, below is your playbook, please make a podcast between Joe and Jane:
#
# ** beginning of the playbook **
#
# Podcast Production Playbook: The Situation Room
# Episode: #24-081: "The Iran Ultimatum"
# Record Date: 22 JUN 2025
# Air Date: 22 JUN 2025
# Hosts: Joe (J), Jane (N)
# Topic: Special Report on Presidential Address regarding military strikes on Iran.
#
# SCRIPT & CUES
# Time	Speaker	Dialogue & Production Cues
# 00:00	-	[COLD OPEN]&lt;br/>**[SFX: NEWS BULLETIN STINGER - URGENT, THREE-TONE CHIME]**
# 00:02	JOE	(Urgent, deliberate pace)&lt;br/>"And we're breaking into our regular programming for what is truly a stunning development. Just moments ago, the President concluded a sudden, late-night address to the nation, announcing a major military strike against Iran."
# 00:14	-	[MUSIC: MAIN THEME - DRIVING, SERIOUS NEWS BEAT - SWELLS AND FADES TO BED UNDERNEATH]
# 00:20	JANE	(Crisp, factual tone)&lt;br/>"That's right, Joe. The core announcement was that the U.S. military has conducted what were described as 'massive precision strikes' on three of Iran's key nuclear facilities—Fordow, Natanz, and Esfahan."
# 00:32	-	[AUDIO CUE: INSERT ACTUALITY 1 - POTUS SPEECH CLIP]&lt;br/>POTUS (CLIP): "...completely and totally obliterated."
# 00:36	JOE	(Analytical)&lt;br/>"And the stated objective was incredibly direct. The President said the mission's goal was the complete 'destruction of Iran's nuclear enrichment capacity' to, in his words, 'stop the nuclear threat from the world's number one state sponsor of terror.' He framed it as an absolute necessity."
# 00:54	JANE	"He certainly did, and he justified the action by pointing to what he called Iran's '40-year history of hostility.' He specifically referenced chants of 'death to America, death to Israel' and accused Iran of being directly responsible for the deaths of over a thousand American soldiers from roadside bombs."
# 01:13	-	[MUSIC: BED SHIFTS TO A MORE TENSE, DRAMATIC UNDERSCORE]
# 01:15	JOE	"And from that justification, he moved to a very stark ultimatum. He called Iran 'the bully of the Middle East' and stated they 'must now make peace.' He warned that if they don't, future attacks would be 'far greater and a lot easier,' presenting a choice of 'either peace or... tragedy for Iran.'"
# 01:34	JANE	(Connecting the dots)&lt;br/>"The address also made a point of acknowledging key partners and military figures. The President specifically thanked Israeli Prime Minister Benjamin Netanyahu, saying they 'worked as a team,' and congratulated the Israeli military. He also gave high praise to the U.S. military and singled out the Chairman of the Joint Chiefs of Staff, General Dan Raisenkaine, for his role in the attack."
# 01:56	JOE	(Pacing slows, adds weight)&lt;br/>"It's a truly gravity-defining moment. The President has drawn a very clear and aggressive line in the sand. An action of this magnitude, followed by such a direct ultimatum, puts the entire region, and arguably the world, on an incredibly uncertain path forward. The next 24 hours will be critical."
# 02:18	-	[MUSIC: MAIN THEME SWELLS TO FULL, PLAYS FOR 10 SECONDS, THEN FADES TO END]
# 02:28	-	[END OF EPISODE]
#
# Export to Sheets
# Producer's Notes:
#
# Pacing is key. The top of the show needs to feel urgent and breaking. Joe's final lines should slow down to convey the seriousness of the situation.
# Actuality 1: The POTUS clip is essential. Make sure the audio is clean and it cuts in sharply after Jane's line for maximum impact.
# Music Bed: The music should support the tone, not overpower it. Ensure the shift at 1:13 is subtle but effective in building tension. Check levels in post.
#
# ** end of the playbook **
#
#
#          """
#
# response = client.models.generate_content(
#    model="gemini-2.5-flash-preview-tts",
#    contents=prompt,
#    config=types.GenerateContentConfig(
#       response_modalities=["AUDIO"],
#       speech_config=types.SpeechConfig(
#          multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
#             speaker_voice_configs=[
#                types.SpeakerVoiceConfig(
#                   speaker='Joe',
#                   voice_config=types.VoiceConfig(
#                      prebuilt_voice_config=types.PrebuiltVoiceConfig(
#                         voice_name='Kore',
#                      )
#                   )
#                ),
#                types.SpeakerVoiceConfig(
#                   speaker='Jane',
#                   voice_config=types.VoiceConfig(
#                      prebuilt_voice_config=types.PrebuiltVoiceConfig(
#                         voice_name='Puck',
#                      )
#                   )
#                ),
#             ]
#          )
#       )
#    )
# )
#
# data = response.candidates[0].content.parts[0].inline_data.data
#
# file_name='out.wav'
# wave_file(file_name, data) # Saves the file to current directory