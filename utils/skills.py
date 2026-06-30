import re

SKILLS = {
    "python": "Python",
    "java": "Java",
    "c": "C",
    "c++": "C++",
    "sql": "SQL",
    "html": "HTML",
    "css": "CSS",
    "javascript": "JavaScript",
    "react": "React",
    "react.js": "React",
    "node.js": "Node.js",
    "flask": "Flask",
    "django": "Django",
    "fastapi": "FastAPI",
    "rest api": "REST API",
    "rest apis": "REST API",
    "git": "Git",
    "github": "GitHub",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "aws": "AWS",
    "azure": "Azure",
    "gcp": "GCP",
    "mongodb": "MongoDB",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",
    "linux": "Linux",
    "tensorflow": "TensorFlow",
    "pytorch": "PyTorch",
    "pandas": "Pandas",
    "numpy": "NumPy",
    "scikit-learn": "Scikit-learn",
    "machine learning": "Machine Learning",
    "deep learning": "Deep Learning",
    "langchain": "LangChain",
    "llm": "LLM",
    "large language model": "LLM",
    "rag": "RAG",
    "retrieval augmented generation": "RAG",
    "generative ai": "Generative AI",
    "data structures": "Data Structures",
    "algorithms": "Algorithms",
    "oop": "Object-Oriented Programming",
    "object-oriented programming": "Object-Oriented Programming",
}


def extract_skills(text):
    text = text.lower()
    found = set()

    for keyword, skill in SKILLS.items():
        pattern = r"\b" + re.escape(keyword) + r"\b"
        if re.search(pattern, text):
            found.add(skill)

    return sorted(found)


def compare_skills(resume_skills, jd_skills):
    matched = sorted(set(resume_skills) & set(jd_skills))
    missing = sorted(set(jd_skills) - set(resume_skills))
    return matched, missing