from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
MENU = [
    {"id": 1, "name": "Veg Burger", "price": 99},
    {"id": 2, "name": "Paneer Pizza", "price": 199},
    {"id": 3, "name": "French Fries", "price": 79},
]

@app.get("/")
def home():
    return render_template("index.html", menu=MENU)

@app.get("/health")
def health():
    return jsonify(status="healthy"), 200

@app.get("/api/menu")
def menu():
    return jsonify(MENU), 200

@app.post("/api/orders")
def create_order():
    data = request.get_json(silent=True) or {}
    item = next((x for x in MENU if x["id"] == data.get("item_id")), None)
    if not item:
        return jsonify(error="Invalid menu item"), 400
    return jsonify(message="Order placed successfully", item=item), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
