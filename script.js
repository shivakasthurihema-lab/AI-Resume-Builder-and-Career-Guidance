function optimizeResume() {
    const text = document.getElementById('resumeText')?.value || '';
    if (text.trim()) {
        postResume(text);
    } else {
        document.getElementById("resumeOutput").innerHTML =
            "✅ Your resume has been optimized using AI (IBM Granite Model).";
    }
}

function optimizeResumeSample() {
    let text =document.getElementById('resumeText')?.value || '';
    postResume(text);
    alert("✅ Your resume has been optimized using AI (IBM Granite Model).");
}

function getCareer() {
    document.getElementById("careerOutput").innerHTML =
        "🎓 Suggested Career Path: Software Engineer / Data Analyst<br>📚 Recommended Skills: DSA, Cloud, Python";
}

// Send resume text to local backend `POST /resume` and show response
function postResume(resumeText) {
    fetch("https://abcd-123-45.ngrok.io/career", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ skills: "Python, Java" })
})
.then(res => res.json())
.then(data => console.log(data));
    fetch("http://localhost:5000/resume", {
    })
    .then(response => response.json())
    .then(data => {
        if (data.status && data.status === 'ok') {
            const skills = (data.skills && data.skills.length) ? data.skills.join(', ') : 'None detected';
            const education = (data.education && data.education.length) ? data.education.join('<br>') : 'None detected';
            const optimized = data.optimized_resume ? escapeHtml(data.optimized_resume).replace(/\n/g, '<br>') : '';
            const html = `
                <strong>Word count:</strong> ${data.word_count || 0}<br>
                <strong>Estimated experience (years):</strong> ${data.experience_years_estimate || 0}<br>
                <strong>Skills:</strong> ${skills}<br>
                <strong>Education:</strong><br>${education}<br>
                <strong>Optimized Resume:</strong><div class="output-pre">${optimized}</div>
            `;
            document.getElementById('resumeOutput').innerHTML = html;
        } else {
            const out = data.error ?? JSON.stringify(data);
            document.getElementById('resumeOutput').innerText = 'Server response: ' + out;
        }
    })
    .catch(err => {
        document.getElementById('resumeOutput').innerHTML = 'Error: ' + err.message;
    });
}

// Helper to post a sample resume
function sendSampleResume() {
    postResume('I am a Python developer with Flask experience');
}

function escapeHtml(unsafe) {
    return unsafe
         .replace(/&/g, '&amp;')
         .replace(/</g, '&lt;')
         .replace(/>/g, '&gt;')
         .replace(/"/g, '&quot;')
         .replace(/'/g, '&#039;');
}
