from flask import Flask, jsonify, request, render_template

# ========= An online store app

app = Flask(__name__)  # give each app a unique name

stores = [
    {
        "name": "randomstore",
        "items": [
            {"name": "My Item 1", "price": 50.99},
            {"name": "My Item 2", "price": 39.99},
        ]
    }
]


# GET /
@app.route("/")  # when hit /
def home():
    # flask will automatically search for the template dir
    return render_template("index.html")


# POST /store
@app.route("/store", methods=["POST"])
def create_store():
    req_data = request.get_json()
    print("req", req_data)
    new_store = {
        "name": req_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify({"store": stores})

# GET /store/name


@app.route("/store/<string:name>")
def get_store(name):

    for s in stores:
        if s["name"] == name:
            return jsonify({"store": s})

    return jsonify({"error": "store not found"})


# GET /store
@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})


# POST /store
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    req_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            store["items"].append({
                "name": req_data["name"],
                "price": req_data["price"]
            })
            return jsonify({"stores": stores})

    return jsonify({"error": "store not found"})


# GET /store
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for s in stores:
        if s["name"] == name:
            return jsonify({"items": s["items"]})

    return jsonify({"error": "store not found"})


app.run(port=5000)
