import os

def skill_gap_analysis(current_skills, target_role):
    # Simulated mapping (IBM SkillsBuild-aligned)
    role_skill_map = {
        "Software Engineer": [
            "Data Structures",
            "Algorithms",
            "Python",
            "Java",
            "Cloud Computing",
            "Git"
        ],
        "Data Analyst": [
            "Python",
            "SQL",
            "Statistics",
            "Data Visualization",
            "Excel"
        ]
    }

    required_skills = role_skill_map.get(target_role, [])
    missing_skills = list(set(required_skills) - set(current_skills))

    # IBM SkillsBuild-style recommendations
    courses = [
        f"IBM SkillsBuild: {skill}" for skill in missing_skills
    ]

    return {
        "target_role": target_role,
        "missing_skills": missing_skills,
        "recommended_courses": courses
    }
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
    # Extract skills from resume text
    skills = re.findall(r'\b(?:Python|Java|SQL|Git|Cloud Computing|Data Structures|Algorithms|Statistics|Data Visualization)\b', text, re.IGNORECASE)
    return skills

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
