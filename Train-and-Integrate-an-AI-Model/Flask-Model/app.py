from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load the trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        genre = data.get("genre", "")

        if not genre:
            return jsonify({"error": "Genre is missing"}), 400

        # Transform and predict
        X = vectorizer.transform([genre])
        prediction = model.predict(X)[0]

        return jsonify({"liked": bool(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
