from pathlib import Path
from services.extractor import extract_text
from services.parser import parse_job_description
from config import JOB_DESCRIPTION

# resume_path = Path("resumes/Arnav_Amrit_resume.pdf")  
# text = extract_text(resume_path)
# print(text)

job = parse_job_description(JOB_DESCRIPTION)
print(job.role)
print(job.required_skills)
print(job.preferred_skills)
print(job.minimum_experience)
print(job.education_requirements)
print(job.responsibilities)