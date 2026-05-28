from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

transactions = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_transaction", methods=["POST"])
def add_transaction():
    data = request.get_json()

    print(data)  # Debug

    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    transaction = {
        "type": data.get("type"),
        "amount": data.get("amount"),
        "date": data.get("date"),
        "category": data.get("category"),
        "note": data.get("note")
    }

    transactions.append(transaction)

    return jsonify({
        "message": "Transaktion sparad!",
        "transactions": transactions
    })

@app.route("/get_transactions")
def get_transactions():
    return jsonify(transactions)

if __name__ == "__main__":
    app.run(debug=True)