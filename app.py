from flask import Flask, send_file, request
from openai import OpenAI

app = Flask(__name__)

API_KEY = open("api-key.txt", "r", encoding="utf-8").read()
MODEL = "gpt-4-1106-preview"
client = OpenAI(api_key=API_KEY)


@app.route("/")
def get_data():
    return send_file("index.html")


@app.route("/prompt", methods=["POST"])
def prompt():
    data = request.get_json()
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": data["searchText"]}], model=MODEL
    )
    return {"text": response.choices[0].message.content}

if __name__ == "__main__":
    app.run(debug=True)
