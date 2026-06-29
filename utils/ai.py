from ollama import chat
import json


def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an expert ATS Resume Analyzer.

Compare the resume with the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Return ONLY valid JSON in this exact format:

{{
    "score": 85,
    "matched_skills": [
        "Python",
        "SQL",
        "Git"
    ],
    "missing_skills": [
        "Docker",
        "AWS"
    ],
    "suggestions": [
        "Learn Docker",
        "Add AWS projects",
        "Quantify achievements"
    ]
}}

Return ONLY JSON.
"""

    response = chat(
        model="llama3:latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return json.loads(response.message.content)