import google.generativeai as genai
from .config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config={
        "temperature": 0.4,
        "max_output_tokens": 512,
    }
)

def ask_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(
            prompt,
            request_options={"timeout": settings.REQUEST_TIMEOUT}
        )
        return response.text
    except Exception as e:
        return f"Erro na IA: {str(e)}"
