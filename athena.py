import google.generativeai as genai 
import os, json, sys

if len(sys.argv) < 2:
    print("Missing all arguments: Policy.pdf and Application.json Required")

policy_path = "loan_policy.pdf"
application_path = sys.argv[1]

os.environ["GEMINI_API_KEY"] = "AIzaSyAZQ2AdgCBH41vWQK_c9xs5ZN6yYauuR44"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])



policy = genai.upload_file(path=policy_path)

with open(application_path, "r", encoding="utf-8") as f:
    application = json.load(f)

prompt = f"""
You are an underwriting AI agent. The loan policy is attached as a pdf.
Apply the rules given in the pdf to this loan application:
{json.dumps(application, indent=2)}

Return JSON in the format:
{{
    "decision": "approved" or "denied",
    "riskLevel": "low" | "medium" | "high", 
    "reasoning": "Short Explanation (3 sentences)"
}}
"""

model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content([prompt, policy])

text = response.text.strip()
if text.startswith("```"):
    text = text.strip("`")
    if text.startswith("json\n"):
        text = text[5:]

result = json.loads(text)

print(json.dumps(result, indent=2))
