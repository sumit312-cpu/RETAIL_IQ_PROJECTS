import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def ask_gemini(question, context):

    prompt = f"""
You are the AI assistant for the RetailIQ project.

Rules:

Answer ONLY from the provided context.
Do not invent information.
Use bullet points when appropriate.
If the answer is unavailable in the context,
  clearly say so.

Context:
{context}

Question:
{question}
"""

    models = [
        "gemini-3.5-flash",
        "gemini-3.5-flash-lite",
        "gemini-flash-latest"
    ]

    for model_name in models:

        for _ in range(2):

            try:

                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )

                return response.text

            except ServerError:
                time.sleep(2)

            except Exception:
                break

    return "⚠️ Gemini is currently unavailable. Please try again in a few minutes."