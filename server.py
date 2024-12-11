from flask import Flask, jsonify, Response, request
import json

app = Flask(__name__)

@app.route("/api/elements")
def order_route():
    with open("table.json", "r") as f:
        data = json.load(f)
    return jsonify(data['order'])

@app.route('/api/elements/<element_key>')
def element_route(element_key):
    with open("table.json", "r") as f:
        data = json.load(f)
    data[element_key]['svg_url'] = f"{request.url_root}vector/elements/{element_key}"
    return jsonify(data[element_key])

@app.route('/vector/elements/<element_key>')
def svg_route(element_key):
    file = "elements/" + element_key + ".svg"
    with open(file, "rb") as f:
        svg_data = f.read()
    return Response(svg_data, mimetype="image/svg+xml")

if __name__ == "__main__":
    app.run(debug=True)
