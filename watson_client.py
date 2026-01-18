import os
import re
from urllib import response
from wsgiref import headers
import requests
from dotenv import load_dotenv
load_dotenv()
    
IBM_API_KEY = os.getenv("IBM_WATSONX_API_KEY")
PROJECT_ID = os.getenv("IBM_WATSONX_PROJECT_ID")
BASE_URL = os.getenv("IBM_WATSONX_URL")
MODEL_ID = os.getenv("IBM_GRANITE_MODEL_ID")

def get_iam_token(api_key):
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": api_key
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]


def granite_generate(prompt):
    access_token = get_iam_token(IBM_API_KEY)

    url = f"{BASE_URL}/ml/v1/text/generation?version=2023-05-29"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "model_id": MODEL_ID,
        "input": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.7
        },
        "project_id": PROJECT_ID
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def granite_chat(messages):
    url = f"{BASE_URL}/ml/v1/chat/completions?version=2023-05-29"

    headers = {
        "Authorization": f"Bearer {IBM_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model_id": MODEL_ID,
        "messages": messages,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.5
        },
        "project_id": PROJECT_ID
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()
    print(granite_generate("Write a short professional resume summary for a software engineering student"))

def granite_embed(texts):
    url = f"{BASE_URL}/ml/v1/embeddings?version=2023-05-29"

    headers = {
        "Authorization": f"Bearer {IBM_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model_id": MODEL_ID,
        "input": texts,
        "project_id": PROJECT_ID
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()
def granite_list_models():
    url = f"{BASE_URL}/ml/v1/models?version=2023-05-29"

    headers = { 
        "Authorization": f"Bearer {IBM_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    return response.json()
def granite_get_model_details(model_id):
    url = f"{BASE_URL}/ml/v1/models/{model_id}?version=2023-05-29"

    headers = { 
        "Authorization": f"Bearer   {IBM_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()  
def granite_list_projects():
    url = f"{BASE_URL}/ml/v1/projects?version=2023-05-29"

    headers = { 
        "Authorization": f"Bearer {IBM_API_KEY}",
        "Content-Type": "application/json"      
    }
    response = requests.get(url, headers=headers)
    return response.json()
    return response.json()  
def granite_get_project_details(project_id):
    url = f"{BASE_URL}/ml/v1/projects/{project_id}?version=2023-05-29"

    headers = { 
        "Authorization": f"Bearer {IBM_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()
    return response.json()  
def granite_list_deployments():
    url = f"{BASE_URL}/ml/v1/deployments?version=2023-05-29"

    headers = { 
        "Authorization": f"Bearer {IBM_API_KEY}",
        "Content-Type": "application/json"  
    }
    response = requests.get(url, headers=headers)
    return response.json()

def granite_get_deployment_details(deployment_id):
    url = f"{BASE_URL}/ml/v1/deployments/{deployment_id}?version=2023-05-29"

    headers = {     
        "Authorization": f"Bearer {IBM_API_KEY}",               
        "Content-Type": "application/json"  
    }
    response = requests.get(url, headers=headers)   
    return response.json()
   
def granite_invoke_deployment(deployment_id, input_data):
    url = f"{BASE_URL}/ml/v1/deployments/{deployment_id}/invoke?version=2023-05-29"

    headers = {     
        "Authorization": f"Bearer {IBM_API_KEY}",            
        "Content-Type": "application/json"                  
    }       
    payload = {
        "input": input_data
    }       
    response = requests.post(url, headers=headers, json=payload)
    return response.json()  

def granite_list_jobs():
    url = f"{BASE_URL}/ml/v1/jobs?version=2023-05-29"

    headers = { 
        "Authorization": f"Bearer {IBM_API_KEY}",   
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)   
    return response.json()
    return response.json()
def granite_get_job_details(job_id):
    url = f"{BASE_URL}/ml/v1/jobs/{job_id}?version=2023-05-29"

    headers = {
        "Authorization": f"Bearer {IBM_API_KEY}",   
        "Content-Type": "application/json"          
    }
    response = requests.get(url, headers=headers)
    return response.json()

def granite_cancel_job(job_id):
    url = f"{BASE_URL}/ml/v1/jobs/{job_id}/cancel?version=2023-05-29"

    headers ={
        "Authorization": f"Bearer {IBM_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers)  
    return response.json()
def granite_list_datasets():
    url = f"{BASE_URL}/ml/v1/datasets?version=2023-05-29"

    headers = {
        "Authorization": f"Bearer {IBM_API_KEY}",   
        "Content-Type": "application/json"      
    }
    response = requests.get(url, headers=headers)
    return response.json()  
def granite_get_dataset_details(dataset_id):

    url = f"{BASE_URL}/ml/v1/datasets/{dataset_id}?version=2023-05-29"

    headers = {
        "Authorization": f"Bearer {IBM_API_KEY}",   
        "Content-Type": "application/json"              
    }
    response = requests.get(url, headers=headers)
    return response.json()
def granite_delete_dataset(dataset_id):
    url = f"{BASE_URL}/ml/v1/datasets/{dataset_id}?version=2023-05-29"

    headers ={
        "Authorization": f"Bearer {IBM_API_KEY}",   
        "Content-Type": "application/json"      
    }
    response = requests.delete(url, headers=headers)
    return response.json()
def granite_create_dataset(name, description, file_path):
    url = f"{BASE_URL}/ml/v1/datasets?version=2023-05-29"

    headers = {
        "Authorization": f"Bearer {IBM_API_KEY}",   
        "Content-Type": "multipart/form-data"
    }
    files = {
        'file': open(file_path, 'rb')
    }
    data = {
        'name': name,
        'description': description
    }
    response = requests.post(url, headers=headers, files=files, data=data)
    return response.json()

def granite_update_dataset(dataset_id, name=None, description=None):
    url = f"{BASE_URL}/ml/v1/datasets/{dataset_id}?version=2023-05-29"

    headers = {
        "Authorization": f"Bearer {IBM_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {}
    if name is not None:
        data['name'] = name
    if description is not None:
        data['description'] = description
    response = requests.put(url, headers=headers, json=data)
    return response.json()

    return {
        'received': text,
        'word_count': word_count,
        'skills_found': found_skills,
        'education': education_lines,
        'years_experience': years,
        'summary': summary,
        'optimized_resume': optimized_resume
    }
    skills = [
        "project management", "communication", "sql", "aws", "docker",
        "kubernetes", "react", "node.js", "html", "css", "git"
    ]
    lower = text.lower()
    words = re.findall(r"\w+", lower)
    word_count = len(words)
    found_skills = sorted({s for s in skills if re.search(r"\b" + re.escape(s) + r"\b", lower)})
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
def suggest_career(skills_text):
    skills = [
        "project management", "communication", "sql", "aws", "docker",
        "kubernetes", "react", "node.js", "html", "css", "git"
    ]
    lower = skills_text.lower()
    words = re.findall(r"\w+", lower)
    word_count = len(words)
    found_skills = sorted({s for s in skills if re.search(r"\b" + re.escape(s) + r"\b", lower)})
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
def suggest_career(skills_text):
    skills = [
        "project management", "communication", "sql", "aws", "docker",
        "kubernetes", "react", "node.js", "html", "css", "git"
    ]
    lower = skills_text.lower()
    words = re.findall(r"\w+", lower)
    word_count = len(words)
    found_skills = sorted({s for s in skills if re.search(r"\b" + re.escape(s) + r"\b", lower)})
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
def suggest_career(skills_text):
    skills = [
        "project management", "communication", "sql", "aws", "docker",
        "kubernetes", "react", "node.js", "html", "css", "git"
    ]
    lower = skills_text.lower()
    words = re.findall(r"\w+", lower)
    word_count = len(words)
    found_skills = sorted({s for s in skills if re.search(r"\b" + re.escape(s) + r"\b", lower)})
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
def suggest_career(skills_text):
    skills = [
        "project management", "communication", "sql", "aws", "docker",
        "kubernetes", "react", "node.js", "html", "css", "git"
    ]
    lower = skills_text.lower()
    words = re.findall(r"\w+", lower)
    word_count = len(words)
    found_skills = sorted({s for s in skills if re.search(r"\b" + re.escape(s) + r"\b", lower)})
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
def suggest_career(skills_text):
    skills = [
        "project management", "communication", "sql", "aws", "docker",
        "kubernetes", "react", "node.js", "html", "css", "git"
    ]
    lower = skills_text.lower()
    words = re.findall(r"\w+", lower)
    word_count = len(words)
    found_skills = sorted({s for s in skills if re.search(r"\b" + re.escape(s) + r"\b", lower)})
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
def suggest_career(skills_text):
    skills = [
        "project management", "communication", "sql", "aws", "docker",
        "kubernetes", "react", "node.js", "html", "css", "git"
    ]
    lower = skills_text.lower()
    words = re.findall(r"\w+", lower)
    word_count = len(words)
    found_skills = sorted({s for s in skills if re.search(r"\b" + re.escape(s) + r"\b", lower)})
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
def suggest_career(skills_text):
    skills = [
        "project management", "communication", "sql", "aws", "docker",
        "kubernetes", "react", "node.js", "html", "css", "git"
    ]
    lower = skills_text.lower()
    words = re.findall(r"\w+", lower)
    word_count = len(words)
    found_skills = sorted({s for s in skills if re.search(r"\b" + re.escape(s) + r"\b", lower)})
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
def suggest_career(skills_text):
    skills = [
        "project management", "communication", "sql", "aws", "docker",
        "kubernetes", "react", "node.js", "html", "css", "git"
    ]
    lower = skills_text.lower()
    words = re.findall(r"\w+", lower)
    word_count = len(words)
    found_skills = sorted({s for s in skills if re.search(r"\b" + re.escape(s) + r"\b", lower)})
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