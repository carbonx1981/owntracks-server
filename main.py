from flask import Flask, request
import json
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "OwnTracks Server Online"

@app.route('/')
def map_view():
    return render_template("index.html")

@app.route("/owntracks", methods=["POST"])
def owntracks():
    data = request.json
    print(f"Received: {json.dumps(data)}")
    with open("gps_log.json", "a") as f:
        f.write(json.dumps({"timestamp": time.time(), "data": data}) + "\n")
    return "OK", 200
