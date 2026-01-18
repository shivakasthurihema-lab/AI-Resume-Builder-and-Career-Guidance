# Back end - Flask test server

Quick steps to run locally and expose a public URL (ngrok):

1. Create and activate a Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r "requirements.txt"
```

3. Run the server:

```powershell
python "app.py"
```

The server listens on `http://127.0.0.1:5000` by default.

4. Expose it with ngrok (download from https://ngrok.com):

```powershell
ngrok http 5000
```

Copy the `https://...ngrok.io` URL and use it as your public backend URL.

Example test with curl:

```powershell
curl -X POST https://<your-ngrok-url>/resume -H "Content-Type: application/json" -d '{"resume":"I am a Python developer"}'
```
