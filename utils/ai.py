from ollama import chat
import json


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

    print(response.message.content)

    return json.loads(response.message.content)