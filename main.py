from pathlib import Path

from config import JOB_DESCRIPTION
from services.extractor import extract_text
from services.job_parser import parse_job_description
from services.resume_parser import parse_resume
from services.matcher import final_score


# Step 1: Extract resume text
resume_path = Path("resumes/Arnav_Amrit_resume.pdf")
resume_text = extract_text(resume_path)

# Step 2: Parse the resume
resume = parse_resume(resume_text)

# Step 3: Parse the job description
job = parse_job_description(JOB_DESCRIPTION)

# Step 4: Match resume with job
match = final_score(job, resume)

# Step 5: Print the result
print("\n========== MATCH RESULT ==========\n")

print(match.model_dump_json(indent=4))