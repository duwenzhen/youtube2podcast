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
import prompt_cons
import gemini_mcpclient

# youtube_url = "https://www.youtube.com/watch?v=0lJKucu6HJc"
# youtube_url = "https://www.youtube.com/watch?v=7mCQHeXq1Mg"


if __name__ == "__main__":

   search_prompt = "I am looking for a youtube video about the T100 San Francisco 2024"


   results = asyncio.run(gemini_mcpclient.run(search_prompt))
   youtube_url = results.content[0].text
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
      Read the themes 3 times, based on the transcript provided below, classify the video into one of the follow themes, just returns me the theme, no other word is necessary, again I just need the theme : {prompt_cons.THEMES_EXPLAINED}
      ** START of SUMMARY **
      {transcript}
      ** END of SUMMARY **
      -- END of INSTRUCTION --
      """


   results = asyncio.run(gemini_mcpclient.run(prompt1))

   theme = results.content[0].text
   if theme not in prompt_cons.THEMES:
      print("ERROR")
   else:
      print(theme)


   podcastInstruction = prompt_cons.instructionByTheme[theme].format(transcript)
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
Below this the transcript for a podcast, generate a podcast from it:
{playbook}
-- END of INSTRUCTION --
"""
   results = asyncio.run(gemini_mcpclient.run(prompt3))
   print(results)



