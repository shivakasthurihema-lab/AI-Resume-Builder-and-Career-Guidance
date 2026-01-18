def suggest_career(skills):
    return {
        "recommended_roles": [
            "Software Engineer",
            "Data Analyst"
        ],
        "next_skills": [
            "DSA",
            "Cloud Computing",
            "Python"
        ]
    }
import re
def analyze_resume(text):
    # load skills master list
    skills_master = [
        "python", "java", "c++", "machine learning", "data analysis",
        "project management", "communication", "sql", "aws", "docker",
        "kubernetes", "react", "node.js", "html", "css", "git"
    ]
    lower = text.lower()
    words = re.findall(r"\w+", lower)
    word_count = len(words)
    found_skills = sorted({s for s in skills_master if re.search(r"\b" + re.escape(s) + r"\b", lower)})
    education_lines = [line.strip() for line in text.splitlines() if re.search(r"\b(bachelor|master|phd|college|university)\b", line, re.I)]
    years = 0
    m = re.search(r"(\d+)\s+years", lower)
    if m:
        try:
            years = int(m.group(1))
        except Exception:
            years = 0
    else:
        ranges = re.findall(r"(19|20)\d{2}\s*[-–]\s*(19|20)\d{2}", text)
        if ranges:
            rng = re.search(r"((19|20)\d{2})\s*[-–]\s*((19|20)\d{2})", text)
            if rng:
                try:
                    start = int(rng.group(1))
                    end = int(rng.group(3))
                    years = max(0, end - start)
                except Exception:
                    years = 0
    summary = ' '.join(words[:30])
    optimized = []
    optimized.append('PROFESSIONAL SUMMARY')
    optimized.append((summary + '...').capitalize())
    optimized.append('\nSKILLS')
    optimized.append(', '.join(found_skills) or 'No recognized skills found')
    if education_lines:
        optimized.append('\nEDUCATION')
        optimized.extend(education_lines)
    optimized_resume = '\n'.join(optimized)
    return {
        'received': text,
        'word_count': word_count,
        'skills_found': found_skills,
        'education': education_lines,
        'years_experience': years,
        'summary': summary,
        'optimized_resume': optimized_resume
    }