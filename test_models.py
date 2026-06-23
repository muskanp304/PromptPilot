from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

for model in [
    "gemini-2.5-flash",
    "gemini-flash-latest",
    "gemini-2.0-flash"
]:
    try:
        print(f"\nTesting {model}")

        response = client.models.generate_content(
            model=model,
            contents="Say hello"
        )

        print(response.text)

    except Exception as e:
        print(e)