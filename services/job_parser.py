import os
from groq import Groq
from dotenv import load_dotenv
import json
from models.job import JobD
from config import MODEL_NAME, TEMPERATURE, JOB_DESCRIPTION

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

client = Groq(api_key=my_api_key)


def parse_job_description(job_description: str) -> JobD:
    jobD_schema = JobD.model_json_schema()
    system_prompt = f"""
    You are an expert HR assistant.

    Your job is to analyze job descriptions and extract
    structured information from them.

    Return ONLY valid JSON matching this schema:

    {jobD_schema}
    IMPORTANT:
    Do NOT return the schema itself.
    Do NOT return fields like "properties", "title" or "type".
    Fill the schema with actual information extracted from the job description.

    If minimum experience is not mentioned, return null.
    If information for a list is missing, return an empty list.
    Do not invent information.
    """

    user_prompt = f"""
    Analyze the following job description:

    {job_description}
    """
    message_system={
        "role" : "system",
        "content" : system_prompt
    }
    message_user={
        "role" : "user",
        "content" : user_prompt
    }
    response_format={
        "type" : "json_object"
    }
    messages=[message_system, message_user]

    response=client.chat.completions.create(model=MODEL_NAME, messages=messages, response_format=response_format)

    answer=response.choices[0].message.content

    raw_json=answer

    job_data = json.loads(raw_json)
    job = JobD(**job_data)
    return job