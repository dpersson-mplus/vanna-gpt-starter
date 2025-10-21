import requests
import json
import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/query_vanna", methods=["POST"])
def query_vanna():
    request_json = request.get_json(silent=True)

    # Validate required fields
    required_fields = ["message", "user_email", "agent_id"]
    for field in required_fields:
        if field not in request_json:
            return json.dumps({"error": f"Missing required field: {field}"}), 400, {"Content-Type": "application/json"}

    API_URL = "https://app.vanna.ai/api/v0/chat_sse"
    API_KEY = os.environ.get("VANNA_API_KEY")

    if not API_KEY:
        return json.dumps({"error": "Missing VANNA_API_KEY in environment variables."}), 500, {"Content-Type": "application/json"}

    headers = {
        "Content-Type": "application/json",
        "VANNA-API-KEY": API_KEY
    }

    payload = {
        "message": request_json["message"],
        "user_email": request_json["user_email"],
        "agent_id": request_json["agent_id"],
        "acceptable_responses": request_json.get("acceptable_responses", ["text", "image", "link"])
    }

    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload), stream=True)
        response.raise_for_status()

        result = []
        for line in response.iter_lines():
            if line and line.decode('utf-8').startswith("data:"):
                data = json.loads(line.decode('utf-8')[5:].strip())
                result.append(data)
                if data.get("type") == "end":
                    break

        return json.dumps(result), 200, {"Content-Type": "application/json"}
    except Exception as e:
        return json.dumps({"error": str(e)}), 500, {"Content-Type": "application/json"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
