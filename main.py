from pathlib import Path
import time

from config import JOB_DESCRIPTION
from services.extractor import extract_text
from services.job_parser import parse_job_description
from services.resume_parser import parse_resume
from services.matcher import final_score


# Parse the job description once
job = parse_job_description(JOB_DESCRIPTION)

resume_folder = Path("resumes")
all_results = []

for file_path in resume_folder.iterdir():

    # Skip unsupported files
    if file_path.suffix.lower() not in [".pdf", ".docx"]:
        continue

    print(f"\nProcessing: {file_path.name}")

    # Step 1: Extract resume text
    resume_text = extract_text(file_path)

    # Step 2: Parse resume
    resume = parse_resume(resume_text)

    # Optional: Avoid API rate limits
    time.sleep(5)

    # Step 3: Match resume with job
    match = final_score(job, resume)

    # Optional: Avoid API rate limits
    time.sleep(5)

    print(f"Score: {match.score}%")

    all_results.append({
        "name": resume.name,
        "score": match.score,
        "details": match.details
    })


# Sort candidates by score
all_results.sort(
    key=lambda candidate: candidate["score"],
    reverse=True
)

top_2 = all_results[:2]
lowest_2 = all_results[-2:]


print("\n========== TOP 2 CANDIDATES ==========")

for candidate in top_2:
    print(f"\n{candidate['name']} - {candidate['score']}%")
    print(candidate["details"])


print("\n========== LOWEST 2 CANDIDATES ==========")

for candidate in lowest_2:
    print(f"\n{candidate['name']} - {candidate['score']}%")
    print(candidate["details"])