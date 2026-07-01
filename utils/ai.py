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

    if not gemini_key:
        raise ValueError("GEMINI_API_KEY environment variable is missing. Please configure it in your environment or .env file.")

    print("☁️ Using Google Gemini API Cloud Service...")
    genai.configure(api_key=gemini_key)
    
    # Using gemini-1.5-flash for speed and reliability, set up to return JSON
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        generation_config={"response_mime_type": "application/json"}
    )
    
    response = model.generate_content(prompt)
    content = response.text

    print(content)

    return json.loads(content)


def extract_name(resume_text):
    # Grab the top part of the resume where the name always resides
    header = resume_text[:800].strip()

    prompt = f"""
You are an expert resume parser. Extract the full name of the candidate from the following top section of their resume.
Do NOT include any commentary, labels, or extra text. Return ONLY the extracted name (e.g. "John Doe"). If you cannot find a name, return "Candidate".

Resume Header Section:
---
{header}
---
Extracted Name:"""

    gemini_key = os.getenv("GEMINI_API_KEY")
    try:
        if not gemini_key:
            raise ValueError("GEMINI_API_KEY is not set.")

        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel(model_name='gemini-1.5-flash')
        response = model.generate_content(prompt)
        name = response.text.strip()

        # Clean up any quotes or labels the AI might have accidentally appended
        name = name.replace('"', '').replace("'", "")
        if len(name) > 50 or "name:" in name.lower() or "\n" in name:
            raise ValueError("Invalid name format returned by model")
        return name
    except Exception as e:
        print("Name extraction error, falling back:", e)
        # Monospace/line-based fallback
        lines = [line.strip() for line in header.split('\n') if line.strip()]
        for line in lines[:3]:
            # First line that doesn't look like contact info
            if "@" not in line and "phone" not in line.lower() and "http" not in line.lower() and len(line) > 2 and len(line) < 40:
                return line
        return "Candidate"