from ollama import chat
import json


def analyze_resume(score, matched_skills, missing_skills):

    prompt = f"""
You are an expert ATS Resume Reviewer.

The technical comparison has already been completed.

ATS Score: {score}

Matched Skills:
{matched_skills}

Missing Skills:
{missing_skills}

Your job is ONLY to provide professional feedback.

Rules:
- Base your analysis ONLY on the ATS score and the matched/missing skills.
- Do NOT invent new skills.
- Do NOT mention skills that are not listed.
- Return ONLY valid JSON.
- No markdown.
- No explanations.

Return this exact JSON format:

{{
    "strengths": [
        "Strength 1",
        "Strength 2",
        "Strength 3"
    ],

    "weaknesses": [
        "Weakness 1",
        "Weakness 2",
        "Weakness 3"
    ],

    "suggestions": [
        "Suggestion 1",
        "Suggestion 2",
        "Suggestion 3",
        "Suggestion 4",
        "Suggestion 5"
    ],

    "verdict": "Excellent Match"
}}
"""

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

    print("=" * 70)
    print(response.message.content)
    print("=" * 70)

    try:
        return json.loads(response.message.content)

    except json.JSONDecodeError:

        return {
            "strengths": [
                "Good technical foundation."
            ],
            "weaknesses": [
                "AI could not generate detailed feedback."
            ],
            "suggestions": [
                "Try running the analysis again."
            ],
            "verdict": "Analysis Completed"
        }