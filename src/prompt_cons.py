
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
   ,
"Music"  :
"""
Transform the following raw YouTube video transcript on the theme of "Music" into a polished and engaging podcast script. The podcast features two speakers: Jane, the insightful host who guides the conversation, and Joe, the expert guest and music critic who provides in-depth analysis.

Your task is to:

Assign Roles: Convert the monologue or unstructured dialogue of the source transcript into a dynamic, two-person conversation. Jane should introduce topics, ask probing questions, and provide transitions. Joe should answer these questions, offering the core analysis, expert opinion, and detailed commentary found in the original text.
Create Natural Dialogue: Do not simply split the text. Rewrite it to create a believable back-and-forth. Invent questions for Jane that logically lead to Joe's explanations. Add interjections, agreements, and follow-up thoughts to make the conversation flow naturally (e.g., Jane: "That's fascinating, Joe. So, are you saying the lyrical dissonance is intentional?" or Joe: "Exactly, and if you listen closely to the bridge...").
Structure the Narrative: Organize the original transcript's key points—whether about a music video's symbolism, a live performance's energy, a cover's reinterpretation, or lyrical analysis—into a coherent narrative arc for a podcast episode, complete with a clear introduction, a deep-dive middle section, and a concluding summary.
Maintain Content Integrity: Ensure all critical analysis, facts, and opinions from the source transcript are faithfully represented in the dialogue between Jane and Joe. The final script should be a high-fidelity, yet more engaging, version of the original content.
Here is the source transcript to be converted:
--- START of Transcript ---
{}
--- START of Transcript ---
""",
"Entertainment & Comedy" :
"""
Transform the following YouTube video transcript on the theme of "Entertainment & Comedy" into a complete podcast script. The script will feature two speakers: Jane, the witty host and pop culture enthusiast who sets the scene, and Joe, the sharp-witted guest (e.g., a comedian or industry insider) who provides the core critique and humorous analysis.

Your detailed instructions are to:

Establish a Comedic Dynamic: Convert the source transcript into a lively, humorous dialogue. Jane's role is to act as the audience's proxy, setting up premises, asking questions about comedic timing, and reacting to the content. Joe's role is to deliver the punchlines, provide the insider analysis, and explain the mechanics of the comedy or entertainment piece being discussed.
Deconstruct and Reconstruct Jokes: Do not simply copy-paste jokes. Have Jane introduce the context or premise of a sketch, prank, or stand-up bit, allowing Joe to deliver the punchline or the critical observation from the original transcript. Crucially, you must script the non-verbal cues and reactions (e.g., [Jane laughs], [A beat of silence for comedic effect], Joe: (deadpan)) that are essential for comedic pacing.
Analyze the Entertainment: The dialogue must go beyond recitation. Weave in analysis from the source transcript by having Jane pose questions like, "From a writing perspective, what makes that sketch so clever?" or "Why do you think that particular viral challenge captured the public's imagination?" Joe should then provide the in-depth explanation.
Adapt to the Sub-Genre: Tailor the conversation to the specific type of entertainment. If it's a celebrity interview, the dialogue might focus on humorous anecdotes. If it's a movie review, it could be a comedic debate. If it's a stand-up analysis, they should break down the structure of a specific joke.
Create a Narrative Flow: Structure the script with a clear beginning (hooking the listener with a funny clip or premise), middle (the detailed breakdown and humorous back-and-forth), and end (a summary of why the piece of entertainment succeeds or fails), ensuring all key points from the source transcript are included in a logical and engaging conversational sequence.
Here is the source transcript to be converted:
--- START of Transcript ---
{}
--- START of Transcript ---
""",
"Gaming"  :
   """
   Transform the following YouTube video transcript on the theme of "Gaming" into a dynamic, ready-to-record podcast script. The podcast features two speakers: Jane, the curious host who represents the everyday player, and Joe, the seasoned gaming analyst and strategist who provides the expert commentary.

Your detailed instructions are to:

Translate Visuals to Audio: Your primary challenge is to convert visual gameplay into compelling audio. Jane should prompt for descriptions of the on-screen action, environment, or UI (e.g., "Joe, describe this boss battle for us," or "What makes this level's design so effective?"). Joe must then provide vivid, "theater-of-the-mind" narration that explains the gameplay, strategies, and visual spectacle detailed in the source transcript.
Define a Clear Dynamic: Structure the conversation based on the type of gaming content.
For Reviews/Analysis: Jane asks targeted questions about game mechanics, narrative, graphics, and value, prompting Joe to deliver the detailed critical assessment from the transcript.
For Gameplay/Walkthroughs: Jane acts as a co-op partner or observer, asking about Joe's strategy ("Why did you choose that weapon?") or reacting to in-game events, allowing Joe to explain his thought process and actions.
For Esports/Trends: Frame the dialogue as a high-level analytical discussion. Jane introduces the topic (a specific match, a player's performance, or a new industry trend), and Joe provides the in-depth, expert breakdown.
Create Authentic Gamer Dialogue: Rewrite the transcript into a natural back-and-forth. Inject common gaming vernacular and reactions where appropriate. Turn declarative statements from the transcript into discussions. For example, instead of a simple statement about a "difficulty spike," have Jane say, "I heard the third act has a serious difficulty spike. Is that true?" leading to Joe's detailed explanation.
Structure for Engagement: Organize the script with a clear narrative arc. Start with a hook (e.g., a bold opinion on a game, a description of an epic moment), move into the detailed analysis and gameplay breakdown in the middle, and conclude with a final verdict, a key takeaway, or a look at the future, ensuring all core information from the transcript is seamlessly integrated.
Here is the source transcript to be converted:
--- START of Transcript ---
{}
--- START of Transcript ---
   """,
"News & Current Events" :
   """
   Transform the following YouTube video transcript on the theme of "News & Current Events" into a professional and insightful podcast script. The podcast will feature two speakers: Jane, the lead anchor/journalist who grounds the conversation in fact, and Joe, the expert analyst or commentator who provides in-depth political or social analysis.

Your detailed instructions are to:

Establish Journalistic Roles: Cast Jane as the primary anchor. Her lines should focus on presenting the core, verifiable facts of the story (the who, what, where, when) as laid out in the transcript. Cast Joe as the expert analyst. His lines should consist of the opinion, historical context, and political analysis from the transcript, providing the "why it matters" and "what's next."
Separate Fact from Analysis: This is crucial. Structure the dialogue so Jane first lays out a factual premise or reports a recent development. She should then pose a direct, open-ended question to Joe, teeing him up to provide his analysis. For example, Jane: "Joe, the official report cites a 5% increase in unemployment. What are the underlying economic factors driving that number?" Joe then delivers the detailed analysis from the source material.
Maintain Factual Integrity: All statistics, names, dates, and direct quotations mentioned in the source transcript must be preserved with absolute accuracy in the final script. Attribute direct quotes clearly within the dialogue.
Build a Logical Narrative: Deconstruct the original transcript to identify the core issue, the main arguments, and the key stakeholders. Reassemble these points into a structured conversation that flows logically from introduction of the topic, to background information, to core analysis of the current situation, and finally to a discussion of potential future outcomes.
Inject Professional Dialogue: Create a tone that is authoritative, balanced, and respectful. The questions you invent for Jane should be probing and intelligent, designed to elicit the most insightful commentary from Joe. The back-and-forth should feel like a genuine, high-quality news program, not just a reading of the original text.
Here is the source transcript to be converted:
--- START of Transcript ---
{}
--- START of Transcript ---
""",

"Lifestyle & Vlogging" : """
Transform the following YouTube video transcript on the theme of "Lifestyle & Vlogging" into a relaxed, personal, and engaging podcast script. The script will feature two speakers: Jane, the warm and inquisitive host who asks questions like a close friend, and Joe, who embodies the role of the "vlogger," sharing his personal experiences and reflections.

Your detailed instructions are to:

Convert Monologue to Dialogue: The source transcript is likely a personal, first-person narrative (a daily vlog, travel diary, or routine). Your task is to split this internal monologue into a natural conversation. Jane's role is to ask the questions a curious friend or viewer would, prompting Joe to share the feelings, motivations, and details of his experience.
Translate Visuals into Storytelling: Vlogs are highly visual. You must convert the "showing" into "telling." Create dialogue where Jane asks for sensory details about what's happening (e.g., "You mentioned the sunrise view; can you describe what that looked like?" or "What was the atmosphere like in that cafe?"). Joe's replies should be descriptive and narrative-driven, painting a picture for the listener using the details from the source transcript.
Explore the 'Why' Behind the 'What': A simple list of activities is not engaging. The dialogue must delve into the purpose and feeling behind the actions. Jane should pose questions that explore motivation, such as, "What is it about that morning routine that sets you up for the day?" or "What made you choose that specific travel destination over others?" This allows Joe to share the deeper insights and personal philosophy present in the original vlog.
Maintain an Authentic & Intimate Tone: The final script's tone should be casual, relatable, and authentic, mirroring the personal nature of a vlog. It should feel less like a formal interview and more like a comfortable chat between two friends, where one is sharing a personal story with the other. The goal is to make the listener feel like they are part of a warm, personal conversation.
Here is the source transcript to be converted:
--- START of Transcript ---
{}
--- START of Transcript ---
""",
"Sports" :
   """
Transform the following YouTube video transcript on the theme of "Sports" into a high-energy and insightful podcast script. The script will feature two speakers whose roles are adapted to the content: Jane, the energetic host or play-by-play announcer, and Joe, the expert analyst or color commentator.

Your detailed instructions are to:

Dynamically Assign Roles Based on Content: Your primary task is to adapt the speaker roles to fit the specific type of sports video:
For Game Highlights: Cast Jane as the play-by-play announcer, vividly describing the action. Cast Joe as the color commentator, providing immediate analysis, strategic insights, and context for the plays.
For Match Analysis/Commentary: Frame it as a studio debate. Jane is the host who introduces topics, presents statistics, and poses critical questions. Joe is the expert analyst who provides in-depth opinions and tactical breakdowns based on the transcript's content.
For Athlete Interviews: Jane becomes the interviewer, asking the questions from the transcript. Joe's dialogue should be crafted directly from the athlete's answers, transforming a simple Q&A into a more personal, conversational interview.
For Fitness/Training: Jane acts as the motivated trainee or curious enthusiast, asking questions about technique, benefits, and the science behind the exercises. Joe is the expert coach, clearly and encouragingly explaining the workout instructions from the transcript.
Translate Visual Action into Compelling Audio: For visual-heavy content, convert the physical action into "theater-of-the-mind" audio. Jane should narrate the crucial moments (e.g., "He's making a break down the wing!"), allowing Joe to interject with analysis on form, strategy, or what makes the moment significant.
Integrate Data and Statistics Naturally: Sports analysis is data-rich. Weave any stats, scores, or performance metrics from the source transcript directly into the dialogue. For example, Jane might state a key statistic, which then serves as a launchpad for Joe's deeper analysis of what those numbers actually mean.
Capture the Passion and Energy: The dialogue must reflect the excitement of sports. Use dynamic language, script believable reactions to pivotal moments (e.g., [Joe: Unbelievable!]), and foster a back-and-forth that feels like a live broadcast or a spirited debate between two knowledgeable and passionate experts.
Here is the source transcript to be converted:
   --- START of Transcript ---
{}
--- START of Transcript ---
   """,
"Science & Technology" :
   """
   Transform the following YouTube video transcript on the theme of "Science & Technology" into a clear, engaging, and informative podcast script. The script will feature two speakers: Jane, the inquisitive host who represents the curious and intelligent audience, and Joe, the expert science communicator or tech analyst who breaks down complex topics.

Your detailed instructions are to:

Prioritize Clarity and Accuracy: Your foremost task is to ensure all scientific principles, technical specifications, data points, and terminology from the source transcript are preserved with absolute precision. The objective is to make complex information accessible without sacrificing technical correctness.
Structure for Explanation and Simplification: Create a dynamic where Jane acts as the audience's advocate for clarity. Her questions should actively deconstruct complex topics, prompting Joe for analogies, definitions, and simpler explanations (e.g., Jane: "That's fascinating, Joe. Can you walk me through a real-world example of how that algorithm is used?"). Joe's role is to provide these clear, structured explanations drawn from the source material.
Adapt to the Content Format: Tailor the conversational flow to the specific type of Sci-Tech video:
For Tech Tutorials: Convert the linear steps into an interactive, guided walkthrough. Jane should act as the user, asking "What's the next step?" or confirming the process ("So, the command is -v for verbose output, correct?"), while Joe provides the clear, step-by-step instructions as the expert guide.
For Product Reviews: Structure the dialogue as a hands-on evaluation. Jane should ask about specific features, user experience, performance benchmarks, and comparisons to competitors, prompting Joe to provide the detailed review points from the transcript.
For Scientific Explanations: Frame the conversation as a journey of discovery. Jane should guide the listener from a broad question to a detailed conclusion, allowing Joe to build the explanation layer by layer.
Create an Engaging and Intelligent Dialogue: The tone should be one of intellectual curiosity and enthusiasm for learning. The back-and-forth should make the listener feel like they are part of a stimulating conversation that respects their intelligence while making challenging subjects understandable and exciting.
Here is the source transcript to be converted:
--- START of Transcript ---
{}
--- START of Transcript ---
   """,
"Travel & Events" :
   """
   Transform the following YouTube video transcript on the theme of "Travel & Events" into an immersive, practical, and culturally rich podcast script. The script will feature two speakers: Jane, the enthusiastic travel planner who asks the practical questions a listener would have, and Joe, the seasoned traveler or on-the-ground correspondent who shares the experiences and insights.

Your detailed instructions are to:

Evoke a Sense of Place Through Sensory Detail: Your primary goal is to transport the listener. Go beyond visual descriptions found in the transcript and convert them into a multi-sensory audio experience. Jane should actively prompt for these details, asking questions like, "What were the sounds of the old city in the morning?" or "Can you describe the taste and smell of that street food you tried?" Joe's role is to provide vivid, narrative answers that paint a complete picture.
Structure for Practical, Actionable Advice: Frame the conversation as a useful guide for potential travelers. Jane should systematically inquire about the practical tips contained within the transcript, covering key topics such as budgeting, transportation, accommodation recommendations, local etiquette, and "must-do" activities. For event coverage, this should include advice on ticketing, navigating crowds, and can't-miss moments.
Weave in Cultural and Historical Storytelling: Elevate the script from a simple itinerary to a cultural exploration. The dialogue must delve into the context of the destination or event. Jane should pose questions that probe deeper, such as, "What's the historical significance of that landmark?" or "What local custom or tradition did you find most meaningful?" This allows Joe to share the richer, more insightful stories from the source transcript.
Create an Immersive "You Are There" Feel: For content covering festivals, concerts, or specific events, create a dynamic that feels like a live report. Jane can ask about the energy of the crowd, the standout performances, or the overall atmosphere, while Joe provides an enthusiastic, on-the-scene account of the experience, making the listener feel as if they are right there in the middle of the action.
Here is the source transcript to be converted:
--- START of Transcript ---
{}
--- START of Transcript ---
   """,

"Food & Cooking" :
   """
Transform the following YouTube video transcript on the theme of "Food & Cooking" into a savory, descriptive, and engaging podcast script. The script will feature two speakers: Jane, the enthusiastic home cook and foodie who asks about process and flavor, and Joe, the expert chef or food critic who provides the culinary guidance and sensory details.

Your detailed instructions are to:

Engage All Senses Through Audio: Your most crucial task is to translate the visual appeal of food into compelling audio. Jane's questions must be designed to elicit rich, descriptive language from Joe about taste, aroma, texture, and even sound (e.g., Jane: "You say the sauce is ready, but what aroma should I be looking for?" or "Describe the texture of that dish."). Joe's responses should be highly evocative, making the listener's mouth water.
Adapt the Dialogue to the Culinary Format: Tailor the conversational structure to the specific type of content:
For Recipes/Tutorials: Frame the script as an interactive cook-along. Jane should act as the home cook, asking questions like, "My garlic is fragrant, what's the next step, Chef?" or "How do I know when the chicken is perfectly cooked?" This prompts Joe to provide clear, sequential instructions, along with any 'pro tips' or explanations of technique found in the source transcript.
For Restaurant Reviews: Structure the conversation as a trusted recommendation. Jane should ask the practical questions a potential diner would have ("What's the ambiance like?" "Is it worth the price?" "What's the one dish we absolutely must order?"), allowing Joe to deliver the detailed critique.
For Food Challenges or Cuisine Explorations: Format it as a narrative of discovery. Jane prompts Joe to recount his experience, asking about the history of a dish, the rules of a challenge, or the standout flavors he encountered.
Explain the "Why" Behind the "How": A great cooking podcast teaches more than just steps. The dialogue must explore the culinary science and reasoning behind the techniques. Jane should ask questions like, "Why is it so important to let the meat rest?" or "What does blooming the spices actually do for the final flavor?" This enables Joe to share the deeper knowledge contained within the transcript.
Here is the source transcript to be converted:
--- START of Transcript ---
{}
--- START of Transcript ---
   """
}

