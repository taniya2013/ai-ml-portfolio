import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Read API Key
API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini Client
client = genai.Client(api_key=API_KEY)


def generate_all(text):

    combined_prompt = f"""
The transcript may contain speech recognition errors.

Before generating the output:
- Correct grammar and spelling.
- Correct obvious pronunciation mistakes.
- If "Anya" refers to the speaker's name, replace it with "Taniya".
- Use the corrected transcript for every output.

Generate output in this exact format:

SUMMARY:
(write short summary)

NOTES:
(use headings and bullet points)

Q&A:
(generate 5 interview question answers)

Transcript:
{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=combined_prompt
    )

    response_text = response.text

    try:
        summary = response_text.split("NOTES:")[0].replace("SUMMARY:", "").strip()

        notes_part = response_text.split("NOTES:")[1]
        notes = notes_part.split("Q&A:")[0].strip()

        qa = response_text.split("Q&A:")[1].strip()

    except Exception:
        summary = response_text
        notes = response_text
        qa = response_text

    return summary, notes, qa