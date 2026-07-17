from pathlib import Path

from services.extractor import extract_text
from services.resume_parser import parse_resume

resume_path = Path("resumes/Arnav_Amrit_resume.pdf")

resume_text = extract_text(resume_path)

resume = parse_resume(resume_text)

print("\n========== Resume ==========\n")

print(f"Name: {resume.name}")
print(f"Email: {resume.email}")
print(f"Phone: {resume.phone}")
print(f"Experience: {resume.total_experience_years} years")

print("\nSkills:")
print(resume.skills)

print("\nExperiences:")
for exp in resume.experiences:
    print(f"\nCompany: {exp.company}")
    print(f"Role: {exp.role}")
    print(f"Duration: {exp.duration}")
    print(f"Description: {exp.description}")
    print(f"Skills Used: {exp.skills_used}")

print("\nEducation:")
print(resume.education)

print("\nProjects:")
print(resume.projects)

print("\nCertifications:")
print(resume.certifications)