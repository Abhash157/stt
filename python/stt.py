from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

DEEPGRAM_API_KEY = "1d7cf8ab4f0d07ccd53029aac8db2a518d0a7d74"


@app.route('/upload', methods=['POST'])
def upload_audio():
    audio_data = request.data

    # Save raw audio file
    with open("audio.raw", "wb") as f:
        f.write(audio_data)

    headers = {
        "Authorization": f"Token {DEEPGRAM_API_KEY}",
        "Content-Type": "application/octet-stream"
    }

    with open("audio.raw", "rb") as f:
        response = requests.post(
            "https://api.deepgram.com/v1/listen?encoding=linear16&sample_rate=8000&channels=1",
            headers=headers,
            data=f
        )
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": response.text}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
