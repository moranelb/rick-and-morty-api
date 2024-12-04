from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://rickandmortyapi.com/api/character"

def fetch_all_characters():
    """
    Fetch all characters from the Rick and Morty API with pagination.
    """
    characters = []
    url = API_URL
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            characters.extend(data["results"])
            url = data.get("info", {}).get("next")
        else:
            break
    return characters

@app.route("/fetch_characters", methods=["GET"])
def fetch_characters():
    """
    Fetch and filter characters based on query parameters.
    """
    species = request.args.get("species", "")
    status = request.args.get("status", "")
    origin = request.args.get("origin", "")

    characters = fetch_all_characters()
    filtered_characters = [
        {
            "Name": char["name"],
            "Origin": char["origin"]["name"],
            "Image": char["image"]
        }
        for char in characters
        if (
            species.lower() in char["species"].lower()
            and status.lower() in char["status"].lower()
            and origin.lower() in char["origin"]["name"].lower()
        )
    ]
    return jsonify(filtered_characters), 200

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    """
    Healthcheck endpoint.
    """
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
