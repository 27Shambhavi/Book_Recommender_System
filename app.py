from flask import Flask, request, jsonify, render_template
from model import BookRecommender

app = Flask(__name__)
recommender = BookRecommender()

@app.route("/")
def home():
    # ✅ render frontend instead of plain string
    popular_books = recommender.get_popular()
    return render_template("index.html", popular_books=popular_books)

@app.route("/recommend", methods=["GET"])
def recommend():
    title = request.args.get("title")
    if not title:
        return jsonify({"error": "Please provide a book title"}), 400
    
    recommendations = recommender.recommend(title)
    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
