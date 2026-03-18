import json

# Load data
with open("data.json", "r") as f:
    items = json.load(f)

def get_recommendations(item_type, genre):
    results = []

    for item in items:
        if item["type"] == item_type and item["genre"] == genre:
            results.append(item["title"])

    return results