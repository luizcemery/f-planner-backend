import google.generativeai as genai
from fastapi import FastAPI

genai.configure(api_key="AIzaSyAIRdXZBcFJHshlcWzkdQnVYlas7oSBv5I")

app = FastAPI()

@app.get("/ask")
def ask(prompt: str):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return {"response": response.text}
