import os
from dotenv import load_dotenv
from google import genai
from services.openrouter_service import (
    generate_openrouter_response
)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_response(prompt):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print("Gemini Error:")
        print(e)

    try:

        print(
            "Switching to OpenRouter..."
        )

        return generate_openrouter_response(
            prompt
        )

    except Exception as e:

        print(
            "OpenRouter Error:"
        )

        print(e)

        return """
All AI providers are busy right now.

Please try again after a few seconds.
"""