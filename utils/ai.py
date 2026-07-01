# pyrefly: ignore [missing-import]
from ollama import chat
import json
import os
import google.generativeai as genai


def analyze_resume(score, matched_skills, missing_skills):

    prompt = f"""
You are an ATS Resume Expert.

The ATS has already calculated everything.

ATS Score:
{score}

Matched Skills:
{matched_skills}

Missing Skills:
{missing_skills}

Generate ONLY:

1. Three strengths
2. Three weaknesses
3. Five suggestions

Return ONLY valid JSON.

{{
    "strengths":[
        "",
        "",
        ""
    ],

    "weaknesses":[
        "",
        "",
        ""
    ],

    "suggestions":[
        "",
        "",
        "",
        "",
        ""
    ]
}}
"""

    gemini_key = os.getenv("GEMINI_API_KEY")

    if gemini_key:
        print("☁️ Using Google Gemini API Cloud Service...")
        genai.configure(api_key=gemini_key)
        
        # Using gemini-1.5-flash for speed and reliability, set up to return JSON
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            generation_config={"response_mime_type": "application/json"}
        )
        
        response = model.generate_content(prompt)
        content = response.text
    else:
        print("💻 Using local Ollama...")
        response = chat(
            model="llama3:latest",
            format="json",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        content = response.message.content

    print(content)

    return json.loads(content)