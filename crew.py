from crewai import Crew, Task
from agents.job_analyzer import job_analyzer
from agents.resume_agent import resume_agent
from agents.messaging_agent import messaging_agent


def run_job_search_ai(job_description: str, candidate_profile: str):
    analyze_task = Task(
        description=f"Analyze the following job description and list required skills:\n{job_description}",
        expected_output="A bullet-point list of skills",
        agent=job_analyzer
    )

    resume_task = Task(
        description=(
            "Using the extracted skills and the candidate profile below, "
            "create a tailored one-page resume.\n\n"
            f"Candidate Profile:\n{candidate_profile}"
        ),
        expected_output="A professional one-page resume",
        agent=resume_agent
    )

    message_task = Task(
        description=(
            "Write a short, professional LinkedIn message (3–4 sentences) "
            "to a recruiter expressing interest in the role. "
            "Base it on the candidate profile above."
        ),
        expected_output="A short professional LinkedIn outreach message",
        agent=messaging_agent
    )

    crew = Crew(
        agents=[job_analyzer, resume_agent, messaging_agent],
        tasks=[analyze_task, resume_task, message_task],
        verbose=False,
        max_iterations=1
    )

    crew.kickoff()

    return {
        "skills": analyze_task.output,
        "resume": resume_task.output,
        "message": message_task.output
    }
