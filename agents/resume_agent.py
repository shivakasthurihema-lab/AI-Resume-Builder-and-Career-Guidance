from watson_client import granite_generate

def optimize_resume(resume_text, role):
    prompt = f"""
    Optimize the following resume for the role of {role}.
    Make it ATS-friendly and professional.

    Resume:
    {resume_text}
    """
    return granite_generate(prompt)
