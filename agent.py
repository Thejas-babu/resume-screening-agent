import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
print("DEBUG GROQ KEY PREFIX:", os.getenv("GROQ_API_KEY")[:8])

SYSTEM_PROMPT = """
You are an expert technical recruiter.
Evaluate the resume strictly based on the job description.
Return JSON only:
{
  "score": number (0-100),
  "strengths": [],
  "weaknesses": [],
  "fit_percentage": number,
  "decision": "Strong Fit" | "Moderate Fit" | "Weak Fit",
  "reasoning": "..."
}
"""

def screen_resume(resume_text: str, jd_text: str):
    user_prompt = f"""
Job Description:
{jd_text}

Resume:
{resume_text}

Return JSON only.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   # 👈 IMPORTANT: exact model ID
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
        max_tokens=500,
    )

    output = response.choices[0].message.content

    try:
        return json.loads(output)
    except Exception:
        return {"error": "Invalid JSON", "raw": output}
