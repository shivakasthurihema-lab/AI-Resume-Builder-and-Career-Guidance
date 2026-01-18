from agents.career_agent import suggest_career
from agents.skills_agent import skill_gap_analysis
from agents.ai_career_agent import chatgpt_career_guidance

def run_career_workflow(user_skills):
    # Step 1: Career suggestion
    career_info = suggest_career(user_skills)
    target_role = career_info["recommended_roles"][0]

    # Step 2: Skill gap analysis
    skills_info = skill_gap_analysis(user_skills, target_role)

    # Step 3: AI guidance
    ai_guidance = chatgpt_career_guidance(user_skills)

    return {
        "career_roles": career_info["recommended_roles"],
        "skill_gap": skills_info,
        "ai_guidance": ai_guidance
    }