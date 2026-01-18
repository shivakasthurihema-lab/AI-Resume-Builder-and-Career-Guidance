from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
from agents.resume_agent import optimize_resume
from agents.career_agent import suggest_career
from flask import Flask, request, jsonify
from agents.orchestator import run_career_workflow

app = Flask(__name__)

@app.route("/career-agent", methods=["POST"])
def career_agent():
    data = request.json
    user_skills = data["skills"]

    result = run_career_workflow(user_skills)
    return jsonify(result)

app.run()


app = Flask(__name__)

@app.route("/resume", methods=["POST"])
def resume():
    data = request.json
    result = optimize_resume(data["resume"], data["role"])
    return jsonify(result)

@app.route("/career", methods=["POST"])
def career():
    data = request.json
    result = suggest_career(data["skills"])
    return jsonify(result)

app.run()


load_dotenv()

IBM_API_KEY = os.getenv("IBM_WATSONX_API_KEY")
MODEL_ID = os.getenv("IBM_GRANITE_MODEL_ID")


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return jsonify(message='Backend is running'), 200


@app.route('/resume', methods=['POST'])
def resume():
    data = request.get_json(silent=True) or {}
    resume_text = data.get('resume') if isinstance(data, dict) else None
    if not resume_text:
        return jsonify(error='Missing "resume" in JSON body'), 400

    processed = process_resume(resume_text)
    return jsonify(status='ok', **processed), 200


def process_resume(text: str) -> dict:
    """Lightweight resume processing for demo purposes.

    Returns: skills, word_count, education (lines), experience_years_estimate,
    summary (first 30 words), and a simple optimized_resume string.
    """
    import re

    skills_master = [
        'python', 'flask', 'django', 'javascript', 'react', 'node', 'sql', 'mongodb',
        'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'git', 'linux', 'html', 'css',
        'java', 'c++', 'c#', 'pandas', 'numpy', 'scikit-learn'
    ]

    # normalize
    lower = text.lower()
    words = re.findall(r"\w+", lower)
    word_count = len(words)

    # detect skills present
    found_skills = sorted({s for s in skills_master if re.search(r"\\b" + re.escape(s) + r"\\b", lower)})

    # simple education detection: lines containing degree keywords
    education_lines = [line.strip() for line in text.splitlines() if re.search(r"\b(bachelor|master|b.sc|m.sc|bachelor's|master's|phd|college|university)\b", line, re.I)]

    # estimate experience by looking for patterns like 'X years' or year ranges
    years = 0
    m = re.search(r"(\d+)\s+years", lower)
    if m:
        try:
            years = int(m.group(1))
        except Exception:
            years = 0
    else:
        # look for year ranges like 2018-2022
        ranges = re.findall(r"(19|20)\d{2}\s*[-–]\s*(19|20)\d{2}", text)
        if ranges:
            # crude: take first range and compute difference
            rng = re.search(r"((19|20)\d{2})\s*[-–]\s*((19|20)\d{2})", text)
            if rng:
                try:
                    start = int(rng.group(1))
                    end = int(rng.group(3))
                    years = max(0, end - start)
                except Exception:
                    years = 0

    # summary: first 30 words
    summary = ' '.join(words[:30])

    # optimized resume (very simple improvements): ensure headings and bullet format
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
        'skills': found_skills,
        'education': education_lines,
        'experience_years_estimate': years,
        'summary': summary,
        'optimized_resume': optimized_resume,
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

