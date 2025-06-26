# Vanna Custom GPT – Self-Hosted Starter Kit 🚀

This starter kit lets you run Vanna AI through your own Custom GPT by deploying a lightweight backend that forwards requests to the Vanna API.

## 🎥 Demo: Vanna Custom GPT in Action

[![Watch the demo](https://img.youtube.com/vi/99SeFvRPs98/0.jpg)](https://www.youtube.com/watch?v=99SeFvRPs98)

---

## 🌟 What’s Inside

- `main.py` — Flask app to relay requests to Vanna
- `requirements.txt` — Python dependencies
- `Procfile` — For Railway/Heroku deployment
- `openapi.yaml` — Upload to your Custom GPT
- `.env.example` — Template for environment variables
- `README.md` — You’re reading it 🙂

---

## 🛠 Step 1: Set Your API Key

Create a `.env` file by copying the example:

```bash
cp .env.example .env
```

Then edit `.env` and add your Vanna API key:

```env
VANNA_API_KEY=your-api-key-here
```

---

## 🚀 Step 2: Deploy the Backend

### Option A: Google Cloud Run

```bash
gcloud auth login

gcloud run deploy vanna-api \
  --source . \
  --entry-point app \
  --runtime python311 \
  --port 8080 \
  --allow-unauthenticated \
  --region us-central1 \
  --set-env-vars VANNA_API_KEY=your-api-key-here
```

---

### Option B: Railway (recommended for ease)

1. Go to [https://railway.app](https://railway.app) and log in
2. Create a new project and deploy this repo
3. Set an environment variable: `VANNA_API_KEY=your-api-key-here`
4. Railway will auto-detect the Flask app from `Procfile`

---

### Option C: Heroku

```bash
heroku login

heroku create vanna-api

heroku config:set VANNA_API_KEY=your-api-key-here

git push heroku main
```

---

## 🤖 Step 3: Set Up Your Custom GPT

1. Go to [https://chat.openai.com/gpts/new](https://chat.openai.com/gpts/new)
2. In the **Actions** tab, upload the `openapi.yaml` file
3. Update the `servers:` section in `openapi.yaml` with your deployed endpoint, e.g.:

```yaml
servers:
  - url: https://your-cloudrun-or-railway-url-here
```

4. Save and start chatting!

---

## 🙋 Need Help?

Reach out to your Vanna contact or support@vanna.ai for assistance.
