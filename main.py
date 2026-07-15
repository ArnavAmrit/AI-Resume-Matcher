from pathlib import Path
from services.extractor import extract_text

resume_path = Path("resumes/Arnav_Amrit_resume.pdf")  
text = extract_text(resume_path)
print(text)